#!/usr/bin/env python
# coding=utf-8
import Mail
import random
import urllib
import urllib2
import lxml
from bs4 import BeautifulSoup
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')

url = "http://www.smzdm.com/jingxuan/p1/"
#url = "http://www.baidu.com"
my_headers=["Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
            "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"]

def get_content(url,headers):
    random_header = random.choice(headers)
    request = urllib2.Request(url)
    request.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')
    #request.add_header('Host','http://www.smzdm.com/')
    #request.add_header('Referer','http://www.smzdm.com/')
    request.add_header('GET',url)

    content = urllib2.urlopen(request).read()
    return content

content =  get_content(url,my_headers)
soup = BeautifulSoup(content,'lxml')
List = soup.select('.feed-block-title')
str = ''
search = '冲锋衣'
for li in List:
    href = li.a.attrs['href']
    text = li.a.attrs['onclick'].split(':')[-1].strip(" ')}")
    if search in text:
        str += """<a style='text-decoration:none;color:#000;font-size:18px' target='_blank' href='%s'>
        %s
        <span style="font-color:red">
            %s
        <span>
    </a></br>
    """ % (href, text, li.a.span.string )
if str:
    Mail.sendMail(str)

    print(str)
