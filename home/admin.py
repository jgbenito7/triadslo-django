from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

# Register your models here.

from .models import Listing
from .models import Agent
from .models import Development

class ListingAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title','cost','featured','status')

class AgentAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('first','last','email')

class DevelopmentAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title','location')

admin.site.register(Listing,ListingAdmin)
admin.site.register(Agent,AgentAdmin)
admin.site.register(Development,DevelopmentAdmin)
