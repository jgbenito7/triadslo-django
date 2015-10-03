from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from preferences.admin import PreferencesAdmin

# Register your models here.

from .models import Listing
from .models import Agent
from .models import Development
from .models import Testimonial
from .models import BestOfSlo
from home.models import MyPreferences

#admin.site.register(MyPreferences, PreferencesAdmin)

class ListingAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title','cost','featured','status','published')

class AgentAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('first','last','email')

class DevelopmentAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title','location')

class TestimonialAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('agent','testimonial')

class BestOfSloAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title','category')

admin.site.register(Listing,ListingAdmin)
admin.site.register(Agent,AgentAdmin)
admin.site.register(Development,DevelopmentAdmin)
admin.site.register(Testimonial,TestimonialAdmin)
admin.site.register(BestOfSlo,BestOfSloAdmin)
