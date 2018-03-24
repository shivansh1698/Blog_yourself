# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-01 19:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180201_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 1, 19, 43, 50, 253017, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 1, 19, 43, 50, 252521, tzinfo=utc)),
        ),
    ]
