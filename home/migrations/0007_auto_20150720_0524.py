# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20150718_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='picture',
            field=models.ImageField(upload_to='images/agents/', blank=True),
            preserve_default=True,
        ),
    ]
