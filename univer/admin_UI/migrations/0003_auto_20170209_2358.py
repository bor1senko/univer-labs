# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 23:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_UI', '0002_auto_20170209_2357'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(blank=True, default='null', max_length=30)),
                ('faculty', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=255, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='A',
        ),
    ]