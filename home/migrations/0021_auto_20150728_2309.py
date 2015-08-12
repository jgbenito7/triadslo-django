# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_auto_20150728_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='agent',
            field=models.ForeignKey(to='home.Agent', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='gallery',
            field=models.ForeignKey(to='photologue.Gallery', null=True),
            preserve_default=True,
        ),
    ]
