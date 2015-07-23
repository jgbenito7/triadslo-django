# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20150720_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='published',
            field=models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='request_button',
            field=models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no')]),
            preserve_default=True,
        ),
    ]
