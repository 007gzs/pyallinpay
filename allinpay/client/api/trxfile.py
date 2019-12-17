# encoding: utf-8
from __future__ import absolute_import, unicode_literals

import datetime

from optionaldict import optionaldict

from .base import AllInPayBaseAPI


class Trxfile(AllInPayBaseAPI):
    """
    对账文件下载接口
    """

    def get(self, date):
        """
        获取对账单接口
        https://aipboss.allinpay.com/know/devhelp/home.php?id=109

        :param date: 交易日期
        """
        if isinstance(date, datetime.date):
            date = date.strftime("%Y%m%d")
        data = optionaldict({
            "cusid": self.cus_id,
            "appid": self.app_id,
            "date": date
        })
        self.add_sign(data)
        return self._post("/apiweb/trxfile/get", data, result_processor=lambda x: x['url'])

    def setttrx(self, settdate):
        """
        获取结算单接口
        https://aipboss.allinpay.com/know/devhelp/home.php?id=422

        :param settdate: 结算日期
        """
        if isinstance(settdate, datetime.date):
            settdate = settdate.strftime("%Y%m%d")
        data = optionaldict({
            "cusid": self.cus_id,
            "appid": self.app_id,
            "settdate": settdate
        })
        self.add_sign(data)
        return self._post("/trxfile/setttrx", data, result_processor=lambda x: x['trxlist'])
