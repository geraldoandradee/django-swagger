from django.conf.urls import patterns, include, url
from django_swagger import urls
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^docs', include(urls)),
)
