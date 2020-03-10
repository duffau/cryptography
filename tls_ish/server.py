import socket

HOST = "127.0.0.1"
PORT = 8080
ADDRESS = (HOST, PORT)

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(ADDRESS)
serversocket.listen(5)

while True:
    (clientsocket, address) = serversocket.accept()
    print(clientsocket)
