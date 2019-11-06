# encoding: utf-8
from __future__ import absolute_import, unicode_literals

import datetime

from optionaldict import optionaldict

from .base import AllInPayBaseAPI


class QPay(AllInPayBaseAPI):
    """
    快捷支付
    """
    def agreeapply(self, meruserid, accttype, acctno, idno, acctname, mobile,
                   validdate=None, cvv2=None, reqip=None, version='11'):
        """
        快捷支付 - 签约申请
        https://aipboss.allinpay.com/know/devhelp/home.php?id=136

        :param meruserid: 商户用户号
        :param accttype: 卡类型
        :param acctno: 银行卡号
        :param idno: 证件号
        :param acctname: 户名
        :param mobile: 手机号码
        :param validdate: 有效期
        :param cvv2: Cvv2
        :param reqip: 请求ip
        :param version: 版本号
        """
        data = optionaldict({
            "cusid": self.cus_id,
            "appid": self.app_id,
            "reqip": reqip,
            "version": version,
            "reqtime": datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
            "meruserid": meruserid,
            "accttype": accttype,
            "acctno": acctno,
            "idno": idno,
            "acctname": acctname,
            "mobile": mobile,
            "validdate": validdate,
            "cvv2": cvv2
        })
        self.add_sign(data)
        return self._post('/apiweb/qpay/agreeapply', data)

    def agreeconfirm(self, meruserid, accttype, acctno, idno, acctname, mobile, smscode, thpinfo,
                     validdate=None, cvv2=None, reqip=None, version='11'):
        """
        快捷支付 - 签约申请确认
        https://aipboss.allinpay.com/know/devhelp/home.php?id=137

        :param meruserid: 商户用户号
        :param accttype: 卡类型
        :param acctno: 银行卡号
        :param idno: 证件号
        :param acctname: 户名
        :param mobile: 手机号码
        :param smscode: 短信验证码
        :param thpinfo: 交易透传信息
        :param validdate: 有效期
        :param cvv2: Cvv2
        :param reqip: 请求ip
        :param version: 版本号
        """
        data = optionaldict({
            "cusid": self.cus_id,
            "appid": self.app_id,
            "reqip": reqip,
            "version": version,
            "reqtime": datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
            "meruserid": meruserid,
            "accttype": accttype,
            "acctno": acctno,
            "idno": idno,
            "acctname": acctname,
            "mobile": mobile,
            "smscode": smscode,
            "thpinfo": thpinfo,
            "validdate": validdate,
            "cvv2": cvv2
        })
        self.add_sign(data)
        return self._post('/apiweb/qpay/agreeconfirm', data)

    def payapplyagree(self, orderid, agreeid, amount, subject, notifyurl, validtime=None, trxreserve=None, asinfo=None,
                      currency="CNY", reqip=None, version='11'):
        """
        快捷支付 - 商户支付申请
        https://aipboss.allinpay.com/know/devhelp/home.php?id=139

        :param orderid: 商户订单号
        :param agreeid: 协议编号
        :param amount: 订单金额
        :param subject: 订单内容
        :param notifyurl: 交易结果通知地址
        :param validtime: 有效时间
        :param trxreserve: 交易备注
        :param asinfo: 分账信息
        :param currency: 币种
        :param reqip: 请求ip
        :param version: 版本号
        """
        data = optionaldict({
            "cusid": self.cus_id,
            "appid": self.app_id,
            "reqip": reqip,
            "version": version,
            "reqtime": datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
            "orderid": orderid,
            "agreeid": agreeid,
            "amount": amount,
            "subject": subject,
            "notifyurl": notifyurl,
            "validtime": validtime,
            "trxreserve": trxreserve,
            "asinfo": asinfo,
            "currency": currency
        })
        self.add_sign(data)
        return self._post('/apiweb/qpay/payapplyagree', data)

    def payagreeconfirm(self, orderid, agreeid, thpinfo, smscode=None, reqip=None, version='11'):
        """
        快捷支付 - 支付确认
        https://aipboss.allinpay.com/know/devhelp/home.php?id=140

        :param orderid: 订单号
        :param agreeid: 协议编号
        :param thpinfo: 交易透传信息
        :param smscode: 短信验证码
        :param reqip: 请求ip
        :param version: 版本号
        """
        data = optionaldict({
            "cusid": self.cus_id,
            "appid": self.app_id,
            "reqip": reqip,
            "version": version,
            "reqtime": datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
            "orderid": orderid,
            "agreeid": agreeid,
            "thpinfo": thpinfo,
            "smscode": smscode
        })
        self.add_sign(data)
        return self._post('/apiweb/qpay/payagreeconfirm', data)

    def paysmsagree(self, orderid, agreeid=None, thpinfo=None, reqip=None, version='11'):
        """
        快捷支付 - 重新获取支付短信
        https://aipboss.allinpay.com/know/devhelp/home.php?id=141

        :param orderid: 商户订单号
        :param agreeid: 协议编号
        :param thpinfo: 交易透传信息
        :param reqip: 请求ip
        :param version: 版本号
        """
        data = optionaldict({
            "cusid": self.cus_id,
            "appid": self.app_id,
            "reqip": reqip,
            "version": version,
            "reqtime": datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
            "orderid": orderid,
            "agreeid": agreeid,
            "thpinfo": thpinfo
        })
        self.add_sign(data)
        return self._post('/apiweb/qpay/paysmsagree', data)

    def agreequery(self, meruserid, reqip=None, version='11'):
        """
        快捷支付 - 协议查询接口
        https://aipboss.allinpay.com/know/devhelp/home.php?id=213

        :param meruserid: 商户用户号
        :param reqip: 请求ip
        :param version: 版本号
        """
        data = optionaldict({
            "cusid": self.cus_id,
            "appid": self.app_id,
            "reqip": reqip,
            "version": version,
            "reqtime": datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
            "meruserid": meruserid
        })
        self.add_sign(data)
        return self._post('/apiweb/qpay/agreequery', data, result_processor=lambda x: x['agreelist'])

    def unbind(self, agreeid, reqip=None, version='11'):
        """
        快捷支付 - 银行卡解绑
        https://aipboss.allinpay.com/know/devhelp/home.php?id=142

        :param agreeid: 协议编号
        :param reqip: 请求ip
        :param version: 版本号
        """
        data = optionaldict({
            "cusid": self.cus_id,
            "appid": self.app_id,
            "reqip": reqip,
            "version": version,
            "reqtime": datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
            "agreeid": agreeid
        })
        self.add_sign(data)
        return self._post('/apiweb/qpay/unbind', data)

    def cancel(self, orderid, trxamt, oldorderid=None, oldtrxid=None, reqip=None, version='11'):
        """
        快捷支付 - 交易撤销
        https://aipboss.allinpay.com/know/devhelp/home.php?id=143

        :param orderid: 商户退款交易单号
        :param trxamt: 交易金额
        :param oldorderid: 原交易单号
        :param oldtrxid: 原交易流水
        :param reqip: 请求ip
        :param version: 版本号
        """
        if not oldorderid and not oldtrxid:
            raise ValueError("oldorderid和oldtrxid必填其一")
        data = optionaldict({
            "cusid": self.cus_id,
            "appid": self.app_id,
            "reqip": reqip,
            "version": version,
            "reqtime": datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
            "orderid": orderid,
            "trxamt": trxamt,
            "oldorderid": oldorderid,
            "oldtrxid": oldtrxid
        })
        self.add_sign(data)
        return self._post('/apiweb/qpay/cancel', data)

    def refund(self, orderid, trxamt, oldorderid=None, oldtrxid=None, reqip=None, version='11'):
        """
        快捷支付 - 交易退款
        https://aipboss.allinpay.com/know/devhelp/home.php?id=144

        :param orderid: 商户退款交易单号
        :param trxamt: 交易金额
        :param oldorderid: 原交易单号
        :param oldtrxid: 原交易流水
        :param reqip: 请求ip
        :param version: 版本号
        """
        if not oldorderid and not oldtrxid:
            raise ValueError("oldorderid和oldtrxid必填其一")
        data = optionaldict({
            "cusid": self.cus_id,
            "appid": self.app_id,
            "reqip": reqip,
            "version": version,
            "reqtime": datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
            "orderid": orderid,
            "trxamt": trxamt,
            "oldorderid": oldorderid,
            "oldtrxid": oldtrxid
        })
        self.add_sign(data)
        return self._post('/apiweb/qpay/refund', data)

    def query(self, orderid=None, trxid=None, reqip=None, version='11'):
        """
        快捷支付 - 交易查询
        https://aipboss.allinpay.com/know/devhelp/home.php?id=145

        :param orderid: 商户的交易订单号
        :param trxid: 平台交易流水
        :param reqip: 请求ip
        :param version: 版本号
        """
        if not orderid and not trxid:
            raise ValueError("orderid和trxid必填其一")
        data = optionaldict({
            "cusid": self.cus_id,
            "appid": self.app_id,
            "reqip": reqip,
            "version": version,
            "reqtime": datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
            "orderid": orderid,
            "trxid": trxid
        })
        self.add_sign(data)
        return self._post('/apiweb/qpay/query', data)
