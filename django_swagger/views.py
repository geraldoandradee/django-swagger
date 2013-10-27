#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function, unicode_literals)
import logging
import json
from django.conf import settings
from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponseForbidden, HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.views.generic import View
from django_swagger.resources import DjangoSwaggerException, get_group_operations, get_operations
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
        return HttpResponse(json.dumps(eval('{"apiVersion":"1.0.0",'
                                            '"swaggerVersion":"1.2",'
                                            '"basePath":"http://127.0.0.1:8000/docs/api-docs/",'
                                            '"resourcePath":"/user",'
                                            '"apis":[{'
                                            '"path":"/user/{username}",'
                                            '"operations":[{"method":"GET",'
                                            '"summary":"Get user by user name",'
                                            '"notes":"","type":"User",'
                                            '"nickname":"getUserByName",'
                                            '"parameters":[{"name":"username",'
                                            '"description":"The name that needs to be fetched. Use user1 for testing.",'
                                            '"required":True,"type":"string","paramType":"path"}],}]},'
                                            '{"path":"/user/login",'
                                            '"operations":[{"method":"GET",'
                                            '"summary":"Logs user into the system","notes":"","type":"string",'
                                            '"nickname":"loginUser","parameters":[{"name":"username",'
                                            '"description":"The user name for login","required":True,'
                                            '"type":"string","paramType":"query"},{"name":"password",'
                                            '"description":"The password for login in clear text",'
                                            '"required":True,"type":"string","paramType":"query"}],'
                                            '"responseMessages":[{"code":400,'
                                            '"message":"Invalid username and password combination"}]}]},'
                                            '{"path":"/user/logout",'
                                            '"operations":[{"method":"GET",'
                                            '"summary":"Logs out current logged in user session","notes":"",'
                                            '"type":"void","nickname":"logoutUser","parameters":[]}]}],'
                                            '"models":{"User":{"id":"User","properties":{"id":{"type":"integer",'
                                            '"format":"int64","description":"Unique identifier for the user"},'
                                            '"username":{"type":"string","description":"Unique username"},'
                                            '"firstName":{"type":"string","description":"First name of the user"},'
                                            '"lastName":{"type":"string","description":"Last name of the user"},'
                                            '"email":{"type":"string","description":"Email address of the user"},'
                                            '"password":{"type":"string","description":"Password name of the user"},'
                                            '"phone":{"type":"string","description":"Phone number of the user"},'
                                            '"userStatus":{"type":"integer","format":"int32","description":'
                                            '"User Status","enum":["1-registered","2-active","3-closed"]}}}}}')), content_type='application/json')