#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (absolute_import, unicode_literals, print_function)
import django_swagger

class BaseApi(django_swagger.Base):
    def validate(self):
        if len(self.__validators__):
            for validate in self.__validators__:
                for function_to_validate in validate.keys():
                    for to_validate in validate[function_to_validate]:
                        try:
                            value_to_validate = getattr(self, to_validate)

                            if function_to_validate == 'validate_range_in':
                                getattr(django_swagger.validation, function_to_validate)(value_to_validate,
                                                                                         self.__range__[to_validate])
                            else:
                                getattr(django_swagger.validation, function_to_validate)(value_to_validate)
                        except Exception as e:
                            self.errors.append({to_validate: e})


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
        self.title = title
        self.description = description
        self.terms_of_service_url = terms_of_service_url
        self.contact = contact
        self.license = license
        self.license_url = license_url
        self.errors = []
        super(Info, self).__init__(title, description, terms_of_service_url, contact, license, license_url)


class Parameter(BaseApi):
    """
    Parameter
    =========

    This class is represents Api object specified in
    https://github.com/wordnik/swagger-spec/blob/master/versions/1.2.md#524-parameter-object

    .. code-block:: json

        {
          "name": "body",
          "description": "Pet object that needs to be updated in the store",
          "required": true,
          "type": "Pet",
          "paramType": "body"
        }

    """
    __range__ = {'param_type': ["path", "query", "body", "header", "form"], 'required' : ['true', 'false']}
    __attributes__ = ['name', 'description', 'required', 'param_type']
    __validators__ = [{'validate_range_in': ['param_type', 'required']}, {'validate_presence_of': ['param_type', 'name',
                                                                                                   'required']}]

    def __init__(self, name, description, param_type, required, allow_multiple=False):
        self.name = name
        self.description = description
        self.param_type = param_type
        self.required = required
        self.allow_multiple = allow_multiple
        self.errors = []


class Operation(BaseApi):
    """
    Operation
    =========

    This class is represents Api object specified in
    https://github.com/wordnik/swagger-spec/blob/master/versions/1.2.md#523-operation-object

    .. code-block:: json

        {
          "method": "GET",
          "summary": "Find pet by ID",
          "notes": "Returns a pet based on ID",
          "type": "Pet",
          "nickname": "getPetById",
          "authorizations": {},
          "parameters": [
            {
              "name": "petId",
              "description": "ID of pet that needs to be fetched",
              "required": true,
              "type": "integer",
              "format": "int64",
              "paramType": "path",
              "minimum": "1.0",
              "maximum": "100000.0"
            }
          ],
          "responseMessages": [
            {
              "code": 400,
              "message": "Invalid ID supplied"
            },
            {
              "code": 404,
              "message": "Pet not found"
            }
          ]
        }
    """

    __attributes__ = ['method', 'summary', 'notes', 'nickname', 'authorizations', 'parameters', 'responseMessages',
                      'produces', 'consumes', 'deprecated']


class Api(BaseApi):
    """
    Api
    ===

    This class is represents Api object specified in
    https://github.com/wordnik/swagger-spec/blob/master/versions/1.2.md#522-api-object.

    .. code-block:: json

        {
          "path": "/pet",
          "operations": [
            {
              "method": "PUT",
              "summary": "Update an existing pet",
              "notes": "",
              "type": "void",
              "nickname": "updatePet",
              "authorizations": {},
              "parameters": [
                {
                  "name": "body",
                  "description": "Pet object that needs to be updated in the store",
                  "required": true,
                  "type": "Pet",
                  "paramType": "body"
                }
              ],
              "responseMessages": [
                {
                  "code": 400,
                  "message": "Invalid ID supplied"
                },
                {
                  "code": 404,
                  "message": "Pet not found"
                },
                {
                  "code": 405,
                  "message": "Validation exception"
                }
              ]
            },
            {
              "method": "POST",
              "summary": "Add a new pet to the store",
              "notes": "",
              "type": "void",
              "nickname": "addPet",
              "consumes": [
                "application/json",
                "application/xml"
              ],
              "authorizations": {
                "oauth2": [
                  {
                    "scope": "test:anything",
                    "description": "anything"
                  }
                ]
              },
              "parameters": [
                {
                  "name": "body",
                  "description": "Pet object that needs to be added to the store",
                  "required": true,
                  "type": "Pet",
                  "paramType": "body"
                }
              ],
              "responseMessages": [
                {
                  "code": 405,
                  "message": "Invalid input"
                }
              ]
            }
          ]
        }

    """
    __attributes__ = ['path', 'description', 'operations']
    __validators__ = [{'validate_presence_of': ['path', 'operations']}]
    path = ''
    description = ''
    operations = []

    def __init__(self, path, operations, description=''):
        """
        __init__
        ========

        Constructor of Api endpoint.

        :param path: relative path to base.
        :param operations: a list of operations.
        :param description: optional, describes what this endpoint will do.
        """
        self.path = path
        self.errors = []
        super(Api, self).__init__(path, operations, description)


class ResourceList(BaseApi):
    """
    ResourceList
    ============

    This object is described in https://github.com/wordnik/swagger-spec/blob/master/versions/1.2.md#51-resource-listing.
    Basically this endpoint

    """
    __attributes__ = ['swaggerVersion', 'apis', 'apiVersion', 'info', 'authorizations']
    __validators__ = [{'validate_presence_of': ['path', 'operations']}, {'validate_type_of_list': ['apis']}]

    def __init__(self, apis, api_version, info):
        """
        __init__
        ========

        Constructor of Api endpoint.

        :param apis:
        :param api_version:
        :param info:
        """
        self.swaggerVersion = '1.2'
        self.apis = apis
        self.api_version = api_version
        self.info = info
        self.authorizations = {}
        self.errors = []
        super(ResourceList, self).__init__(apis, api_version, info)


class ApiDoc(BaseApi):
    __attributes__ = ['api_version', 'swagger_version', 'apis', 'authorizations', 'info']
    __validators__ = [{'validate_presence_of': ['api_version', 'apis', 'info']}]

    def __init__(self, api_version, apis, info, *args, **kwargs):
        self.api_version = api_version
        self.swagger_version = '1.2'
        self.apis = apis
        authorizations = {}
        self.info = info
        super(ApiDoc, self).__init__(*args, **kwargs)