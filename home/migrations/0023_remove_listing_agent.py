# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_auto_20150728_2310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='agent',
        ),
    ]
