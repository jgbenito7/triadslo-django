# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20150717_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='picture',
            field=models.ImageField(upload_to='mysite/static/home/img/agents/', blank=True),
            preserve_default=True,
        ),
    ]
