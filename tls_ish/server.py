import socket
from symmetric_encryption.xor_cipher import decrypt

HOST = "127.0.0.1"
PORT = 8080
ADDRESS = (HOST, PORT)
SHARED_SECRET = 1234

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(ADDRESS)
serversocket.listen()

while True:
    (clientsocket, address) = serversocket.accept()
    recieved_message = bytearray()
    while True:
        recvd = clientsocket.recv(2048)
        if not recvd: break
        recieved_message += recvd
    print('recieved message: %s' % bytes(recieved_message))
    print('decrypted message: %s' % decrypt(recieved_message, SHARED_SECRET))

serversocket.close()