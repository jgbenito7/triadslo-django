# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_listing_gallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='featured',
            field=models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no')]),
            preserve_default=True,
        ),
    ]
