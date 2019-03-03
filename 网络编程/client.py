import socket
sk=socket.socket()
addr='118.190.205.174'
sk.connect((addr,8888))
while 1:
    content=input('>>')
    sk.send(bytes(content,encoding='utf-8'))
    print(sk.recv(1024).decode('utf-8'))
    if content=='拜拜':
        break
sk.close()