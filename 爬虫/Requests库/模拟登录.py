import requests
from fake_useragent import UserAgent
ua=UserAgent()
login_url='https://www.yaozh.com/login'

header={
    'User-Agent':ua.random
}

session=requests.session()
session.headers=header
user='xiaoyao125656@sina.com'
pwd='789likai'
formhash='0C78326B24'
backurl='https%3A%2F%2Fwww.yaozh.com%2F'
login_data={
    'username':user,
    'pwd':pwd,
    'formhash':formhash,
    'backurl':backurl
}
session.post(url=login_url,data=login_data,verify=False) #取消ssl

data_url='https://www.yaozh.com/member/'

response=session.get(data_url)
data=response.content
with open("模拟登录.html",'w',encoding='utf-8') as f:
    f.write(data.decode('utf-8'))
print("Done")
