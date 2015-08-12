# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_remove_listing_agent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('testimonial', models.TextField()),
                ('agent', models.ForeignKey(blank=True, to='home.Agent', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
