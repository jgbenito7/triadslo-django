# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0008_auto_20150509_1557'),
        ('home', '0003_auto_20150930_0416'),
    ]

    operations = [
        migrations.AddField(
            model_name='bestofslo',
            name='description',
            field=models.CharField(max_length=35, null=True),
            preserve_default=True,
        ),
    ]
