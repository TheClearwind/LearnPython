from multiprocessing import Process
from time import sleep
import os
def func():
    print(os.getppid())
    sleep(5)
    print(123456)
if __name__=='__main__': #必须写否则报错
    print(os.getpid())
    print("父进程",os.getppid())
    Process(target=func).start()
    print('-'*10)