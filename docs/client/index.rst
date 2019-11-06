通联支付接口
===========================================

.. module:: allinpay.client

.. autoclass:: AllInPayClient
   :members:
   :inherited-members:

.. autoclass:: AllInPayTestClient
   :members:
   :inherited-members:

`AllInPayClient` 基本使用方法::

   from allinpay import AllInPayClient, AllInPayTestClient

   client = AllInPayClient('00000003', '990440148166000', 'a0ea3fa20dbd7bb4d5abf1d59d63bae8')  # 生产环境
   test_client = AllInPayTestClient('00000051', '990581007426001', 'allinpay888')  # 测试环境

   info = client.unitorder.pay('1234567890', 1, 'W01')
   info = test_client.unitorder.pay('1234567890', 1, 'W01')


.. toctree::
   :maxdepth: 2
   :glob:

   api/*

