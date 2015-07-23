from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^listings/', views.listings, name='listings'),
    url(r'^single-listing/(?P<listing_id>\d+)/$', views.singleListing, name='singleListing'),
    url(r'^single-agent/(?P<agent_id>\d+)/$', views.singleAgent, name='singleAgent'),
]
