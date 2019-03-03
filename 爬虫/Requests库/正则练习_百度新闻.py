import requests
import re
import fake_useragent
ua=fake_useragent.UserAgent()
url='http://news.baidu.com/'
header={
    "User-Agent":ua.random
}
response=requests.get(url,headers=header)

html=response.content.decode('utf-8')
pattern='<a href=(".*?")[ ]+target="_blank"[ ]+mon=".*?">(.*?)</a>'
result=re.findall(pattern,html)
with open('result.txt','w',encoding='utf-8') as f:
    for e in result:
        f.write("%s:%s\n"%(e[1],e[0]))