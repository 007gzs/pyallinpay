# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import unittest

from allinpay.core.utils import ObjectDict, AllInPayMd5Signer


class UtilityTestCase(unittest.TestCase):

    def test_object_dict(self):
        obj = ObjectDict()
        self.assertTrue(obj.xxx is None)
        obj.xxx = 1
        self.assertEqual(1, obj.xxx)

    def test_wechat_card_signer(self):

        signer = AllInPayMd5Signer(key="1234567890")
        signer.add_data('789')
        signer.add_data('456')
        signer.add_data('123')
        signature = signer.signature

        self.assertEqual('83DE4F53C5FFFE5A7B5BD402C53BA939', signature)
