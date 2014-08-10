#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import pytest
from django_swagger.validation import validate_presence_of, validate_response_type, validate_range_in
from django_swagger.exception import NotPresent, InvalidResponse, ValueNotFound
from django_swagger.api import Info

class TestValidators:

    def test_validate_presence_of_valid_string(self):
        validate_presence_of('Thats all cool')

    def test_validate_presence_of_zero(self):
        with pytest.raises(NotPresent):
            validate_presence_of(0)

    def test_validate_presence_of_false(self):
        with pytest.raises(NotPresent):
            validate_presence_of(False)

    def test_validate_presence_of_empty_string(self):
        with pytest.raises(NotPresent):
            validate_presence_of('')

    def test_validate_presence_of_blank_string(self):
        with pytest.raises(NotPresent):
            validate_presence_of(' ')

    def test_validate_response_type(self):
        with pytest.raises(InvalidResponse):
            for response in ["text/xml", "", " "]:
                validate_response_type(response)

    def test_validate_range_in(self):
        with pytest.raises(ValueNotFound):
            valid_responses = ["application/json", "application/xml", "text/plain", "text/html"]
            validate_range_in('Batatinha', valid_responses)

    def test_validate_range_in(self):
        with pytest.raises(ValueNotFound):
            valid_responses = []
            validate_range_in('', valid_responses)


class TestInfo:

    def test_validation(self):
        info = Info(title=' ', description='', terms_of_service_url='', contact='', license='', license_url='')
        info.validate()
        assert info.has_errors() == True

    def test_validation_correct2(self):
        info2 = Info(title='API Title', description='Some description', terms_of_service_url='', contact='', license='', license_url='')
        info2.validate()
        assert info2.has_errors() == False

    def test_serialize(self):
        info2 = Info(title='API Title', description='Some description', terms_of_service_url='', contact='', license='', license_url='')
        result = info2.serialize()
        assert isinstance(result, str) == True

