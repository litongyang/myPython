import requests
from lxml import etree

url = "https://www.lexico.com/list/0/2?locale=en"
headers = {'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
               'Accept - Encoding':'gzip, deflate',
               'Accept-Language':'zh-Hans-CN, zh-Hans; q=0.5',
               'Connection':'Keep-Alive',
               'Host':'zhannei.baidu.com',
               'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
r = requests.get('http://zhannei.baidu.com/cse/search', headers=headers, timeout=3)
reqs = requests.get(url)
html = etree.HTML(reqs.text)

# item=html.xpath('//*[@id="content"]/div[1]/div[2]/div/div/div/div[2]/ul/li[263]/a')
item=html.xpath('//*[@id="content"]/div[1]/div[2]/div/div/div/div[2]/ul/li[2]/a')
print len(item)
for i in item:
    print i.text



