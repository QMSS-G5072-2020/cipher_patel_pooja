from cipher_pvp2108 import __version__
from cipher_pvp2108 import cipher_pvp2108

def test_version():
    assert __version__ == '0.1.0'


def test_negative_shift():
    actual= cipher_pvp2108.cipher('Pooja', -1)
    expected= 'OnniZ'
    assert actual == expected, "Expected {0}, but got {1} instead".format(expected, actual)
test_negative_shift()

