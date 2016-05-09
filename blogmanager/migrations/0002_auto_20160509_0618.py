# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogmanager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Blog Title', blank=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='update_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
