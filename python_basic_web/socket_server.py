import socket

HOST = ''
PORT =  50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

connection, address = s.accept()
print('connected by', address)

while True:
    data = connection.recv(1024)
    if not data:
        break
    recvData = "[server response] "+data
    connection.send(recvData)

connection.close()
