# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 06:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0008_auto_20170804_0607'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dvapql',
            old_name='query_json',
            new_name='script',
        ),
    ]
