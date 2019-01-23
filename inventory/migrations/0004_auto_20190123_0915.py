# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-01-23 09:15
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_product_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=20),
        ),
    ]