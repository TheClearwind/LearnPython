import socket
sk=socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('172.31.166.40',8868))

while 1:
    msg,addr=sk.recvfrom(1024)
    temp=msg.split('|')
    info=temp[1]+":"+temp[1]
    print(info.encode('utf-8'))
    sk.sendto(msg,addr)
sk.close()
