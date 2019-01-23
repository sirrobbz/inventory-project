from django.db import models
from decimal import Decimal


class Product(models.Model):
    date = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    whom = models.CharField(max_length=200, blank=True, null=True)
    requisition = models.CharField(max_length=200, blank=True, null=True, unique=True)
    unit_price = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0.00'))
    description = models.TextField(blank=True, null=True)
    received = models.IntegerField(blank=True, null=True)
    issued = models.IntegerField(blank=True, null=True)
    balance = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return 'Id:{0} Name:{1}'.format(self.id, self.name)
