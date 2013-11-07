#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (unicode_literals)
import os


class Api(object):

    def __init__(self):
        self._api_version = ''
        self._title = 'Django Swagger'
        self._description = ''
        self._terms_of_service_url = ''
        self._contact = ''
        self._license = ''
        self._license_url = 'javascript:;'

    @classmethod
    def serialize(cls):
        template = os.path.join(os.path.dirname(__file__), 'templates', 'django_swagger/root.json')
        file_template = open(template)
        str_template = file_template.read()

        root_json = str_template % {'api_version': cls._api_version, 'all_apis': '', 'title': cls._title,
                                    'description': cls._description,
                                    'terms_of_service_url': cls._terms_of_service_url,
                                    'contact': cls._contact, 'license': cls._license,
                                    'license_url': cls._license_url}
        return eval(root_json)


class GroupEndpoint(object):

    def __init__(self):
        self._path = ''
        self._description = ''
        self._api = None

    @property
    def api(self):
        return self._api

    @api.setter
    def api(self, value):
        self._api = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value

    @classmethod
    def serialize(cls):
        template = os.path.join(os.path.dirname(__file__), 'templates', 'django_swagger/operations.json')
        file_template = open(template)
        str_template = file_template.read()
        root_json = str_template % {'path': cls._path, 'description': cls._description}

        return eval(root_json)


class Endpoint(object):

    def __init__(self):
        self._method = None
        self._summary = None
        self._path = ''




        self._api_version = None
        self._apis = None
        self.base_path = None
        self._models = []
        self._produces = ['application/json'] # only this for now
        self._resource_path = ''
        self._swagger_version = ''

    @classmethod
    def serialize(self):
        pass


class DjangoSwaggerException(Exception):
    pass

def get_api(group):
    return group._api

def get_endpoints(settings):
    splitted_names = settings['namespace'].split('.') # todo: stopped here
    endpoints = []
    try:
        namespace = __import__(settings['namespace'])
        for sn in splitted_names:
            if splitted_names[0] == sn:
                continue
            namespace = getattr(namespace, sn)
    except Exception:
        raise DjangoSwaggerException('DJANGO_SWAGGER variable namespace not configured properly.')

    for endpoint in settings['endpoints']:
        endpoints.append(getattr(namespace, endpoint)())
    return endpoints


def get_group_operations(settings):
    enpoints = get_endpoints(settings)
    groups = []
    for group in enpoints:
        if group.group not in groups:
            groups.append(group.group)
    return groups


def get_operations(settings):
    return ''

def get_endpoint(settings, name):
    endpoints = get_endpoints(settings)

    for ed in endpoints:
        if ed.name == name:
            return ed