import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 7777))

while True:
    msg = client.recv(1024)
    print(msg.decode("utf-8"))
