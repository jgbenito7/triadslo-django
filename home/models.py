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
from photologue.models import Gallery
from preferences.models import Preferences

YES_OR_NO = (('yes','yes'),('no','no'))
YES_NO_HIDE = (('yes','yes'),('no','no'),('hide','hide'))
BEST_OF = (('Things To Do','Things to Do'),('Places To See','Places To See'),('Wine and Dine','Wine and Dine'))


STATUS = (
    ('active','active'),
    ('pending','pending'),
    ('sold','sold'),
    ('coming_soon','coming_soon')
)

class MyPreferences(Preferences):
    __module__ = 'preferences.models'
    #tagline = models.CharField(max_length=50, blank=True)
    #test = models.EmailField()

class Agent(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    #precedence = models.IntegerField()
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    cell_number = models.CharField(max_length=15)
    bre = models.CharField(db_column='BRE', max_length=12)  # Field name made lowercase.
    bio = models.TextField(blank=True)
    #picture = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    picture = models.ImageField(upload_to="images/agents/",blank=True); #stores in media root
    def __str__(self):
        return self.first + " " + self.last

    class Meta:
        db_table = 'agents'
        ordering = ('order',)

class Development(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    #precedence = models.IntegerField()
    title = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    image_name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        db_table = 'developments'
        ordering = ('order',)

class Listing(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    #precedence = models.IntegerField(default=0)
    title = models.CharField(max_length=75)
    info = models.TextField()
    bedrooms = models.CharField(max_length=100, blank=True)
    bathrooms = models.CharField(max_length=100, blank=True)
    square_feet = models.CharField(max_length=100, blank=True)
    acres = models.CharField(max_length=100, blank=True)
    cost = models.CharField(max_length=100)
    mls = models.CharField(db_column='MLS', max_length=50, blank=True)  # Field name made lowercase.
    latitude = models.FloatField(default=0,blank=True)
    longitude = models.FloatField(default=0,blank=True)
    #album = models.CharField(max_length=200)
    virtual_tour = models.CharField(max_length=255, blank=True)
    featured = models.CharField(max_length=3, choices=YES_OR_NO, default='no')
    published = models.CharField(max_length=3, choices=YES_OR_NO, default='no')
    status = models.CharField(max_length=11, choices=STATUS)
    request_button = models.CharField(max_length=3, choices=YES_OR_NO, default='no')
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    gallery = models.ForeignKey(Gallery,null=True,blank=True)

    garage = models.CharField(max_length=5, choices=YES_NO_HIDE, default='no')
    outdoor_pool = models.CharField(max_length=5, choices=YES_NO_HIDE, default='no')
    garden = models.CharField(max_length=5, choices=YES_NO_HIDE, default='no')
    security_system = models.CharField(max_length=5, choices=YES_NO_HIDE, default='no')
    air_conditioning = models.CharField(max_length=5, choices=YES_NO_HIDE, default='no')
    heating = models.CharField(max_length=5, choices=YES_NO_HIDE, default='no')
    fireplace = models.CharField(max_length=5, choices=YES_NO_HIDE, default='no')
    balcony = models.CharField(max_length=5, choices=YES_NO_HIDE, default='no')
    tv_cable = models.CharField(max_length=5, choices=YES_NO_HIDE, default='no')
    pantry = models.CharField(max_length=5, choices=YES_NO_HIDE, default='no')
    laundy_room = models.CharField(max_length=5, choices=YES_NO_HIDE, default='no')
    elevator = models.CharField(max_length=5, choices=YES_NO_HIDE, default='no')
    skylights = models.CharField(max_length=5, choices=YES_NO_HIDE, default='no')
    cathedral_cielings = models.CharField(max_length=5, choices=YES_NO_HIDE, default='no')
    wet_bar = models.CharField(max_length=5, choices=YES_NO_HIDE, default='no')
    hot_tub = models.CharField(max_length=5, choices=YES_NO_HIDE, default='no')
    patio = models.CharField(max_length=5, choices=YES_NO_HIDE, default='no')
    bbq = models.CharField(max_length=5, choices=YES_NO_HIDE, default='no')
    decks = models.CharField(max_length=5, choices=YES_NO_HIDE, default='no')
    horses_allowed = models.CharField(max_length=5, choices=YES_NO_HIDE, default='no')
    fenced_yard = models.CharField(max_length=5, choices=YES_NO_HIDE, default='no')
    guest_quarters = models.CharField(max_length=5, choices=YES_NO_HIDE, default='no')
    barn = models.CharField(max_length=5, choices=YES_NO_HIDE, default='no')

    def getAlbum(self):
        return self.album;

    class Meta(object):
        db_table = 'listings'
        ordering = ('order',)

class Testimonial(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    agent = models.ForeignKey(Agent,null=True,blank=True)
    testimonial = models.TextField(null=True,blank=True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ('order',)

class BestOfSlo(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    title = models.CharField(max_length=75)
    link = models.CharField(max_length=75, null=True)
    category = models.CharField(max_length=15, choices=BEST_OF, default='no')
    description = models.CharField(max_length=35, null=True)
    latitude = models.FloatField(default=0,blank=True)
    longitude = models.FloatField(default=0,blank=True)
    picture = models.ImageField(upload_to="images/bestofslo/",blank=True); #stores in media root
    class Meta(object):
        ordering = ('order',)
