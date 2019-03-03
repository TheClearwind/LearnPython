import struct
import socket
import subprocess
sk=socket.socket()
ip_port=('127.0.0.1',8080)
sk.connect(ip_port)
while True:
    ret=sk.recv(1024).decode('gbk')
    if ret=='q':
        break
    r=subprocess.Popen(ret,shell=True,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
    std_out=r.stdout.read()
    std_err=r.stderr.read()
    size=len(std_out)+len(std_err)
    size=struct.pack('i',size)
    sk.send(size)
    sk.send(std_out)
    sk.send(std_err)

sk.close()