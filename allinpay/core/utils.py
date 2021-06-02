# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import base64
import copy
import hashlib
import json
import random
import string

import six


class ObjectDict(dict):
    """Makes a dictionary behave like an object, with attribute-style access.
    """

    def __getattr__(self, key):
        if key in self:
            return self[key]
        return None

    def __setattr__(self, key, value):
        self[key] = value


class AllInPaySigner(object):
    """AllInPay data signer"""

    def __init__(self, delimiter=b'', key=None):
        self._key = key
        self._data = []
        self._delimiter = to_binary(delimiter)

    def add_data(self, *args):
        """Add data to signer"""
        for data in args:
            self._data.append(to_binary(data))

    @property
    def signature(self):
        """Get data signature"""
        raise NotImplementedError

    def verify(self, sign):
        """check sign"""
        return self.signature == sign


class AllInPayMd5Signer(AllInPaySigner):

    @classmethod
    def get_public_key(cls, key):
        return "key=%s" % key

    @classmethod
    def get_private_key(cls, key):
        return "key=%s" % key

    @property
    def signature(self):
        data = copy.copy(self._data)
        if self._key:
            data.append(to_binary(self._key))
        data.sort()
        str_to_sign = self._delimiter.join(data)
        return hashlib.md5(str_to_sign).hexdigest().lower()

    def verify(self, sign):
        return self.signature == sign


class AllInPayRsaSigner(AllInPaySigner):

    @classmethod
    def get_public_key(cls, key):
        from Crypto.PublicKey import RSA
        return RSA.import_key(base64.b64decode(key))

    @classmethod
    def get_private_key(cls, key):
        from Crypto.PublicKey import RSA
        return RSA.import_key(base64.b64decode(key))

    def get_str_to_sign(self):
        data = copy.copy(self._data)
        data.sort()
        return self._delimiter.join(data)

    def get_digest(self):
        from Crypto.Hash import SHA1
        return SHA1.new(self.get_str_to_sign())

    @property
    def signature(self):
        from Crypto.Signature import pkcs1_15
        return to_text(base64.b64encode(pkcs1_15.new(self._key).sign(self.get_digest())))

    def verify(self, sign):
        from Crypto.Signature import pkcs1_15
        try:
            pkcs1_15.new(self._key).verify(self.get_digest(), base64.b64decode(sign))
            return True
        except (ValueError, TypeError):
            return False


class AllInPaySm2Signer(AllInPayRsaSigner):
    @classmethod
    def get_public_key(cls, key):
        return base64.b64decode(key)

    @classmethod
    def get_private_key(cls, key):
        return base64.b64decode(key)

    @property
    def signature(self):
        raise RuntimeError("暂不支持")

    def verify(self, sign):
        raise RuntimeError("暂不支持")


def to_text(value, encoding='utf-8'):
    """Convert value to unicode, default encoding is utf-8

    :param value: Value to be converted
    :param encoding: Desired encoding
    """
    if value is None:
        return ''
    if isinstance(value, six.text_type):
        return value
    if isinstance(value, six.binary_type):
        return value.decode(encoding)
    return six.text_type(value)


def to_binary(value, encoding='utf-8'):
    """Convert value to binary string, default encoding is utf-8

    :param value: Value to be converted
    :param encoding: Desired encoding
    """
    if value is None:
        return b''
    if isinstance(value, six.binary_type):
        return value
    if isinstance(value, six.text_type):
        return value.encode(encoding)
    return to_text(value).encode(encoding)


def random_string(length=16):
    rule = string.ascii_letters + string.digits
    rand_list = random.sample(rule, length)
    return ''.join(rand_list)


def byte2int(c):
    if six.PY2:
        return ord(c)
    return c


def json_loads(s, object_hook=ObjectDict, **kwargs):
    return json.loads(s, object_hook=object_hook, **kwargs)
