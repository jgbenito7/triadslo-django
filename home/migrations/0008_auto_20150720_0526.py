# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20150720_0524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='bio',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
