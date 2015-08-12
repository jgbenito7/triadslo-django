# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_auto_20150810_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='agent',
            field=models.ForeignKey(blank=True, to='home.Agent', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testimonial',
            name='testimonial',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
