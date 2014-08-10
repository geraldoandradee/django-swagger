#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (absolute_import, unicode_literals, print_function)
import json
from django_swagger import Base

class BaseApi(Base):
    pass


class Info(BaseApi):
    """
    Info
    ====

    This class is represents Info object specified in
    https://github.com/wordnik/swagger-spec/blob/master/versions/1.2.md#513-info-object.

    .. code-block:: json

        {
          "title": "Swagger Sample App",
          "description": "This is a sample server Petstore server.",
          "termsOfServiceUrl": "http://helloreverb.com/terms/",
          "contact": "apiteam@wordnik.com",
          "license": "Apache 2.0",
          "licenseUrl": "http://www.apache.org/licenses/LICENSE-2.0.html"
        }

    """
    __attributes__ = ['title', 'description', 'terms_of_service_url', 'contact', 'license', 'license_url']
    __validators__ = [{'validate_presence_of': ['title', 'description']}]

    def __init__(self, title, description, terms_of_service_url=None, contact=None, license=None, license_url=None):
        self.title=title
        self.description=description
        self.terms_of_service_url=terms_of_service_url
        self.contact=contact
        self.license=license
        self.license_url=license_url
        self.errors = []
        super(Info, self).__init__(title, description, terms_of_service_url, contact, license, license_url)

