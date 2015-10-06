# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0008_auto_20150509_1557'),
        ('home', '0005_auto_20151003_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bestofslo',
            name='category',
            field=models.CharField(default='no', max_length=15, choices=[('Things To Do', 'Things to Do'), ('Places To Stay', 'Places To Stay'), ('Wine and Dine', 'Wine and Dine')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bestofslo',
            name='link',
            field=models.CharField(max_length=75, null=True, blank=True),
            preserve_default=True,
        ),
    ]
