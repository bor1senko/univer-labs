# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 23:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_UI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='A',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]
