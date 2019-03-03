from multiprocessing import Process
from time import sleep
import os
def func(*args):
    sleep(2)
    print('*'*args[0])
if __name__=='__main__': #必须写否则报错
    p=Process(target=func,args=(10,))
    p.start()
    p.join() #子进程变成了同步，需要等待子进程结束才会继续执行
    print("Ok")