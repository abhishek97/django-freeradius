# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-26 21:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_freeradius', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='radiusaccounting',
            name='acct_update_time',
            field=models.DateTimeField(db_column='acctupdatetime', db_index=True, null=True, verbose_name='acct update time'),
        ),
    ]
