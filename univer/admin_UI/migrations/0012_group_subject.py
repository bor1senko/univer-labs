# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 21:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_UI', '0011_remove_subject_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='subject',
            field=models.ManyToManyField(to='admin_UI.Subject'),
        ),
    ]
