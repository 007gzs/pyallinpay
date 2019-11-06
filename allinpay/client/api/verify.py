# encoding: utf-8
from __future__ import absolute_import, unicode_literals

import datetime

from optionaldict import optionaldict

from .base import AllInPayBaseAPI


class Verify(AllInPayBaseAPI):
    """
    银行账户要素认证
    """
    def _bankverify(self, num, reqsn, cardno, name, idno=None, phone=None, version='11'):
        data = optionaldict({
            "cusid": self.cus_id,
            "appid": self.app_id,
            "version": version,
            "reqtime": datetime.datetime.now().strftime(""),
            "reqsn": reqsn,
            "cardno": cardno,
            "name": name,
            "idno": idno,
            "phone": phone
        })
        self.add_sign(data)
        return self._post("/apiweb/verify/bankverify%d" % num, data, result_processor=lambda x: x['validid'])

    def bankverify2(self, reqsn, cardno, name, version='11'):
        """
        银行账户二要素验证

        :param reqsn: 请求流水
        :param cardno: 银行卡号
        :param name: 户名
        :param version: 版本号
        """
        return self._bankverify(2, reqsn, cardno, name, version=version)

    def bankverify3(self, reqsn, cardno, name, idno, version='11'):
        """
        银行账户三要素验证

        :param reqsn: 请求流水
        :param cardno: 银行卡号
        :param name: 户名
        :param idno: 身份证号
        :param version: 版本号
        """
        return self._bankverify(3, reqsn, cardno, name, idno, version=version)

    def bankverify4(self, reqsn, cardno, name, idno, phone, version='11'):
        """
        银行账户四要素验证

        :param reqsn: 请求流水
        :param cardno: 银行卡号
        :param name: 户名
        :param idno: 身份证号
        :param phone: 手机号码
        :param version: 版本号
        """
        return self._bankverify(4, reqsn, cardno, name, idno, phone, version=version)
