from symmetric_encryption.xor_cipher import encrypt, decrypt


def test_encrypt():
    message = "plain text message"
    key = 123
    cipher = encrypt(message, key)
    assert isinstance(cipher, bytes)
    assert message != cipher


def test_encrypt_different_keys():
    message = "plain text message"
    key1 = 65535
    key2 = 3459
    cipher_1 = encrypt(message, key1)
    cipher_2 = encrypt(message, key2)
    assert cipher_1 != cipher_2


def test_decrypt():
    cipher = b'p\x17a\x12n[t\x1ex\x0f \x16e\x08s\x1ag\x1e'
    key = 123
    message = decrypt(cipher, key)
    assert isinstance(message, str)
    assert cipher != message


def test_encrypt_decrypt_invertability():
    for key in [1, 123, 456, 5289, 2231, 65535]:
        message = "plain text message"
        cipher = encrypt(message, key)
        recovered_message = decrypt(cipher, key)
        assert message == recovered_message
