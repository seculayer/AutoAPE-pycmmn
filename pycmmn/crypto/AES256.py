# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jin.kim@seculayer.com
# Powered by Seculayer © 2021 Service Model Team, R&D Center.

import base64
from typing import Optional, Union

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


class AES256(object):
    _BLOCK_SIZE = 16

    def __init__(self, key: Optional[bytes] = None):

        # INPUT KEY
        if key is None:
            self._key = b"AES/CBC/PKCS5Padding"
        else:
            self._key = key

        # INIT VECTOR
        self._iv = self._key[: self._BLOCK_SIZE]

    def encrypt(self, plane_text: str) -> str:
        data = pad(plane_text.encode("utf-8"), self._BLOCK_SIZE)
        aes = AES.new(self._key[: self._BLOCK_SIZE], AES.MODE_CBC, self._iv)
        enc = aes.encrypt(data)
        return base64.b64encode(enc).decode("utf-8")

    def decrypt(self, encrypt_text: Union[str, bytes, bytearray]) -> str:
        b64_dec = base64.b64decode(encrypt_text)
        aes = AES.new(self._key[: self._BLOCK_SIZE], AES.MODE_CBC, self._iv)
        dec = aes.decrypt(b64_dec)
        return unpad(dec, self._BLOCK_SIZE).decode("utf-8")


if __name__ == "__main__":
    import sys

    aes = AES256()
    _pt = sys.argv[1]
    _et = aes.encrypt(plane_text=_pt)
    print(_et)
    _dt = aes.decrypt(_et)
    print(_dt)
