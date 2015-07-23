# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0008_auto_20150509_1557'),
        ('home', '0008_auto_20150720_0526'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='gallery',
            field=models.ForeignKey(to='photologue.Gallery', null=True),
            preserve_default=True,
        ),
    ]
