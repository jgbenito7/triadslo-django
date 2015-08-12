# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_auto_20150811_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='air_conditioning',
            field=models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no'), ('hide', 'hide')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='balcony',
            field=models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no'), ('hide', 'hide')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='barn',
            field=models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no'), ('hide', 'hide')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='bbq',
            field=models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no'), ('hide', 'hide')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='cathedral_cielings',
            field=models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no'), ('hide', 'hide')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='decks',
            field=models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no'), ('hide', 'hide')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='elevator',
            field=models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no'), ('hide', 'hide')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='fenced_yard',
            field=models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no'), ('hide', 'hide')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='fireplace',
            field=models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no'), ('hide', 'hide')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='garage',
            field=models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no'), ('hide', 'hide')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='garden',
            field=models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no'), ('hide', 'hide')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='guest_quarters',
            field=models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no'), ('hide', 'hide')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='heating',
            field=models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no'), ('hide', 'hide')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='horses_allowed',
            field=models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no'), ('hide', 'hide')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='hot_tub',
            field=models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no'), ('hide', 'hide')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='laundy_room',
            field=models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no'), ('hide', 'hide')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='outdoor_pool',
            field=models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no'), ('hide', 'hide')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='pantry',
            field=models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no'), ('hide', 'hide')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='patio',
            field=models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no'), ('hide', 'hide')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='security_system',
            field=models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no'), ('hide', 'hide')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='skylights',
            field=models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no'), ('hide', 'hide')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='tv_cable',
            field=models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no'), ('hide', 'hide')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='wet_bar',
            field=models.CharField(default='no', max_length=3, choices=[('yes', 'yes'), ('no', 'no'), ('hide', 'hide')]),
            preserve_default=True,
        ),
    ]
