import json
import struct
import socket
import os
head={'fileName':'models-master.zip','filePath':r'E:\Download','fileSize':''}
fileName = os.path.join(head['filePath'],head['fileName'])
head['fileSize']=os.path.getsize(fileName)

head_j=json.dumps(head)
head_b=head_j.encode('utf-8')
head_size=len(head_b)
head_size_b=struct.pack('i',head_size)

ip_port=('127.0.0.1',8080)
sk=socket.socket()
sk.connect(ip_port)
sk.send(head_size_b)
sk.send(head_b)

buffer=4096
with open(fileName,'rb') as f:
    fileSize=head['fileSize']
    content=None
    while fileSize:
        if fileSize>=buffer:
            content=f.read(buffer)
            fileSize-=buffer
        else:
            content=f.read(fileSize)
            fileSize=0
        sk.send(content)
print("发送完毕")
sk.close()