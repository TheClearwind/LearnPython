import json
import struct
import socket

sk=socket.socket()
ip_port=('127.0.0.1',8080)
sk.bind(ip_port)
sk.listen()
con,addr=sk.accept()

head_size_b=con.recv(4)
head_size=struct.unpack('i',head_size_b)[0]
head_b=con.recv(head_size)
head=head_b.decode('utf-8')
head=json.loads(head)
fileName=head['fileName']
fileSize=head['fileSize']

with open(fileName,'wb') as f:
    buffer=4096
    while fileSize:
        if fileSize>=buffer:
            content=con.recv(buffer)
            f.write(content)
            fileSize-=buffer
        else:
            content=con.recv(fileSize)
            f.write(content)
            fileSize=0
print("接收完毕")
con.close()
sk.close()