from django.db import models


class Transaction(models.Model):
    address_from = models.CharField(max_length=65)
    address_to = models.CharField(max_length=65)
    amount = models.CharField(max_length=20)
    transaction_hash = models.CharField(max_length=65, null=True)