# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_auto_20150810_2227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonial',
            name='agent',
        ),
        migrations.RemoveField(
            model_name='testimonial',
            name='testimonial',
        ),
    ]
