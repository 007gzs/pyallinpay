# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


class AllInPayBaseAPI(object):

    API_BASE_URL = None
    SYB_API_BASE_URL = None

    def __init__(self, client=None):
        self._client = client
        if self.SYB_API_BASE_URL is None and self._client is not None:
            self.SYB_API_BASE_URL = self._client.SYB_API_BASE_URL

    def _get(self, url, params=None, **kwargs):
        if self.API_BASE_URL and 'api_base_url' not in kwargs:
            kwargs['api_base_url'] = self.API_BASE_URL
        return self._client.get(url, params, **kwargs)

    def _post(self, url, data=None, params=None, **kwargs):
        if self.API_BASE_URL and 'api_base_url' not in kwargs:
            kwargs['api_base_url'] = self.API_BASE_URL
        return self._client.post(url, data, params, **kwargs)

    def add_sign(self, data, random_str_key="randomstr", sign_key="sign"):
        return self._client.add_sign(data, random_str_key, sign_key)

    @property
    def cus_id(self):
        return self._client.cus_id

    @property
    def app_id(self):
        return self._client.app_id
