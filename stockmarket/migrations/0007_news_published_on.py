# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-29 12:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmarket', '0006_remove_news_publish_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='published_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]