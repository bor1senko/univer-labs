# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_UI', '0006_auto_20170221_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
