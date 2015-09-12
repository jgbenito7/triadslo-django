# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_auto_20150811_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='status',
            field=models.CharField(max_length=11, choices=[('active', 'active'), ('pending', 'pending'), ('sold', 'sold'), ('coming_soon', 'coming_soon')]),
            preserve_default=True,
        ),
    ]
