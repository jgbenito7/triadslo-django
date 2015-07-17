# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20150717_2015'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='listing',
            options={'ordering': ('my_order',)},
        ),
        migrations.AddField(
            model_name='listing',
            name='my_order',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
