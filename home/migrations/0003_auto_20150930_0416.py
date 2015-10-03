# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0008_auto_20150509_1557'),
        ('home', '0002_agent_bestofslo_development_listing_testimonial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bestofslo',
            name='latitude',
            field=models.FloatField(default=0, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bestofslo',
            name='longitude',
            field=models.FloatField(default=0, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bestofslo',
            name='picture',
            field=models.ImageField(upload_to='images/bestofslo/', blank=True),
            preserve_default=True,
        ),
    ]
