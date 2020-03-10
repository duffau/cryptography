import socket
from symmetric_encryption.xor_cipher import encrypt

HOST = "127.0.0.1"
PORT = 8080
ADDRESS = (HOST, PORT)
SHARED_SECRET = 1234

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(ADDRESS)
    message = 'Hello'
    cipher = encrypt(message, SHARED_SECRET)
    sent = 0
    while sent < len(cipher):
        sent += s.send(cipher[sent:])
