# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-25 09:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20160424_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
