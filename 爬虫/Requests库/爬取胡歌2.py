import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import os
ua=UserAgent()
class HugeSpider:
    def __init__(self):
        self.url='http://www.5857.com/tag_huge.html'
        self.session=requests.session()
        self.session.headers={
            'User-Agent':ua.random
        }
        self.savepath='result/{}.jpg'
        self.imgIndex=0
    def getdata(self,url):
        response = self.session.get(url)
        data=response.content.decode('utf-8')
        return data
    def parsedata(self,data):
        soup=BeautifulSoup(data,'lxml',from_encoding='utf-8')
        contents=soup.select('.listbox')
        imgs=[content.select_one('a') for content in contents]
        for e in imgs:
            url=e['href']
            #print(url)
            res=self.getdata(url)
            soup2=BeautifulSoup(res,'lxml',from_encoding='utf-8')
            img_box=soup2.select_one('.img-box')
            if img_box==None:
                continue
            else:
                imglist=img_box.select('img')
            for e in imglist:
                img_url=e['src']
                print(img_url)
                if img_url.find('chat')!=-1:
                    continue
                img=self.session.get(img_url).content
                self.saveimg(img)
    def saveimg(self,img):
        with open(self.savepath.format(self.imgIndex),'wb') as f:
            f.write(img)
            self.imgIndex+=1
    def run(self):
        if not os.path.exists('result/'):
            os.makedirs('result')
        data=self.getdata(self.url)
        self.parsedata(data)
        print('Done')
HugeSpider().run()


