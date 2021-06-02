# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import unittest

import pytest

from allinpay.core.utils import ObjectDict, AllInPayMd5Signer, AllInPayRsaSigner


class UtilityTestCase(unittest.TestCase):

    def test_object_dict(self):
        obj = ObjectDict()
        self.assertTrue(obj.xxx is None)
        obj.xxx = 1
        self.assertEqual(1, obj.xxx)

    def test_md5_signer(self):

        signer = AllInPayMd5Signer(key="1234567890")
        signer.add_data('789')
        signer.add_data('456')
        signer.add_data('123')
        signature = signer.signature

        self.assertEqual('83de4f53c5fffe5a7b5bd402c53ba939', signature)

    def test_rsa_signer(self):
        private_key = (
            "MIICdQIBADANBgkqhkiG9w0BAQEFAASCAl8wggJbAgEAAoGBAJgHMGYsspghvP+yCbjLG43CkZuQ3YJyDcmEKxvmgblITfmi"
            "TPx2b9Y2iwDT9gnLGExTDm1BL2A8VzMobjaHfiCmTbDctu680MLmpDDkVXmJOqdlXh0tcLjhN4+iDA2KkRqiHxsDpiaKT6MM"
            "BuecXQbJtPlVc1XjVhoUlzUgPCrvAgMBAAECgYAV9saYTGbfsdLOF5kYo0dve1JxaO7dFMCcgkV+z2ujKtNmeHtU54DlhZXJ"
            "iytQY5Dhc10cjb6xfFDrftuFcfKCaLiy6h5ETR8jyv5He6KH/+X6qkcGTkJBYG1XvyyFO3PxoszQAs0mrLCqq0UItlCDn0G7"
            "2MR9/NuvdYabGHSzEQJBAMXB1/DUvBTHHH4LiKDiaREruBb3QtP72JQS1ATVXA2v6xJzGPMWMBGQDvRfPvuCPVmbHENX+lRx"
            "MLp39OvIn6kCQQDEzYpPcuHW/7h3TYHYc+T0O6z1VKQT2Mxv92Lj35g1XqV4Oi9xrTj2DtMeV1lMx6n/3icobkCQtuvTI+Ac"
            "qfTXAkB6bCz9NwUUK8sUsJktV9xJN/JnrTxetOr3h8xfDaJGCuCQdFY+rj6lsLPBTnFUC+Vk4mQVwJIE0mmjFf22NWW5AkAm"
            "sVaRGkAmui41Xoq52MdZ8WWm8lY0BLrlBJlvveU6EPqtcZskWW9KiU2euIO5IcRdpvrB6zNMgHpLD9GfMRcPAkBUWOV/dH13"
            "v8V2Y/Fzuag/y5k3/oXi/WQnIxdYbltad2xjmofJ7DbB7MJqiZZD8jlr8PCZPwRNzc5ntDStc959"
        )
        signer = AllInPayRsaSigner(key=AllInPayRsaSigner.get_private_key(private_key), delimiter=b"&")
        signer.add_data('appid=00000051')
        signer.add_data('cusid=990581007426001')
        signer.add_data('randomstr=82712208')
        signer.add_data('signtype=RSA')
        signer.add_data('trxid=112094120001088317')
        signer.add_data('version=11')
        signature = signer.signature
        self.assertTrue(signer.verify(signature))

        self.assertEqual(
            (
                'ce6EAOj4rhoBMJM5MJCNG4qQ/CVMTWkoRuSGpSzRAnD3U3V5QyHkQUEej2eZXRaa+qSbw2/IJJSPV0sPuAia1+'
                'ccb7OnvxyZqkV9wQyimX6qAMz0K+UWFhQ5McCcQ/XsFhhezoVd5QgL7PtdvuK1AtjuzA3J9yzNmwuPssPnKnc='
            ),
            signature
        )

    def test_rsa_verify(self):
        public_key = (
            "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCYBzBmLLKYIbz/sgm4yxuNwpGbkN2Ccg3J"
            "hCsb5oG5SE35okz8dm/WNosA0/YJyxhMUw5tQS9gPFczKG42h34gpk2w3LbuvNDC5qQw5FV5"
            "iTqnZV4dLXC44TePogwNipEaoh8bA6Ymik+jDAbnnF0GybT5VXNV41YaFJc1IDwq7wIDAQAB"
        )
        signer = AllInPayRsaSigner(key=AllInPayRsaSigner.get_public_key(public_key), delimiter=b"&")
        signer.add_data('appid=00000051')
        signer.add_data('cusid=990581007426001')
        signer.add_data('randomstr=82712208')
        signer.add_data('signtype=RSA')
        signer.add_data('trxid=112094120001088317')
        signer.add_data('version=11')
        self.assertTrue(
            signer.verify(
                'ce6EAOj4rhoBMJM5MJCNG4qQ/CVMTWkoRuSGpSzRAnD3U3V5QyHkQUEej2eZXRaa+qSbw2/IJJSPV0sPuAia1+'
                'ccb7OnvxyZqkV9wQyimX6qAMz0K+UWFhQ5McCcQ/XsFhhezoVd5QgL7PtdvuK1AtjuzA3J9yzNmwuPssPnKnc='
            )
        )

    @pytest.mark.skip(reason="not support")
    def test_sm2_signer(self):
        private_key = (
            "MIGTAgEAMBMGByqGSM49AgEGCCqBHM9VAYItBHkwdwIBAQQgNqz1EieIP8QVzV7vEmx5e8f7XN7/MIzoeXgEinxcG0agCgYIKoEc"
            "z1UBgi2hRANCAAQNfkEgaCQ4cdZ4aD2LWMcnkk5LALQfL05oY8x8XQDIyUM44N15YcTwtFNvHYgyeNRa93vlEUutp935n6rp4yuf"
        )
        signer = AllInPayRsaSigner(key=AllInPayRsaSigner.get_private_key(private_key), delimiter=b"&")
        signer.add_data('appid=00000051')
        signer.add_data('cusid=990581007426001')
        signer.add_data('randomstr=75016315')
        signer.add_data('signtype=SM2')
        signer.add_data('trxid=112094120001088317')
        signer.add_data('version=11')
        signature = signer.signature
        self.assertTrue(signer.verify(signature))
        self.assertEqual(
            'm4ki0xZ+19LtqjuyG8Qb0ytD3Q8B166mboCeg+6Ar1Z4XmQB14LrcfddkM121EbroDDnJ17bbJAH/S+8jus9iQ==', signature
        )
