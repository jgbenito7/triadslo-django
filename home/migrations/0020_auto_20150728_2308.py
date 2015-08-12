# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20150728_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='agent',
            field=models.ForeignKey(default=None, blank=True, to='home.Agent', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='gallery',
            field=models.ForeignKey(to='photologue.Gallery', blank=True),
            preserve_default=True,
        ),
    ]
