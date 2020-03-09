from random import getrandbits
from key_exchange import rsa


def test_rsa_cryptosystem():
    bits = 16
    message = getrandbits(bits)
    print("original message = %d" % message)

    public_key, private_key = rsa.generate_keys(bits)

    cipher = rsa.encrypt(message, public_key)
    print("cipher:", cipher)

    recovered_message = rsa.decrypt(cipher, private_key)
    print("recovered message = %d" % recovered_message)
    assert message == recovered_message

