import requests
from bs4 import BeautifulSoup
import json
from lxml import etree
from fake_useragent import UserAgent
ua=UserAgent()
class BooksSpider:
    def __init__(self):
        self.baseurl='http://www.allitebooks.com/page/{}'
        self.session=requests.session()
        self.session.headers={"User-Agent":ua.random}

    def getdata(self,index):
        url=self.baseurl.format(index)
        response=self.session.get(url)
        return response.content.decode('utf-8')

    def parsedata_xpath(self,data):
        xdate=etree.HTML(data)
        booklist=xdate.xpath('//div[@class="main-content-inner clearfix"]/article')
        for book in booklist:
            bookName=book.xpath('.//h2[@class="entry-title"]/a/text()')[0]
            bookAuth=book.xpath('.//h5[@class="entry-author"]/a/text()')[0]
            bookSummary=book.xpath('.//div[@class="entry-summary"]/p/text()')[0]
            bookImage=book.xpath('.//div[@class="entry-thumbnail hover-thumb"]//img/@src')[0]
            print(bookImage)

    def parsedata_bs4(self,data):
        bs4_data=BeautifulSoup(data,'lxml',from_encoding='utf-8')
        booklist=bs4_data.find_all('article')
        for book in booklist:
            bookName = book.select_one('.entry-title').get_text()
            bookAuth = book.select_one('.entry-author').get_text()
            bookSummary = book.select_one('.entry-summary').get_text()
            bookImage = book.select_one('.attachment-post-thumbnail')['src']
            print(bookSummary)

    def savedata(self):
        pass

    def run(self):
        data=self.getdata(1)
        #self.parsedata_xpath(data)
        self.parsedata_bs4(data)
        #num=int(input("请输入需要抓取的页数:").strip())
        count=0

        # for i in range(num):
        #     pass

if __name__=="__main__":
    BooksSpider().run()