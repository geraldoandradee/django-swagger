#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django_swagger.exception import NotPresent, InvalidResponse, ValueNotFound


def validate_presence_of(value):
    if not value:
        raise NotPresent('Provided value [%s] is not present' % value)

    if isinstance(value, str) and not value.strip():
        raise NotPresent('Provided value is blank')


def validate_response_type(response):
    valid_responses = ["application/json", "application/xml", "text/plain", "text/html"]
    try:
        validate_range_in(response, valid_responses)
    except ValueNotFound:
        raise InvalidResponse('This response is not valid. Choose a valid response: %s' % valid_responses)


def validate_range_in(value, range):
    if value not in range:
        raise ValueNotFound('Value %s was not found in %s.' % (value, range))