# encoding: utf-8
from __future__ import absolute_import, unicode_literals

from six.moves.urllib import parse
from optionaldict import optionaldict

from .base import AllInPayBaseAPI


class Tranx(AllInPayBaseAPI):
    """
    终端订单支付, 当面付订单支付
    """

    def queryorder(self, trxdate=None, orderid=None, trxid=None, termno=None, resendnotify=False):
        """
        终端订单支付-订单交易结果查询
        https://aipboss.allinpay.com/know/devhelp/home.php?id=100
        当面付订单支付-交易查询
        https://aipboss.allinpay.com/know/devhelp/home.php?id=207

        :param trxdate: 交易日期
        :param orderid: 订单号
        :param trxid: 收银宝交易流水
        :param termno: 终端号
        :param resendnotify: 是否重发交易结果通知
        """
        if not orderid and not trxid:
            raise ValueError("orderid和trxid不能同时为空")
        data = optionaldict({
            "cusid": self.cus_id,
            "appid": self.app_id,
            "trxdate": trxdate,
            "orderid": orderid,
            "trxid": trxid,
            "termno": termno,
            "resendnotify": 1 if resendnotify else 0,
        })
        self.add_sign(data)
        return self._post('/apiweb/tranx/queryorder', data)

    def refund(self, reqsn, trxamt, trxdate=None, oldtrxid=None, oldbizseq=None, version="01", remark=None):
        """
        当面付订单支付-交易退款
        https://aipboss.allinpay.com/know/devhelp/home.php?id=208

        :param reqsn: 退款流水号
        :param trxamt: 退款金额
        :param trxdate: 交易日期
        :param oldtrxid: 原交易单号
        :param oldbizseq: 原交易商户单号
        :param version: 接口版本编号
        :param remark: 退款备注
        """
        if not oldtrxid and not oldbizseq:
            raise ValueError("oldtrxid和oldbizseq不能同时为空")

        data = optionaldict({
            "cusid": self.cus_id,
            "appid": self.app_id,
            "version": version,
            "trxdate": trxdate,
            "reqsn": reqsn,
            "oldtrxid": oldtrxid,
            "oldbizseq": oldbizseq,
            "trxamt": trxamt,
            "remark": remark,
        })
        self.add_sign(data)
        return self._post('/voapiweb/unitorder/refund', data)

    def cuspay(self, c, oid=None, amt=None, trxreserve=None):
        """
        自带参数的当面付订单接口
        https://aipboss.allinpay.com/know/devhelp/home.php?id=292

        :param c: 通联分配的二维码编号
        :param oid: 订单编号
        :param amt: 交易金额
        :param trxreserve: 业务备注信息
        """
        if not oid and not amt:
            raise ValueError("oid和amt不能同时为空")

        data = optionaldict({
            "appid": self.app_id,
            "c": c,
            "oid": oid,
            "amt": amt,
            "trxreserve": trxreserve
        })
        self.add_sign(data, random_str_key=None)
        return parse.urljoin(self.SYB_API_BASE_URL, '/sappweb/usertrans/cuspay?%s' % parse.urlencode(data))
