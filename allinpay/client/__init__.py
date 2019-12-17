# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import logging

from allinpay.core.exceptions import AllInPayClientException
from . import api
from .base import BaseClient
from ..core.utils import AllInPayMd5Signer, random_string, to_text


logger = logging.getLogger(__name__)


class AllInPayClient(BaseClient):
    """
    通联支付生产环境
    """
    gateway = api.Gateway()
    posol = api.Posol()
    prescanpay = api.PreScanPay()
    qpay = api.QPay()
    tranx = api.Tranx()
    trxfile = api.Trxfile()
    unitorder = api.UnitOrder()
    verify = api.Verify()

    def __init__(self, app_id, cus_id, signer_key, timeout=None):
        super(AllInPayClient, self).__init__(timeout)
        self.app_id = app_id
        self.cus_id = cus_id
        self.signer_key = "key=%s" % signer_key

    def add_sign(self, data, random_str_key="randomstr", sign_key="sign"):
        if random_str_key and random_str_key not in data:
            data[random_str_key] = random_string()
        signer = AllInPayMd5Signer(delimiter=b'&', key=self.signer_key)
        for k, v in data.items():
            v = to_text(v)
            if v:
                signer.add_data("%s=%s" % (k, v))
        data[sign_key] = signer.signature
        return data

    def check_sign(self, data, sign_key="sign"):
        sign = ''
        signer = AllInPayMd5Signer(delimiter=b'&', key=self.signer_key)
        for k, v in data.items():
            v = to_text(v)
            if k == sign_key:
                sign = v
            elif v:
                signer.add_data("%s=%s" % (k, v))
        if sign.lower() != signer.signature:
            raise AllInPayClientException("SIGNAUTHERR", "签名错误")

    def _handle_pre_request(self, method, uri, kwargs):
        # if 'access_token=' in uri or 'access_token' in kwargs.get('params', {}):
        #     raise ValueError("uri参数中不允许有access_token: " + uri)
        # uri = '%s%saccess_token=%s' % (uri, '&' if '?' in uri else '?', self.access_token)
        return method, uri, kwargs

    def _handle_request_except(self, e, func, *args, **kwargs):
        # if e.errcode in (33001, 40001, 42001, 40014):
        #     self.cache.access_token.delete()
        #     if self.auto_retry:
        #         return func(*args, **kwargs)
        raise e


class AllInPayTestClient(AllInPayClient):
    """
    通联支付测试环境
    """
    API_BASE_URL = 'https://test.allinpaygd.com/'
    SYB_API_BASE_URL = 'https://test.allinpaygd.com/'
