# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20150717_0621'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='listing',
            options={'ordering': ('precedence',)},
        ),
        migrations.RemoveField(
            model_name='listing',
            name='order',
        ),
        migrations.AlterField(
            model_name='listing',
            name='precedence',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
