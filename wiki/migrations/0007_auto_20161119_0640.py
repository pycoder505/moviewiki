# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-19 06:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0006_auto_20160917_0645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_songs', to='wiki.Movie'),
        ),
    ]
