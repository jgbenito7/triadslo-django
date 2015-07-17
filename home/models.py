# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models
from adminsortable.models import Sortable


class Agent(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    precedence = models.IntegerField()
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    cell_number = models.CharField(max_length=15)
    bre = models.CharField(db_column='BRE', max_length=12)  # Field name made lowercase.
    bio = models.TextField()
    picture = models.CharField(max_length=200)

    class Meta:
        db_table = 'agents'

class BestOfSlo(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    precedence = models.IntegerField()
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    image_name = models.CharField(max_length=255, blank=True)
    type = models.CharField(max_length=14)

    class Meta:
        db_table = 'best_of_slo'


class Development(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    precedence = models.IntegerField()
    title = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    image_name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        db_table = 'developments'



class Listing(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    precedence = models.IntegerField(default=0)
    title = models.CharField(max_length=75)
    info = models.TextField()
    bedrooms = models.CharField(max_length=100)
    bathrooms = models.CharField(max_length=100)
    square_feet = models.CharField(max_length=100)
    acres = models.CharField(max_length=100)
    cost = models.CharField(max_length=100)
    mls = models.CharField(db_column='MLS', max_length=50, blank=True)  # Field name made lowercase.
    album = models.CharField(max_length=200)
    virtual_tour = models.CharField(max_length=255, blank=True)
    featured = models.CharField(max_length=3)
    published = models.CharField(max_length=3)
    status = models.CharField(max_length=11)
    request_button = models.CharField(max_length=3)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)
    class Meta(object):
        db_table = 'listings'
        ordering = ('my_order',)
