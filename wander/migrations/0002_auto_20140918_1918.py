# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wander', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, null=True, blank=True)),
                ('locations', models.ManyToManyField(related_name=b'categories', to='wander.Location')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, null=True, blank=True)),
                ('current_position', geoposition.fields.GeopositionField(max_length=42)),
                ('locations', models.ManyToManyField(related_name=b'user', to='wander.Location')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='category',
            name='user',
            field=models.ForeignKey(related_name=b'categories', to='wander.User'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='location',
            name='zipcode',
            field=models.IntegerField(max_length=10, null=True, blank=True),
        ),
    ]
