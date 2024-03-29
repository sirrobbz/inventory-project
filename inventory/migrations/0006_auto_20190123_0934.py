# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-01-23 09:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20190123_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='balance',
            field=models.IntegerField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='issued',
            field=models.IntegerField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='received',
            field=models.IntegerField(blank=True, max_length=200, null=True),
        ),
    ]
