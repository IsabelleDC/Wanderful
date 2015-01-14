# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wander', '0004_auto_20140918_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='image',
            field=models.ImageField(null=True, upload_to=b'location_image', blank=True),
            preserve_default=True,
        ),
    ]
