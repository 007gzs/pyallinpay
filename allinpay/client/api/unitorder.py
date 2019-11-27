# encoding: utf-8
from __future__ import absolute_import, unicode_literals

import json

import six
from six.moves.urllib import parse
from optionaldict import optionaldict

from .base import AllInPayBaseAPI


class UnitOrder(AllInPayBaseAPI):
    """
    网上收银统一下单
    """

    def pay(
            self, reqsn, trxamt, paytype, acct=None, body=None, notify_url=None, limit_pay=None,
            sub_appid=None, goods_tag=None, benefitdetail=None, chnlstoreid=None, subbranch=None,
            extendparams=None, cusip=None, idno=None, truename=None, asinfo=None, fqnum=None,
            validtime=5, version="11", remark=None
    ):
        """
        网上收银统一下单-统一支付接口
        https://aipboss.allinpay.com/know/devhelp/home.php?id=88

        :param reqsn: 商户交易单号
        :param trxamt: 交易金额
        :param paytype: 交易方式
        :param acct: 支付平台用户标识
        :param body: 订单标题
        :param notify_url: 交易结果通知地址
        :param limit_pay: 支付限制
        :param sub_appid: 微信子appid
        :param goods_tag: 订单优惠标识
        :param benefitdetail: 优惠信息
        :param chnlstoreid: 渠道门店编号
        :param subbranch: 门店号
        :param extendparams: 拓展参数
        :param cusip: 终端ip
        :param idno: 证件号
        :param truename: 付款人真实姓名
        :param asinfo: 分账信息
        :param fqnum: 花呗分期
        :param validtime: 有效时间
        :param version: 版本号
        :param remark: 备注
        """
        if extendparams is not None and isinstance(extendparams, six.string_types):
            extendparams = json.dumps(extendparams)
        data = optionaldict({
            "cusid": self.cus_id,
            "appid": self.app_id,
            "reqsn": reqsn,
            "trxamt": trxamt,
            "paytype": paytype,
            "acct": acct,
            "body": body,
            "notify_url": notify_url,
            "limit_pay": limit_pay,
            "sub_appid": sub_appid,
            "goods_tag": goods_tag,
            "benefitdetail": benefitdetail,
            "chnlstoreid": chnlstoreid,
            "subbranch": subbranch,
            "extendparams": extendparams,
            "cusip": cusip,
            "idno": idno,
            "truename": truename,
            "asinfo": asinfo,
            "fqnum": fqnum,
            "validtime": validtime,
            "version": version,
            "remark": remark
        })
        self.add_sign(data)
        return self._post("/apiweb/unitorder/pay", data)

    def scanqrpay(
            self, reqsn, trxamt, authcode, body=None, limit_pay=None,
            goods_tag=None, benefitdetail=None, chnlstoreid=None, subbranch=None,
            idno=None, truename=None, asinfo=None, fqnum=None,
            version="11", remark=None
    ):
        """
        网上收银统一统一扫码接口
        https://aipboss.allinpay.com/know/devhelp/home.php?id=88

        :param reqsn: 商户交易单号
        :param trxamt: 交易金额
        :param authcode: 支付授权码
        :param body: 订单标题
        :param limit_pay: 支付限制
        :param goods_tag: 订单优惠标识
        :param benefitdetail: 优惠信息
        :param chnlstoreid: 渠道门店编号
        :param subbranch: 门店号
        :param idno: 证件号
        :param truename: 付款人真实姓名
        :param asinfo: 分账信息
        :param fqnum: 花呗分期
        :param version: 版本号
        :param remark: 备注
        """
        data = optionaldict({
            "cusid": self.cus_id,
            "appid": self.app_id,
            "reqsn": reqsn,
            "trxamt": trxamt,
            "authcode": authcode,
            "body": body,
            "limit_pay": limit_pay,
            "goods_tag": goods_tag,
            "benefitdetail": benefitdetail,
            "chnlstoreid": chnlstoreid,
            "subbranch": subbranch,
            "idno": idno,
            "truename": truename,
            "asinfo": asinfo,
            "fqnum": fqnum,
            "version": version,
            "remark": remark
        })
        self.add_sign(data)
        return self._post("/apiweb/unitorder/scanqrpay", data)

    def cancel(self, reqsn, trxamt, oldtrxid=None, oldreqsn=None, version="12"):
        """
        网上收银统一下单 - 交易撤销
        https://aipboss.allinpay.com/know/devhelp/home.php?id=91
        H5收银台 - 交易撤销
        https://aipboss.allinpay.com/know/devhelp/home.php?id=315
        手机支付控件 - 交易撤销
        https://aipboss.allinpay.com/know/devhelp/home.php?id=393

        :param reqsn: 商户退款交易单号
        :param trxamt: 交易金额
        :param oldtrxid: 原交易流水
        :param oldreqsn: 原交易单号
        :param version: 版本号
        """
        if not oldreqsn and not oldtrxid:
            raise ValueError("oldtrxid和oldbizseq不能同时为空")

        data = optionaldict({
            "cusid": self.cus_id,
            "appid": self.app_id,
            "reqsn": reqsn,
            "trxamt": trxamt,
            "oldtrxid": oldtrxid,
            "oldreqsn": oldreqsn,
            "version": version
        })
        self.add_sign(data)
        return self._post("/apiweb/unitorder/cancel", data)

    def refund(self, reqsn, trxamt, oldtrxid=None, oldreqsn=None, version="12", remark=None):
        """
        网上收银统一下单 - 交易退款
        https://aipboss.allinpay.com/know/devhelp/home.php?id=92
        H5收银台 - 交易退款
        https://aipboss.allinpay.com/know/devhelp/home.php?id=314
        手机支付控件 - 交易退款
        https://aipboss.allinpay.com/know/devhelp/home.php?id=394

        :param reqsn: 商户退款交易单号
        :param trxamt: 交易金额
        :param oldtrxid: 原交易流水
        :param oldreqsn: 原交易单号
        :param version: 版本号
        :param remark: 备注
        """
        if not oldreqsn and not oldtrxid:
            raise ValueError("oldtrxid和oldbizseq不能同时为空")

        data = optionaldict({
            "cusid": self.cus_id,
            "appid": self.app_id,
            "reqsn": reqsn,
            "trxamt": trxamt,
            "oldtrxid": oldtrxid,
            "oldreqsn": oldreqsn,
            "remark": remark,
            "version": version
        })
        self.add_sign(data)
        return self._post("/apiweb/unitorder/refund", data)

    def query(self, reqsn, trxid, version="12"):
        """
        网上收银统一下单 - 交易查询
        https://aipboss.allinpay.com/know/devhelp/home.php?id=93
        H5收银台 - 交易查询
        https://aipboss.allinpay.com/know/devhelp/home.php?id=314
        手机支付控件 - 交易查询
        https://aipboss.allinpay.com/know/devhelp/home.php?id=395

        :param reqsn: 商户退款交易单号
        :param trxid: 平台交易流水
        :param version: 版本号
        """
        if not reqsn and not trxid:
            raise ValueError("trxid和reqsn不能同时为空")

        data = optionaldict({
            "cusid": self.cus_id,
            "appid": self.app_id,
            "reqsn": reqsn,
            "trxid": trxid,
            "version": version
        })
        self.add_sign(data)
        return self._post("/apiweb/unitorder/query", data)

    def authcodetouserid(self, authcode, authtype, sub_appid=None, version="12"):
        """
        网上收银统一下单 - 根据授权码(付款码)获取用户ID
        https://aipboss.allinpay.com/know/devhelp/home.php?id=373

        :param authcode: 授权码（付款码）
        :param authtype: 授权码类型
        :param sub_appid: 微信支付appid
        :param version: 版本号
        """
        data = optionaldict({
            "cusid": self.cus_id,
            "appid": self.app_id,
            "authcode": authcode,
            "authtype": authtype,
            "sub_appid": sub_appid,
            "version": version
        })
        self.add_sign(data)
        return self._post("/apiweb/unitorder/query", data)

    def wxfacepayinfo(self, storeid, storename, subappid, rawdata, deviceid=None, attach=None, version="12"):
        """
        网上收银统一下单 - 根据授权码(付款码)获取用户ID
        https://aipboss.allinpay.com/know/devhelp/home.php?id=406

        :param storeid: 门店编号
        :param storename: 门店名称
        :param subappid: 微信支付appid
        :param rawdata: 初始化数据。由微信人脸SDK的接口返回。
        :param deviceid: 终端设备编号
        :param attach:  附加字段
        :param version: 版本号
        :return:
        """
        if attach is not None and isinstance(attach, six.string_types):
            attach = json.dumps(attach)
        data = optionaldict({
            "cusid": self.cus_id,
            "appid": self.app_id,
            "storeid": storeid,
            "storename": storename,
            "subappid": subappid,
            "rawdata": rawdata,
            "deviceid": deviceid,
            "attach": attach,
            "version": version
        })
        self.add_sign(data)
        return self._post("/apiweb/unitorder/query", data)

    def h5unionpay(self, reqsn, trxamt, returl, notify_url, body, charset='utf-8',
                   version="12", remark=None, validtime=5, limit_pay=None, asinfo=None):
        """
        H5收银台-订单提交接口
        https://aipboss.allinpay.com/know/devhelp/home.php?id=313

        :param reqsn: 商户唯一订单号
        :param trxamt: 付款金额(单位分)
        :param returl: 页面跳转同步通知页面路径
        :param notify_url: 服务器异步通知页面路径
        :param body: 订单标题
        :param charset: 参数字符编码集
        :param version: 版本号
        :param remark: 订单备注信息
        :param validtime: 有效时间
        :param limit_pay: 支付限制
        :param asinfo: 分账信息
        """
        data = optionaldict({
            "cusid": self.cus_id,
            "appid": self.app_id,
            "trxamt": trxamt,
            "reqsn": reqsn,
            "returl": returl,
            "notify_url": notify_url,
            "body": body,
            "version": version,
            "remark": remark,
            "validtime": validtime,
            "limit_pay": limit_pay,
            "asinfo": asinfo,
        })
        self.add_sign(data)
        return parse.urljoin(
            self.SYB_API_BASE_URL, '/apiweb/h5unionpay/unionorder?%s' % parse.urlencode(data, encoding=charset)
        )
