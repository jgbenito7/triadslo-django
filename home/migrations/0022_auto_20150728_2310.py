# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20150728_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='agent',
            field=models.ForeignKey(blank=True, to='home.Agent', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='gallery',
            field=models.ForeignKey(blank=True, to='photologue.Gallery', null=True),
            preserve_default=True,
        ),
    ]
