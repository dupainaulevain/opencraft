# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='profile', on_delete=django.db.models.deletion.CASCADE)),
            ],
        ),
    ]
