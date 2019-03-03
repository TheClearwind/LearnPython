import socketserver

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        while 1:
            msg=self.request.recv(1024).decode('utf-8')
            if msg=='q':
                break
            print(msg)
            info=input(">>").encode('utf-8')
            self.request.send(info)

if __name__=='__main__':
    tcpServer=socketserver.ThreadingTCPServer(('127.0.0.1',8888),MyServer)
    tcpServer.serve_forever()