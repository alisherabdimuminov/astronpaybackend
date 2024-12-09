from django.db import models


class Transaction(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    appid = models.CharField(max_length=100)
    state = models.IntegerField()
    amount = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
