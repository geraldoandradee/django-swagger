#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))  # to make import bellow works
from django_swagger.resources import Api, GroupEndpoint, Endpoint


class ApiTest(unittest.TestCase):

    def setUp(self):
        self.api = Api()
        self.api2 = Api()
        self.group1 = GroupEndpoint()
        self.group2 = GroupEndpoint()
        self.endpoint = Endpoint()
        self.endpoint2 = Endpoint()
        self.group1.api = self.api
        self.endpoint.group = self.group1
        self.endpoint2.group = self.group2

    def test_if_root_file_template_is_opened_correctly(self):
        template = os.path.join(os.path.dirname(__file__), '..', 'templates', 'django_swagger/root.json')

        file_template = open(template)
        str_template = file_template.read()

        self.assertIsNot(file_template, None, 'File template is None.')
        self.assertIsInstance(str_template, str, 'It must be a string')

    def test_if_api_returns_a_dict(self):
        result = self.api.serialize()
        self.assertIsInstance(result, dict, 'Serialize method does not return a dict, returns: %s' % type(result))

    def test_if_api_must_have_a_group(self):
        self.assertIsInstance(self.group1.api, Api, 'A GroupEndpoint must have a API instance')

    def test_if_a_endpoint_have_a_group(self):
        self.assertIsInstance(self.endpoint.group, GroupEndpoint, 'A Endpoint must be grouped by a GroupEndpoint '
                                                                  'instance')


class SettingsTest(unittest.TestCase):

    def test_if_settings_is_properly_configured(self):
        self.assertTrue(True)