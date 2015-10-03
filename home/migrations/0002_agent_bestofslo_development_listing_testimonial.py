# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0008_auto_20150509_1557'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BestOfSlo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('title', models.CharField(max_length=75)),
                ('category', models.CharField(default='no', max_length=15, choices=[('Things To Do', 'Things to Do'), ('Places To See', 'Places To See'), ('Wine and Dine', 'Wine and Dine')])),
            ],
            options={
                'ordering': ('order',),
            },
            bases=(models.Model,),
        )
    ]
