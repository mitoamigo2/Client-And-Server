import socket

host = 'localhost'
port = 50000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)

while True:
    clientsocket, address = server.accept()
    print(f"connection from {address} was connected!")
    clientsocket.send(bytes('You entered in a server', "utf-8"))
