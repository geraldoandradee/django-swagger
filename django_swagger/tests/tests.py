#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
import json
import pytest
from django_swagger.validation import validate_presence_of, validate_response_type, validate_range_in, \
    validate_type_of, validate_int
from django_swagger.exception import NotPresentError, InvalidResponseError, ValueNotFoundError, TypeError
from django_swagger.api import Info, Parameter
from django_swagger.response import ResponseMessage
import six

class TestValidators:

    def test_validate_presence_of_valid_string(self):
        validate_presence_of('Thats all cool')

    def test_validate_presence_of_zero(self):
        with pytest.raises(NotPresentError):
            validate_presence_of(0)

    def test_validate_presence_of_false(self):
        assert validate_presence_of('false') == None

    def test_validate_presence_of_true(self):
        assert validate_presence_of('false') == None


    def test_validate_presence_of_false(self):
        with pytest.raises(NotPresentError):
            validate_presence_of(False)

    def test_validate_presence_of_empty_string(self):
        with pytest.raises(NotPresentError):
            validate_presence_of('')

    def test_validate_presence_of_blank_string(self):
        with pytest.raises(NotPresentError):
            validate_presence_of(' ')

    def test_validate_response_type(self):
        with pytest.raises(InvalidResponseError):
            for response in ["text/xml", "", " "]:
                validate_response_type(response)

    def test_validate_range_in(self):
        with pytest.raises(ValueNotFoundError):
            valid_responses = ["application/json", "application/xml", "text/plain", "text/html"]
            validate_range_in('Batatinha', valid_responses)

    def test_validate_range_in(self):
        with pytest.raises(ValueNotFoundError):
            valid_responses = []
            validate_range_in('', valid_responses)

    def test_validate_type_correct(self):
        assert validate_type_of('test', six.text_type) == None
        assert validate_type_of(2, int) == None

    def test_validate_type_incorrect(self):
        with pytest.raises(TypeError):
            validate_type_of('test', dict)

    def test_validate_type_int(self):
        assert validate_int(3) == None

    def test_validate_type_incorrect_int(self):
        with pytest.raises(TypeError):
            validate_int('fds')


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
        assert isinstance(result, six.string_types) == True, "result não é do tipo texto"


class TestParameter:

    def test_correct_validation(self):
        parameter = Parameter(name="name", description="description", param_type="query", required='false',
                              allow_multiple=False)
        parameter.validate()
        assert parameter.has_errors() == False

    def test_validation_of_name(self):
        parameter = Parameter(name="", description="description", param_type="query", required='false',
                              allow_multiple=False)
        parameter.validate()
        assert parameter.has_errors() == True

    def test_validation_optional_description(self):
        parameter = Parameter(name="Name", description="", param_type="query", required='false',
                              allow_multiple=False)
        parameter.validate()
        assert parameter.has_errors() == False

    def test_wrong_validation_of_param_type(self):
        parameter = Parameter(name="Name", description="", param_type="", required='false',
                              allow_multiple=False)
        parameter.validate()
        assert parameter.has_errors() == True

    def test_validation_of_param_type(self):
        parameter = Parameter(name="Name", description="", param_type="asdasdasdasd", required='false',
                              allow_multiple=False)
        parameter.validate()
        assert parameter.has_errors() == True

    def test_wrong_validation_of_required(self):
        parameter = Parameter(name="Name", description="", param_type="path", required='falsee',
                              allow_multiple=False)
        parameter.validate()
        assert parameter.has_errors() == True

    def test_validation_of_required(self):
        parameter = Parameter(name="Name", description="", param_type="path", required='true',
                              allow_multiple=False)
        parameter.validate()
        assert parameter.has_errors() == False

    def test_validation_of_required_true(self):
        parameter = Parameter(name="Name", description="", param_type="path", required='true',
                              allow_multiple=False)
        parameter.validate()
        assert parameter.has_errors() == False

    def test_serialization_return_type(self):
        parameter = Parameter(name="Name", description="", param_type="path", required='true', allow_multiple=False)
        result = parameter.serialize()
        assert isinstance(result, six.string_types) == True

    def test_serialization_structure_return_type(self):
        parameter = Parameter(name="Name", description="", param_type="path", required='true', allow_multiple=False)
        result = json.loads(parameter.serialize())
        assert 'name' in result
        assert 'description' in result
        assert 'param_type' in result
        assert 'required' in result
        assert 'allow_multiple' not in result
        assert isinstance(result, dict) == True


class TestResponseMessage:

    def test_validation_of_response_message(self):
        response = ResponseMessage(code=200, message='OK')
        response.validate()
        assert len(response.errors) == 0

    def test_validation_of_error_response_message(self):
        response = ResponseMessage(code='dsdsd', message='OK')
        response.validate()
        assert len(response.errors) > 0

    def test_validation_of_error_float_code_from_response_message(self):
        response = ResponseMessage(code=200.0, message='OK')
        response.validate()
        assert len(response.errors) > 0

    def test_validation_of_required_fields_of_response_message(self):
        response = ResponseMessage(code=0, message='')
        response.validate()
        assert len(response.errors) > 0

    def test_serialization_response_message(self):
        response = ResponseMessage(code=0, message='')
        response = json.loads(response.serialize())
        assert 'code' in response
        assert 'message' in response

    def test_serialization_response_message_type(self):
        response = ResponseMessage(code=0, message='')
        response = json.loads(response.serialize())
        assert isinstance(response, dict) == True

    def test_serialization_response_message_type_2(self):
        response = ResponseMessage(code=0, message='')
        response = response.serialize()
        assert isinstance(response, six.string_types) == True

    def test_set_default(self):
        response = ResponseMessage(code=0, message='')
        response.set_default()
        assert response.code == 200
        assert response.message == 'OK'

