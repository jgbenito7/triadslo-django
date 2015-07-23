# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20150717_2018'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agent',
            options={'ordering': ('order',)},
        ),
        migrations.AlterModelOptions(
            name='development',
            options={'ordering': ('order',)},
        ),
        migrations.AlterModelOptions(
            name='listing',
            options={'ordering': ('order',)},
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='my_order',
            new_name='order',
        ),
        migrations.AddField(
            model_name='agent',
            name='order',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='development',
            name='order',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
