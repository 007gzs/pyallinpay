# encoding: utf-8
from __future__ import absolute_import, unicode_literals

from optionaldict import optionaldict

from .base import AllInPayBaseAPI


class PreScanPay(AllInPayBaseAPI):
    """
    网上收银预消费
    """
    def pay(self, reqsn, trxamt, paytype, body=None, validtime=5,
            authcode=None, acct=None, notify_url=None, limit_pay=None,
            sub_appid=None, subbranch=None, cusip=None, version='12', remark=None):
        """
        网上收银预消费 - 扫码预消费
        https://aipboss.allinpay.com/know/devhelp/home.php?id=362

        :param reqsn: 商户交易单号
        :param trxamt: 交易金额
        :param paytype: 交易方式
        :param body: 订单标题
        :param validtime: 有效时间
        :param authcode: 支付授权码
        :param acct: 支付平台用户标识
        :param notify_url: 交易结果通知地址
        :param limit_pay: 支付限制
        :param sub_appid: 微信子appid
        :param subbranch: 门店号
        :param cusip: 终端ip
        :param version: 版本号
        :param remark: 备注
        """
        data = optionaldict({
            "cusid": self.cus_id,
            "appid": self.app_id,
            "reqsn": reqsn,
            "trxamt": trxamt,
            "paytype": paytype,
            "body": body,
            "validtime": validtime,
            "authcode": authcode,
            "acct": acct,
            "notify_url": notify_url,
            "limit_pay": limit_pay,
            "sub_appid": sub_appid,
            "subbranch": subbranch,
            "cusip": cusip,
            "version": version,
            "remark": remark
        })
        self.add_sign(data)
        return self._post('/apiweb/prescanpay/pay', data)

    def finish(self, reqsn, trxamt, oldtrxid, asinfo=None, version='12'):
        """
        网上收银预消费 - 扫码预消费完成
        https://aipboss.allinpay.com/know/devhelp/home.php?id=363

        :param reqsn: 商户完成交易单号
        :param trxamt: 交易金额
        :param oldtrxid: 预消费交易流水
        :param asinfo: 分账信息
        :param version: 版本号
        """
        data = optionaldict({
            "cusid": self.cus_id,
            "appid": self.app_id,
            "reqsn": reqsn,
            "trxamt": trxamt,
            "oldtrxid": oldtrxid,
            "asinfo": asinfo,
            "version": version
        })
        self.add_sign(data)
        return self._post('/apiweb/prescanpay/finish', data)

    def cancel(self, reqsn, trxamt, oldtrxid, version='12'):
        """
        网上收银预消费 - 扫码预消费交易回退
        https://aipboss.allinpay.com/know/devhelp/home.php?id=364

        :param reqsn: 商户撤销交易单号
        :param trxamt: 交易金额
        :param oldtrxid: 预消费交易流水
        :param version: 版本号
        """
        data = optionaldict({
            "cusid": self.cus_id,
            "appid": self.app_id,
            "reqsn": reqsn,
            "trxamt": trxamt,
            "oldtrxid": oldtrxid,
            "version": version
        })
        self.add_sign(data)
        return self._post('/apiweb/prescanpay/cancel', data)

    def refund(self, reqsn, trxamt, oldtrxid,  version='12', remark=None):
        """
        网上收银预消费 - 扫码预消费完成交易退款
        https://aipboss.allinpay.com/know/devhelp/home.php?id=365
        """
        data = optionaldict({
            "cusid": self.cus_id,
            "appid": self.app_id,
            "reqsn": reqsn,
            "trxamt": trxamt,
            "oldtrxid": oldtrxid,
            "version": version,
            "remark": remark
        })
        self.add_sign(data)
        return self._post('/apiweb/prescanpay/refund', data)

    def query(self, reqsn=None, trxid=None, version="12"):
        """
        网上收银预消费 - 扫码预消费查询
        https://aipboss.allinpay.com/know/devhelp/home.php?id=366

        :param reqsn: 商户预消费订单号
        :param trxid: 平台预消费交易流水
        :param version: 版本号
        """
        if not reqsn and not trxid:
            raise ValueError("reqsn和trxid必填其一")
        data = optionaldict({
            "cusid": self.cus_id,
            "appid": self.app_id,
            "reqsn": reqsn,
            "trxid": trxid,
            "version": version
        })
        self.add_sign(data)
        return self._post('/apiweb/prescanpay/query', data)
