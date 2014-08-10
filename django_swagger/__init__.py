#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (print_function, absolute_import, unicode_literals)
from django_swagger.exception import SerializeError
import django_swagger.validation
import json

class Base(object):
    errors = []
    __validators__ = []
    __attributes__ = []

    def has_errors(self):
        if len(self.errors) > 0:
            return True
        else:
            return False

    def validate(self):
        if len(self.__validators__):
            for validate in self.__validators__:
                for function_to_validate in validate.keys():
                    for to_validate in validate[function_to_validate]:
                        try:
                            value_to_validate = getattr(self, to_validate)
                            getattr(django_swagger.validation, function_to_validate)(value_to_validate)
                        except Exception as e:
                            self.errors.append({to_validate: e})


    def serialize(self):
        obj = {}
        if len(self.__attributes__):
            for attr in self.__attributes__:
                obj[attr] = getattr(self, attr)
        else:
            raise SerializeError('Class must declare __attributes__ to serialize class')
        return json.dumps(obj)

    def __init__(self, *args, **kwargs):
        for argument in kwargs:
            setattr(self, argument, kwargs[argument])