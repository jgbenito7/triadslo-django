# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_remove_listing_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='latitude',
            field=models.FloatField(default=0, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='listing',
            name='longitude',
            field=models.FloatField(default=0, blank=True),
            preserve_default=True,
        ),
    ]
