# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-26 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignmentapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='updated_by',
        ),
        migrations.AlterField(
            model_name='comment',
            name='message',
            field=models.TextField(max_length=4000),
        ),
    ]
