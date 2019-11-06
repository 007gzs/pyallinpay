
PyAllInPay 使用文档
========================================

PyAllInPay 是通联支付 Python SDK。

快速入门
-------------

.. toctree::
   :maxdepth: 2

   install


开始使用
--------------------
建议在使用前先阅读 `通联支付文档 <https://aipboss.allinpay.com/know/devhelp/index.php>`_

.. toctree::
   :glob:
   :maxdepth: 2

   client/index

调用示例::

    from allinpay import AllInPayClient, AllInPayTestClient

    client = AllInPayClient('00000003', '990440148166000', 'a0ea3fa20dbd7bb4d5abf1d59d63bae8')  # 生产环境
    test_client = AllInPayTestClient('00000051', '990581007426001', 'allinpay888')  # 测试环境

    info = client.unitorder.pay('1234567890', 1, 'W01')
    info = test_client.unitorder.pay('1234567890', 1, 'W01')


Changelogs
---------------

.. toctree::
   :maxdepth: 1

   changelog

