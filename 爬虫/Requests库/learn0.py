import requests
import sys
url='https://baidu.com'
response=requests.get(url)
data=response.content
with open('r_0.html','w',encoding='utf-8') as f:
    f.write(data.decode('utf-8'))
print("Done")