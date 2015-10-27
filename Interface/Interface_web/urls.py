#__author__ = 'litongyang'
import django.conf.urls
from .import views as views



urlpatterns = django.conf.urls.patterns('',
                      django.conf.urls.url(r'^$',views.archive),
                      )