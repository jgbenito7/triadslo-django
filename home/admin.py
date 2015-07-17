from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

# Register your models here.

from .models import Listing




class ListingAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title',)




admin.site.register(Listing,ListingAdmin)
