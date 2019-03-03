import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import os
ua=UserAgent()
class HugeSpider:
    def __init__(self):
        self.url='http://www.kuyv.cn/star/huge/photo/{}/'
        self.session=requests.session()
        self.session.headers={
            'User-Agent':ua.random
        }
        self.savepath='result/{}.jpg'
        self.imgIndex=0
    def getdata(self,index):
        full_url=self.url.format(index)
        response = self.session.get(full_url)
        data=response.content.decode('utf-8')
        return data
    def parsedata(self,data):
        soup=BeautifulSoup(data,'lxml',from_encoding='utf-8')
        contents=soup.select('.picimg')
        imgs=[content.select_one('img') for content in contents]
        for e in imgs:
            url=e['src']
            img=self.session.get(url).content
            self.saveimg(img)
    def saveimg(self,img):
        with open(self.savepath.format(self.imgIndex),'wb') as f:
            f.write(img)
            self.imgIndex+=1
    def run(self):
        if not os.path.exists('result/'):
            os.makedirs('result')
        for i in range(1,31):
            data=self.getdata(i)
            self.parsedata(data)
            print("第%d页完成！"%i)
        print('Done')
HugeSpider().run()


