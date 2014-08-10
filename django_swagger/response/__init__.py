#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import (absolute_import, print_function)

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

    def __init__(self, *args, **kwargs):
        for argument in kwargs:
            setattr(self, argument, kwargs[argument])


class ResponseObject(Response):
    __attrs__=['name', '']

    name = ''