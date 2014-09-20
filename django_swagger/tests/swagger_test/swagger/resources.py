#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django_swagger.resources import Api, Endpoint, GroupEndpoint


class MyApi(Api):
    _api_version = '0.0.3'
    _title = 'Django Swagger'
    _description = 'Um teste do django swagger. Aqui pode ter uma descrição muito grande.'
    _terms_of_service_url = 'http://geraldoandrade.com/terms_of_service'
    _contact = 'Geraldo Andrade (geraldo@geraldoandrade.com)'
    _license = ''
    _license_url = 'javascript:;'


class MyGroupEndpoint(GroupEndpoint):
    _api = MyApi
    _path = 'user'
    _description = 'A crud for users.'


class MyGroupEndpoint2(GroupEndpoint):
    _api = MyApi
    _path = 'pets'
    _description = 'A crud for pets.'



class MyEndpoint1(Endpoint):
    group = MyGroupEndpoint

    path = '/user/{id}'
    method = 'GET'
    decription = 'Get user by ID'
    implementation_notes = 'Returns a pet based on ID'

    parameters = [{'name':'id', 'required': True, 'type': 'integer', 'param_type': 'path',
                   'description': 'ID do usuário'},
                  {'name':'id', 'required': True, 'type': 'integer', 'param_type': 'path',
                   'description': 'ID do usuário'}]

    responses = [400, 500, 404]


class MyEndpoint2(Endpoint):
    group = MyGroupEndpoint2


class MyEndpoint3(Endpoint):
    group = MyGroupEndpoint2