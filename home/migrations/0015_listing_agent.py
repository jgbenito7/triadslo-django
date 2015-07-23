# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_remove_listing_hitcount'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='agent',
            field=models.ForeignKey(to='home.Agent', null=True),
            preserve_default=True,
        ),
    ]
