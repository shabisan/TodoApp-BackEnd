import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    try:
        sock.connect(('0.0.0.0', 9010))
        sock.send('Hello, world!'.encode('utf-8'))
        data = sock.recv(1024).decode('utf-8')
        if not data:
            break
        print(data)
        break
    except socket.error:
        continue