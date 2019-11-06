# encoding: utf-8
from __future__ import absolute_import, unicode_literals

from optionaldict import optionaldict

from .base import AllInPayBaseAPI


class Posol(AllInPayBaseAPI):
    """
    协同收银
    """

    def authfin(self, reqsn, trxid, trxamt, orgid=None, version='11'):
        """
        预授权完成

        :param reqsn: 商户预授权完成交易流水号
        :param trxid: 交易单号
        :param trxamt: 交易金额
        :param orgid: 集团商户号
        :param version: 版本号
        """
        data = optionaldict({
            "cusid": self.cus_id,
            "appid": self.app_id,
            "orgid": orgid,
            "reqsn": reqsn,
            "trxid": trxid,
            "trxamt": trxamt,
            "version": version
        })
        self.add_sign(data)
        return self._post("/apiweb/posol/authfin", data)

    def refund(self, reqsn, trxid, trxamt, orgid=None, version='11', remark=None):
        """
        交易退货

        :param reqsn: 商户退货交易流水号
        :param trxid: 交易单号
        :param trxamt: 退款金额
        :param orgid: 集团商户号
        :param version: 版本号
        :param remark: 交易备注
        """
        data = optionaldict({
            "cusid": self.cus_id,
            "appid": self.app_id,
            "orgid": orgid,
            "reqsn": reqsn,
            "trxid": trxid,
            "trxamt": trxamt,
            "version": version,
            "remark": remark
        })
        self.add_sign(data)
        return self._post("/apiweb/posol/refund", data)

    def cancel(self, reqsn, trxid, trxamt, orgid=None, version='11'):
        """
        交易撤销

        :param reqsn: 商户撤销交易流水号
        :param trxid: 交易单号
        :param trxamt: 撤销金额
        :param orgid: 集团商户号
        :param version: 版本号
        """
        data = optionaldict({
            "cusid": self.cus_id,
            "appid": self.app_id,
            "orgid": orgid,
            "reqsn": reqsn,
            "trxid": trxid,
            "trxamt": trxamt,
            "version": version
        })
        self.add_sign(data)
        return self._post("/apiweb/posol/cancel", data)

    def query(self, reqsn=None, trxid=None, orgid=None, version='11', remark=None):
        """
        交易查询

        :param orgid: 集团商户号
        :param reqsn: 订单号
        :param trxid: 收银宝交易流水
        :param version: 版本号
        :param remark: 交易备注
        """
        if not reqsn and not trxid:
            raise ValueError("reqsn和trxid不能同时为空")
        data = optionaldict({
            "cusid": self.cus_id,
            "appid": self.app_id,
            "orgid": orgid,
            "reqsn": reqsn,
            "trxid": trxid,
            "version": version,
            "remark": remark
        })
        self.add_sign(data)
        return self._post("/apiweb/posol/query", data)
