# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20150728_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='acres',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='bathrooms',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='bedrooms',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='square_feet',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
