# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-27 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='emp_id',
            field=models.IntegerField(default=0),
        ),
    ]