import json
import time
import requests
from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Transaction


@api_view(http_method_names=["POST"])
def pay(request: HttpRequest):
    appid = 0
    url1 = "https://astrontest.uz/mypage/api/userid.php"
    url2 = "https://astrontest.uz/mypage/api/payment.php"
    body = request.body.decode()
    body = json.loads(body)

    if body.get("method") == "CheckPerformTransaction":
        print("Tekshiruvda...")
        appid = body.get("params").get("account").get("appid")
        try:
            appid = int(appid)
        except:
            appid = 0
        res = requests.post(url=url1, data={ "id": appid })
        if res.json().get("status") == "success":
            return Response({
                "jsonrpc": "2.0",
                "id": appid,
                "result": {
                    "allow": True,
                    "additional": {
                        "id": 1,
                        "name": "Alisher",
                        "balance": 1000,
                    }
                }
            })
        else:
            return Response({
                "error": {
                    "code": -31050,
                    "message": {
                        "en": "User not found",
                        "ru": "User not found",
                        "uz": "Foydalanuvchi topilmadi"
                    }
                }
            })
        
    if body.get("method") == "CreateTransaction":
        print("Yaratildi...")
        Transaction.objects.create(
            id=body.get("params").get("id"),
            appid=body.get("params").get("account").get("appid"),
            state="1"
        )
        return Response({
            "result": {
                "create_time": body.get("params").get("time"),
                "transaction": body.get("params").get("id"),
                "state": 1
            }
        })
    if body.get("method") == "PerformTransaction":
        print("To'landi...")
        transaction = Transaction.objects.get(id=body.get("params").get("id"))
        transaction.state = "2"
        transaction.save()
        appid = transaction.appid
        try:
            appid = int(appid)
        except:
            appid = appid
        res = requests.post(url=url2, data={ "id": appid })
        return Response({
            "result": {
                "transaction" : body.get("params").get("id"),
                "perform_time" : int(time.time()),
                "state" : 2
            }
        })
    if body.get("method") == "CancelTransaction":
        print("Bekor qilindi...")
        return Response({
            "result" : {
                "transaction" : body.get("params").get("id"),
                "calcel_time" : int(time.time()),
                "state" : -2
            }
        })