# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0008_auto_20150509_1557'),
        ('home', '0004_auto_20150930_2338'),
    ]

    operations = [
        
        migrations.AddField(
            model_name='bestofslo',
            name='link',
            field=models.CharField(max_length=75, null=True),
            preserve_default=True,
        ),
    ]
