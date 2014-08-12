#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import (unicode_literals, print_function)
from django_swagger.exception import NotPresentError, InvalidResponseError, ValueNotFoundError, TypeError
import six

def validate_presence_of(value):
    if not value:
        raise NotPresentError('Provided value [%s] is not present' % value)

    if isinstance(value, six.text_type) and not value.strip():
        raise NotPresentError('Provided value is blank')

    if not len(value):
        raise NotPresentError('Provided list or array is empty. It must have one item.')


def validate_response_type(response):
    valid_responses = ["application/json", "application/xml", "text/plain", "text/html"]
    try:
        validate_range_in(response, valid_responses)
    except ValueNotFoundError:
        raise InvalidResponseError('This response is not valid. Choose a valid response: %s' % valid_responses)


def validate_range_in(value, range):
    if value not in range:
        raise ValueNotFoundError('Value %s was not found in %s.' % (value, range))


def validate_type_of(value, type_var):
    if not isinstance(value, type_var):
        raise TypeError('Type of %s is not a %s. %s has type %s.' % (value, type_var, value, type(value)))


def validate_int(value):
    validate_type_of(value, int)


def validate_type_of_list(value):
    validate_type_of(value, list)
