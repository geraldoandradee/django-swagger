#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import (absolute_import, print_function)
from django_swagger import Base

class BaseResponse(Base):
    _response_types = ["application/json", "application/xml", "text/plain", "text/html"]


class Response(BaseResponse):
    __attributes__ = ['response_type']
    __validators__ = [{'validate_range_in': ['response_type']}]
    _response_type = None

    @property
    def default_response_type(self):
        """
        default_response_type
        ---------------------

        Json is default return type.

        :rtype : str
        """
        return self._response_types[0]

    @property
    def response_type(self, value):
        return self._response_type

    @response_type.setter
    def response_type(self, value):
        self._response_type = value


class ResponseObject(Response):
    __attrs__=['name', '']

    name = ''