# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-10-18 00:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('easyaudit', '0011_auto_20181101_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crudevent',
            name='user',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='crudevent',
            name='content_type',
            field=models.ForeignKey(to='contenttypes.ContentType', db_constraint=False, on_delete=models.CASCADE),
        ),
        migrations.AlterField(
            model_name='loginevent',
            name='user',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True,
                                    on_delete=django.db.models.deletion.SET_NULL,
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='requestevent',
            name='user',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True,
                                    on_delete=django.db.models.deletion.SET_NULL,
                                    to=settings.AUTH_USER_MODEL),
        ),

    ]
