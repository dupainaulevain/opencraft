# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-24 20:49
from __future__ import unicode_literals

from django.db import migrations
import django_extensions.db.fields.json
import instance.models.openedx_appserver


class Migration(migrations.Migration):

    dependencies = [
        ('instance', '0093_rabbitmq_remove_blank_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openedxappserver',
            name='github_admin_organizations',
            field=django_extensions.db.fields.json.JSONField(blank=True, default=instance.models.openedx_appserver.default_admin_organizations, help_text='A list of GitHub organizations; the members of the "Sandbox" team in these organizations will be given SSH admin access to this instance\'s VMs.', max_length=256),
        ),
        migrations.AlterField(
            model_name='openedxinstance',
            name='github_admin_organizations',
            field=django_extensions.db.fields.json.JSONField(blank=True, default=instance.models.openedx_appserver.default_admin_organizations, help_text='A list of GitHub organizations; the members of the "Sandbox" team in these organizations will be given SSH admin access to this instance\'s VMs.', max_length=256),
        ),
    ]
