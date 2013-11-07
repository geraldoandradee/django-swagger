#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function, unicode_literals)
import logging
import json
from django.conf import settings
from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponseForbidden, HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.views.generic import View
from django_swagger.resources import DjangoSwaggerException, get_group_operations, get_endpoint
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
log = logging.getLogger('django')


class Initial(View):
    def get(self, request):
        if not hasattr(settings, 'DJANGO_SWAGGER'):
            raise DjangoSwaggerException('Django Swagger is not properly configured.')
        return render_to_response('django_swagger/index.html')


class Api(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(Api, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        api = None
        for group in get_group_operations(settings.DJANGO_SWAGGER):
            if not api:
                api = group._api.serialize()
            api['apis'].append(group.serialize())

        return HttpResponse(json.dumps(api), content_type='application/json')


class ApiDocs(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ApiDocs, self).dispatch(request, *args, **kwargs)

    def get(self, request, resource):
        endpoint = get_endpoint(settings, resource)

        if endpoint:
            return HttpResponse(json.dumps(endpoint.serialize()), content_type='application/json')
        else:
            return HttpResponse(json.dumps({'error': 'Enpoint does not exists.'}), content_type='application/json')
