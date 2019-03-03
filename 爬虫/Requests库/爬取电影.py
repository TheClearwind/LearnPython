import requests
import json
import pandas
from fake_useragent import UserAgent
ua=UserAgent(verify_ssl=False)

class MovieSpider:
    def __init__(self):
        self.baseUrl='http://www.cbooo.cn/BoxOffice/getCBW?pIndex={0}&dt={1}'
        self.session=requests.session()
        self.session.headers={
            'User-Agent':ua.random
        }
    def getData(self,index,id):
        url=self.baseUrl.format(index,id)
        r=self.session.get(url).content
        if len(r)==0:
            return
        response=json.loads(r)
        data=response["data1"]
        return data
    def savedata(self,data):
        data.to_csv('result.csv',encoding='gb2312')
        print("Done")
    def run(self):
        index=1
        df=None
        while 1:
            data=self.getData(index,1040)
            if data==None:
                self.savedata(df)
                break
            data_frame=pandas.DataFrame.from_dict(data)
            if df is None:
                df=data_frame
            else:
                df=df.append(data_frame)
            index+=1
MovieSpider().run()