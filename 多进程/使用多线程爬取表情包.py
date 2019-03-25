import requests
from lxml import etree
import os
from queue import Queue
import re
import threading
from urllib import request
class Producer(threading.Thread):
    def __init__(self,page_queue,img_queue):
        super().__init__()
        self.page_queue=page_queue
        self.img_queue=img_queue
        self.session=requests.session()
        self.session.headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    def run(self):
        while 1:
            if self.page_queue.empty():
                break
            self.page_parse(self.page_queue.get())
    def page_parse(self,page):
        html=etree.HTML(self.session.get(page).content.decode('utf-8'))
        imgs=html.xpath('//div[@class="page-content text-center"]//img[@class!="gif"]')
        for e in imgs:
            img=e.get('data-original')
            suffix=os.path.splitext(img)[1]
            filename=e.get('alt')
            filename=re.sub(r'[\/:*?"<>|]','',filename)
            filename=filename+suffix
            # print(filename)
            self.img_queue.put((img,filename))
class Consumer(threading.Thread):
    def __init__(self,page_queue,img_queue):
        super().__init__()
        self.img_queue=img_queue
        self.page_queue=page_queue

    def run(self):
        while 1:
            if self.img_queue.empty() and self.page_queue.empty():
                break
            url,filename=self.img_queue.get()
            request.urlretrieve(url,'Images/'+filename)
            print(filename+" Done!")


if __name__ == '__main__':
    page_queue=Queue(100)
    img_queue=Queue(500)
    for i in range(100):
        url="https://www.doutula.com/photo/list/?page={}".format(i+1)
        page_queue.put(url)
    for i in range(5):
        Producer(page_queue,img_queue).start()
    for i in range(5):
        Consumer(page_queue,img_queue).start()