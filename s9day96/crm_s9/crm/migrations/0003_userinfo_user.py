# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-11-17 07:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0003_auto_20181117_1537'),
        ('crm', '0002_customerdistrbute'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='rbac.User'),
        ),
    ]
