# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-05 21:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pr_watch', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchedpullrequest',
            name='branch_name',
            field=models.CharField(default='master', max_length=255),
        ),
    ]
