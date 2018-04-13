# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-21 14:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='description_de',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='board',
            name='description_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='board',
            name='description_pt',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='board',
            name='name_de',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='board',
            name='name_en',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='board',
            name='name_pt',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
    ]
