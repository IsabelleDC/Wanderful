# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wander', '0002_auto_20140918_1918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='locations',
        ),
        migrations.RemoveField(
            model_name='user',
            name='locations',
        ),
        migrations.AddField(
            model_name='location',
            name='categories',
            field=models.ManyToManyField(related_name=b'locations', to='wander.Category'),
            preserve_default=True,
        ),
    ]
