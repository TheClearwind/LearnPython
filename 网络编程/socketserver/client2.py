import socket
import random
sk=socket.socket()
addr='127.0.0.1'
sk.connect((addr,8888))
while 1:
    content=input('Lambda >>')
    if content=='q':
        sk.send(b'q')
        break
    sk.send(bytes('lambda:'+content,encoding='utf-8'))
    msg=sk.recv(1024).decode('utf-8')
    print(msg)
sk.close()