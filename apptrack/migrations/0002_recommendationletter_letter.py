# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-17 04:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptrack', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendationletter',
            name='letter',
            field=models.TextField(default='yay'),
            preserve_default=False,
        ),
    ]
