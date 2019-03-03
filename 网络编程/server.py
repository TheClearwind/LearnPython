import socket
sk=socket.socket()
sk.bind(('127.0.0.1',8888))
sk.listen()
con,addr=sk.accept()
while 1:
    ret=con.recv(1024)
    con.send(ret)
    ret=ret.decode('utf-8')
    print(ret)
    if ret=='拜拜':
        break
con.close()
sk.close()
