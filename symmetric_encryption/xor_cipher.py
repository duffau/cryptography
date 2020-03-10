
def encrypt(message: str, key: int, bits: int = 16):
    n_bytes = bits // 8
    key = (key % 2 ** bits).to_bytes(n_bytes, 'big')
    cipher = bytearray()
    for i, message_byte in enumerate(message.encode('utf-8')):
        cipher.append(message_byte ^ key[i % n_bytes])
    return bytes(cipher)


def decrypt(cipher: bytes, key: int, bits: int = 16):
    n_bytes = bits // 8
    key = (key % 2 ** bits).to_bytes(n_bytes, 'big')
    message = bytearray()
    for i, cipher_byte in enumerate(cipher):
        message.append(cipher_byte ^ key[i % n_bytes])
    return message.decode('utf-8')


