# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-18 06:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('group', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='groupmember',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_member', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='group',
            name='group_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
