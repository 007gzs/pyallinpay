# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import logging

from allinpay.core.exceptions import AllInPayClientException
from . import api
from .base import BaseClient
from ..core.utils import AllInPayMd5Signer, AllInPayRsaSigner, AllInPaySm2Signer, random_string, to_text

logger = logging.getLogger(__name__)

SIGNER_CONFIG = {
    "md5": (AllInPayMd5Signer, "signer_key", "signer_key"),
    "rsa": (AllInPayRsaSigner, "signer_key", "PUBLIC_RSA_KEY"),
    "sm2": (AllInPaySm2Signer, "signer_key", "PUBLIC_SM2_KEY"),
}


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
    PUBLIC_RSA_KEY = AllInPayRsaSigner.get_public_key(
        "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCm9OV6zH5DYH/ZnAVYHscEELdCNfNTHGuBv1nYYEY9FrOzE0/4kLl9f7Y9dkWHlc2ocDwb"
        "rFSm0Vqz0q2rJPxXUYBCQl5yW3jzuKSXif7q1yOwkFVtJXvuhf5WRy+1X5FOFoMvS7538No0RpnLzmNi3ktmiqmhpcY/1pmt20FHQQIDAQAB"
    )
    PUBLIC_SM2_KEY = AllInPaySm2Signer.get_public_key(
        "MFkwEwYHKoZIzj0CAQYIKoEcz1UBgi0DQgAEBQicgWm0KAMqhO3bdqMUEDrKQv"
        "Yg8cCXHhdGwq7CGE6oJDzJ1P/94HpuVdBf1KidmPxr7HOH+0DAnpeCcx9TcQ=="
    )

    def __init__(self, app_id, cus_id, signer_key, timeout=None, sign_type="md5", public_key=None):
        sign_type = sign_type.lower()
        assert sign_type in SIGNER_CONFIG
        super(AllInPayClient, self).__init__(timeout)
        self.app_id = app_id
        self.cus_id = cus_id
        self.sign_type = sign_type
        signer_cls = SIGNER_CONFIG[sign_type][0]
        self.signer_key = signer_cls.get_private_key(signer_key)
        if public_key is not None:
            setattr(self, SIGNER_CONFIG[sign_type][2], signer_cls.get_public_key(public_key))

    def get_signer_cls(self, sign_type):
        if sign_type is None:
            sign_type = self.sign_type
        sign_type = sign_type.lower()
        assert sign_type in SIGNER_CONFIG
        signer_cls, private_key, public_key = SIGNER_CONFIG[sign_type]
        private_key = getattr(self, private_key)
        public_key = getattr(self, public_key)
        return signer_cls, private_key, public_key

    def add_sign(self, data, random_str_key="randomstr", sign_key="sign", sign_type=None):
        signer_cls, private_key, public_key = self.get_signer_cls(sign_type)
        if random_str_key and random_str_key not in data:
            data[random_str_key] = random_string()
        signer = signer_cls(delimiter=b'&', key=private_key)
        for k, v in data.items():
            v = to_text(v)
            if v:
                signer.add_data("%s=%s" % (k, v))
        data[sign_key] = signer.signature
        return data

    def check_sign(self, data, sign_key="sign", sign_type=None):
        signer_cls, private_key, public_key = self.get_signer_cls(sign_type)
        sign = ''
        signer = signer_cls(delimiter=b'&', key=public_key)
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
    PUBLIC_RSA_KEY = AllInPayRsaSigner.get_public_key(
        "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDYXfu4b7xgDSmEGQpQ8Sn3RzFgl5CE4gL4TbYrND4FtCYOrvbgLijkdFgIrVVWi2hUW4K0"
        "PwBsmlYhXcbR+JSmqv9zviVXZiym0lK3glJGVCN86r9EPvNTusZZPm40TOEKMVENSYaUjCxZ7JzeZDfQ4WCeQQr2xirqn6LdJjpZ5wIDAQAB"
    )
    PUBLIC_SM2_KEY = AllInPaySm2Signer.get_public_key(
        "MFkwEwYHKoZIzj0CAQYIKoEcz1UBgi0DQgAE/BnA8BawehBtH0ksPyayo4pmzL"
        "/u1FQ2sZcqwOp6bjVqQX4tjo930QAvHZPJ2eez8sCz/RYghcqv4LvMq+kloQ=="
    )
