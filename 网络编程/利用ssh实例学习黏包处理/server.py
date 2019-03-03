# 只有TCP的时候才会出现黏包
import struct #解决黏包的利器
import socket

sk=socket.socket()
ip_port=('127.0.0.1',8080)
sk.bind(ip_port)
sk.listen()
con,add=sk.accept()
while True:
    cmd=input(">>")
    con.send(cmd.encode('gbk'))
    if cmd=='q':
        break
    r=con.recv(4)
    data_size=struct.unpack('i',r)[0]
    ret=con.recv(int(data_size)).decode('gbk')
    print(ret)
sk.close()