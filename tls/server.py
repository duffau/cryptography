import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = "0.0.0.0"
PORT = 8080
s.connect((HOST, PORT))