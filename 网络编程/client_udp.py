import socket
import random
sk=socket.socket(type=socket.SOCK_DGRAM)
addr_port=('118.190.205.174',8868)
r=str(random.randint(0,10))
while 1:
    content=input('%s>>'%r)
    sk.sendto((content+'|'+r).encode('utf-8'),addr_port)
    msg,addr=sk.recvfrom(1024)
    print(msg.decode('utf-8'))
sk.close()