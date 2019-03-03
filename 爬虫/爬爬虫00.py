import urllib.request

def my_handle(url):
    #不含代理的基本handle
    handle=urllib.request.HTTPHandler()
    opener=urllib.request.build_opener(handle)
    response=opener.open(url)
    data=response.read()
    return data.decode('utf-8')
def my_proxyhandle(url):
    #可添加代理版
    proxy={
        "http":"121.61.25.128:9999"
    }
    handle=urllib.request.ProxyHandler(proxy)
    opener=urllib.request.build_opener(handle)
    opener.addheaders={('User-agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0')}
    response=opener.open(url)
    data = response.read()
    return data.decode('utf-8')
# with open('htmls/0.html','w',encoding='utf-8') as f:
#     f.write(my_handle('http://www.baidu.com/'))
#     print("Done")
with open('htmls/0_proxy.html','w',encoding='utf-8') as f:
    f.write(my_proxyhandle('http://httpbin.org/ip'))
    print('done')


