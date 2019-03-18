# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-18 10:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('employee_unique_id', models.CharField(max_length=10)),
                ('department', models.CharField(choices=[('employee', 'employee'), ('FINANCE', 'FINANCE'), ('HR', 'HR'), ('MARKETING', 'MARKETING'), ('OPERATIONS', 'OPERATIONS'), ('R%D', 'R%D')], max_length=25)),
                ('contract', models.CharField(max_length=60, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('phone_number', models.PositiveIntegerField(unique=True)),
                ('email', models.EmailField(default='@gmail.com', max_length=60)),
            ],
        ),
    ]
