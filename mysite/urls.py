from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': 'home/media', 'show_indexes': True}),
    url(r'', include('home.urls')),
    #url(r'^single-listing/', include('home.urls')),
)
