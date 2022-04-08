# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jin.kim@seculayer.com
# Powered by Seculayer © 2021 Service Model Team, R&D Center. 

import base64
from Crypto.Cipher import AES


# ---------------------------------------------------------------------------------------------------------------------
# class : AES256
class AES256(object):
    def __init__(self, key=None):
        self.BLOCK_SIZE = 16

        # INPUT KEY
        if key is None:
            self.key = b"AES/CBC/PKCS5Padding"
        else:
            self.key = key

        # INIT VECTOR
        self.iv = self.key[:self.BLOCK_SIZE]

    def _pad(self, plane_text):
        length = self.BLOCK_SIZE - (len(plane_text) % self.BLOCK_SIZE)
        plane_text += chr(length) * length
        return plane_text

    @staticmethod
    def _unpad(decrypt_text):
        result = decrypt_text[0:-int(decrypt_text[-1])]
        return result

    def encrypt(self, plane_text):
        _plane_text = plane_text.encode()
        raw = self._pad(plane_text)
        aes = AES.new(
            self.key[:self.BLOCK_SIZE], AES.MODE_CBC, self.iv
        )
        enc = aes.encrypt(raw)
        return base64.b64encode(enc).decode("utf-8")

    def decrypt(self, encrypt_text):
        b64_dec = base64.b64decode(encrypt_text)
        aes = AES.new(
            self.key[:self.BLOCK_SIZE], AES.MODE_CBC, self.iv
        )
        dec = aes.decrypt(b64_dec)
        return self._unpad(dec).decode("utf-8")


if __name__ == '__main__':
    import sys

    aes = AES256()
    _pt = sys.argv[1]
    _et = aes.encrypt(plane_text=_pt)
    print(_et)
    _dt = aes.decrypt(_et)
    print(_dt)
