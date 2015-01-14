# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('streetnum', models.IntegerField(null=True, blank=True)),
                ('street', models.CharField(max_length=100, null=True, blank=True)),
                ('city', models.CharField(max_length=100, null=True, blank=True)),
                ('country', models.CharField(max_length=100)),
                ('zipcode', models.IntegerField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
