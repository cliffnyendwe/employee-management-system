# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-17 08:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0009_auto_20190316_1824'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employees',
            old_name='job',
            new_name='contract',
        ),
    ]