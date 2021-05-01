import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', 9010))
sock.listen(5)
while True:
    csock, caddr = sock.accept()
    data = csock.recv(1024).decode('utf-8')
    if not data:
        break
    print(data)
    if 'Hello, world!' in data:
        csock.send('Hello form server!'.encode('utf-8'))
    break
