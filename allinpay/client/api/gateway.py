# encoding: utf-8
from __future__ import absolute_import, unicode_literals

from optionaldict import optionaldict

from .base import AllInPayBaseAPI


class Gateway(AllInPayBaseAPI):
    """
    网关支付
    """
    def pay(self, orderid, trxamt, paytype, returl=None, notifyurl=None,
            validtime=720, goodsid=None, goodsinf=None, gateid=None, limitpay=None, charset='UTF-8'):
        """
        网关支付 - 订单提交接口（商户网站->支付网关）
        https://aipboss.allinpay.com/know/devhelp/home.php?id=73

        :param orderid: 商户唯一订单号
        :param trxamt: 付款金额
        :param paytype: 交易类型
        :param returl: 页面跳转同步通知页面路径
        :param notifyurl: 服务器异步通知页面路径
        :param validtime: 有效时间
        :param goodsid: 商品号
        :param goodsinf: 商品描述信息
        :param gateid: 支付银行
        :param limitpay: 支付限制
        :param charset: 参数字符编码集
        """
        if not returl and not notifyurl:
            raise ValueError("returl和notifyurl不能同时为空")
        data = optionaldict({
            "cusid": self.cus_id,
            "appid": self.app_id,
            "orderid": orderid,
            "trxamt": trxamt,
            "paytype": paytype,
            "returl": returl,
            "notifyurl": notifyurl,
            "validtime": validtime,
            "goodsid": goodsid,
            "goodsinf": goodsinf,
            "gateid": gateid,
            "limitpay": limitpay,
            "charset": charset
        })
        self.add_sign(data)
        return self._post('/apiweb/tranx/queryorder', data)

    def query(self, orderid=None, trxid=None):
        """
        网关支付 - 交易查询接口
        https://aipboss.allinpay.com/know/devhelp/home.php?id=73

        :param orderid: 商户订单号
        :param trxid: 平台交易流水
        """
        if not orderid and not trxid:
            raise ValueError("orderid和trxid必填其一")
        data = optionaldict({
            "cusid": self.cus_id,
            "appid": self.app_id,
            "orderid": orderid,
            "trxid": trxid
        })
        self.add_sign(data)
        return self._post('/apiweb/gateway/query', data)

    def refund(self, reqsn, trxamt, orderid=None, trxid=None, notifyurl=None):
        """
        网关支付 - 订单退款接口
        https://aipboss.allinpay.com/know/devhelp/home.php?id=73

        :param reqsn: 商户退款流水
        :param trxamt: 退款金额
        :param orderid: 商户订单号
        :param trxid: 平台交易流水
        :param notifyurl: 服务器异步通知页面路径
        """
        if not orderid and not trxid:
            raise ValueError("orderid和trxid必填其一")
        data = optionaldict({
            "cusid": self.cus_id,
            "appid": self.app_id,
            "reqsn": reqsn,
            "trxamt": trxamt,
            "orderid": orderid,
            "trxid": trxid,
            "notifyurl": notifyurl
        })
        self.add_sign(data)
        return self._post('/apiweb/gateway/refund', data)
