import threading
import random
import time
gmoney=1000
gTotalTimes = 5
gTimes = 0
gcondition=threading.Condition()

class Producer(threading.Thread):
    def run(self):
        global gmoney, gTimes, gTotalTimes
        while gTimes<gTotalTimes:
            money=random.randint(100,1000)
            gcondition.acquire()
            gmoney+=money
            print("生成了%d元,剩余%d元"%(money,gmoney))
            gTimes+=1
            gcondition.notify_all() #唤醒所有等待的线程
            gcondition.release()
            time.sleep(0.5)
class Consumer(threading.Thread):
    def run(self):
        global gmoney, gTimes, gTotalTimes
        while 1:
            money = random.randint(100, 1000)
            gcondition.acquire()
            while gmoney<money:
                if gTimes>=gTotalTimes:
                    gcondition.release()
                    return
                print("%s预计消费%d元剩余%d元,不足!"%(threading.current_thread(),money,gmoney))
                gcondition.wait()
            gmoney-=money
            print("%s消费%d元剩余%d元!" % (threading.current_thread(),money, gmoney))
            gcondition.release()

if __name__ == '__main__':
    Producer().start()
    for i in range(3):
        Consumer(name="消费者%d"%i).start()

