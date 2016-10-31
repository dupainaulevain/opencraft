# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-28 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instance', '0060_mark_successful_instances'),
    ]

    operations = [
        migrations.AddField(
            model_name='openedxappserver',
            name='configuration_secret_keys',
            field=models.TextField(blank=True, help_text='YAML vars for secret keys'),
        ),
        migrations.AddField(
            model_name='openedxinstance',
            name='secret_key_b64encoded',
            field=models.CharField(blank=True, help_text='This field holds a base-64-encoded secret key that is generated when the instance is created, and is used to generate secret keys for individual services on each appserver.', max_length=48, verbose_name='Instance-specific base-64-encoded secret key'),
        ),
    ]
