from django.db import models


class Transaction(models.Model):
    id = models.CharField(max_length=100)
    appid = models.CharField(max_length=100)
    state = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
