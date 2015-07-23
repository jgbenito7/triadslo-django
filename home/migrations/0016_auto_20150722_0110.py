# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_listing_agent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent',
            name='precedence',
        ),
        migrations.RemoveField(
            model_name='bestofslo',
            name='precedence',
        ),
        migrations.RemoveField(
            model_name='development',
            name='precedence',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='precedence',
        ),
    ]
