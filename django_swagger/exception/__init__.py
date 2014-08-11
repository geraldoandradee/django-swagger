#!/usr/bin/env python
# -*- coding:utf-8 -*-

class NotPresentError(Exception):
    pass

class SerializeError(Exception):
    pass

class InvalidResponseError(Exception):
    pass

class ValueNotFoundError(Exception):
    pass

class TypeError(Exception):
    pass