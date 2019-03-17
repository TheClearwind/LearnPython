import threading
value=10
lock=threading.Lock()
def add():
    global value
    lock.acquire() #对于全局变量的修改操作需要上锁防止多线程冲突
    for i in range(100000):
        value+=1
    lock.release()
    print(value)

if __name__ == '__main__':
    threading.Thread(target=add()).run()
    threading.Thread(target=add()).run()