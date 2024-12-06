from django.contrib import admin

from .models import Transaction


@admin.register(Transaction)
class TransactionModelAdmin(admin.ModelAdmin):
    list_display = ["id", "appid", "state", "created"]

