# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_auto_20150810_2235'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testimonial',
            options={'ordering': ('order',)},
        ),
        migrations.AddField(
            model_name='testimonial',
            name='order',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
