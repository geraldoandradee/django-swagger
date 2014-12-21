#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import (absolute_import, print_function)
from django_swagger import Base
import django_swagger.validation

class BaseResponse(Base):
    _response_types = ["application/json", "application/xml", "text/plain", "text/html"]

    def validate(self):
        """
        validate
        ========

        Validate is a flexible function. Lets
        """
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


class ResponseMessage(BaseResponse):
    """
    ResponseMessage
    ===============

    This is a response message of each Operation. Each operation has one or more ResponseMessage. The range of code
    response is available to check it out in: http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html. But for some
    reasons we use just these: 200, 201, 203, 204, 205, 206, 400, 401, 403, 404, 405, 500.

    """
    __attributes__ = ['code', 'message']
    __validators__ = [{'validate_presence_of': ['code', 'message']}, {'validate_int': ['code']},
                      {'validate_range_in': ['code']}]
    __range__ = {'code': [200, 201, 203, 204, 205, 206, 400, 401, 403, 404, 405, 500]}

    def __init__(self, code, message):
        self.code = code
        self.message = message
        self.errors = []
        super(ResponseMessage, self).__init__(code=code, message=message)

    def set_default(self):
        self.code = 200
        self.message = 'OK'


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

    def produces(self):
        return


class ResponseObject(Response):
    __attrs__=['name', '']

    name = ''