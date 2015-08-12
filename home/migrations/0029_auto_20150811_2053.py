# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_auto_20150810_2237'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('garage', models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no')])),
                ('outdoor_pool', models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no')])),
                ('garden', models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no')])),
                ('security_system', models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no')])),
                ('air_conditioning', models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no')])),
                ('heating', models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no')])),
                ('fireplace', models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no')])),
                ('balcony', models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no')])),
                ('tv_cable', models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no')])),
                ('pantry', models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no')])),
                ('laundy_room', models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no')])),
                ('elevator', models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no')])),
                ('skylights', models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no')])),
                ('cathedral_cielings', models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no')])),
                ('wet_bar', models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no')])),
                ('hot_tub', models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no')])),
                ('patio', models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no')])),
                ('bbq', models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no')])),
                ('decks', models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no')])),
                ('horses_allowed', models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no')])),
                ('fenced_yard', models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no')])),
                ('guest_quarters', models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no')])),
                ('barn', models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='listing',
            name='amenities',
            field=models.ManyToManyField(to='home.Amenity'),
            preserve_default=True,
        ),
    ]
