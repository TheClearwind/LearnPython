import requests

header={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

url='https://ip8.com/'
proxy={
    'https':'222.94.148.114:3128'
}
response=requests.get(url,proxies=proxy)
data=response.content
print(data.decode('utf-8'))