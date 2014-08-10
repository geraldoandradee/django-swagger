#!/usr/bin/env python
# -*- coding: utf-8 -*-
from inspect import classify_class_attrs


class BaseDoc(object):
    def _validate(self):
        pass


class Doc(BaseDoc):

    __attrs__ = ['api_version', 'title', 'description', 'terms_of_service_url', 'contact', 'license', 'license_url']

    swaggerVersion = "1.2"

    api_version = ''
    title = ''
    description = ''
    terms_of_service_url = ''
    contact = ''
    license = ''
    license_url = ''



class Response(object):
    response_types = ["application/json", "application/xml", "text/plain", "text/html"]

    @property
    def default_response_type(self):
        """
        default_response_type
        ---------------------

        Json is default return type.

        :rtype : str
        """
        return self.response_types[0]


class Endpoint(BaseDoc):
    doc = ''
    base_path = ''

    response = ''