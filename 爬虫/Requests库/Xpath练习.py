import requests
from lxml import etree
from fake_useragent import UserAgent
ua=UserAgent()
class BtcSpider:
    def __init__(self):
        self.baseurl='http://8btc.com/forum-61-'
        self.index=1
        self.session=requests.session()
        self.session.headers={
            'User-Agent':ua.random
        }
    def getdata(self):
        url=self.baseurl+'%s.html'%self.index
        response=self.session.get(url)
        data=response.content.decode('gbk')
        return data
    def parsedata(self,data):
        x_data=etree.HTML(data)
        title_list=x_data.xpath('//a[@class="s xst"]/text()')
        url_list=x_data.xpath('//a[@class="s xst"]/@href')
        parse_data=list(zip(title_list,url_list))
        return parse_data
    def savedata(self,data):
        with open("result.txt",'a') as f:
            for e in data:
                f.write('%s : %s\n'%(e[0],e[1]))
    def run(self):
        num=int(input("请输入需要抓取的页数:").strip())
        count=0
        for i in range(num):
            data=self.getdata()
            parsedata=self.parsedata(data)
            self.savedata(parsedata)
            count+=len(parsedata)
            print("%d页抓取完成共计%d数据"%(self.index,count))
            self.index+=1
        print("Done!")
if __name__=='__main__':
    BtcSpider().run()
