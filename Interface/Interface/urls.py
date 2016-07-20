from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Interface.views.home', name='home'),
    #url(r'^Interface/', include('Interface.urls', namespace="Interface")),
    url(r'^index/', include('Interface_web.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
