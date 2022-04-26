from hypothesis import example, given
from hypothesis import strategies as st

from pycmmn.crypto.AES256 import AES256


@given(st.text())
@example("\x10")
@example("")
def test_aes256_with_default_seed(data):
    aes256 = AES256()
    assert data == aes256.decrypt(aes256.encrypt(data))


@given(st.binary(min_size=16), st.text())
def test_aes256_with_key(key, data):
    aes256 = AES256(key)
    assert data == aes256.decrypt(aes256.encrypt(data))
