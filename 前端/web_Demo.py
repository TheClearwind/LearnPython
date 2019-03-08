# web demo

import socket

sk = socket.socket()
sk.bind(('127.0.0.1',8000))
sk.listen()
while 1:
    con,add=sk.accept()
    con.recv(1024)
    con.send(b'HTTP/1.1 200 OK\r\n\r\n')
    with open('HTML/html01.html','rb') as f:
        con.send(f.read())

