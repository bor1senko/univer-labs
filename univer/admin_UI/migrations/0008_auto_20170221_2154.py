# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 21:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_UI', '0007_auto_20170221_2106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='faculty',
        ),
        migrations.AddField(
            model_name='student',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='admin_UI.Group'),
            preserve_default=False,
        ),
    ]