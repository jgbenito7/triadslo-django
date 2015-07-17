# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('precedence', models.IntegerField()),
                ('first', models.CharField(max_length=100)),
                ('last', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('cell_number', models.CharField(max_length=15)),
                ('bre', models.CharField(max_length=12, db_column='BRE')),
                ('bio', models.TextField()),
                ('picture', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'agents',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BestOfSlo',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('precedence', models.IntegerField()),
                ('title', models.CharField(max_length=255, blank=True)),
                ('description', models.TextField(blank=True)),
                ('image_name', models.CharField(max_length=255, blank=True)),
                ('type', models.CharField(max_length=14)),
            ],
            options={
                'db_table': 'best_of_slo',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Development',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('precedence', models.IntegerField()),
                ('title', models.CharField(max_length=255, blank=True)),
                ('location', models.CharField(max_length=255, blank=True)),
                ('image_name', models.CharField(max_length=255, blank=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'developments',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('precedence', models.IntegerField()),
                ('title', models.CharField(max_length=75)),
                ('info', models.TextField()),
                ('bedrooms', models.CharField(max_length=100)),
                ('bathrooms', models.CharField(max_length=100)),
                ('square_feet', models.CharField(max_length=100)),
                ('acres', models.CharField(max_length=100)),
                ('cost', models.CharField(max_length=100)),
                ('mls', models.CharField(max_length=50, db_column='MLS', blank=True)),
                ('album', models.CharField(max_length=200)),
                ('virtual_tour', models.CharField(max_length=255, blank=True)),
                ('featured', models.CharField(max_length=3)),
                ('published', models.CharField(max_length=3)),
                ('status', models.CharField(max_length=11)),
                ('request_button', models.CharField(max_length=3)),
            ],
            options={
                'db_table': 'listings',
            },
            bases=(models.Model,),
        ),
    ]
