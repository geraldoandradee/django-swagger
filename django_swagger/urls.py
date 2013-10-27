#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function)
from django.conf.urls import patterns, url
from .views import Api, Initial, ApiDocs

urlpatterns = patterns('',
                       url(r"^/$", Initial.as_view(), name='django_swagger.docs'),
                       url(r"^/api-docs/$", Api.as_view(), name='django_swagger.all_resources'),
                       url(r"^/api-docs/(?P<resource>.*)$", ApiDocs.as_view(), name='django_swagger.resource'),
)
