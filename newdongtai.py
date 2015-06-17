#!/usr/bin/python
#encoding:utf8
import re
import sys
import urllib2 as url 
import string
import urllib
import cookielib
from bs4 import BeautifulSoup

def getList(regex,text):
    ''' 
    输入：正则表达式，文本
    输出：匹配到的数组(默认使用findall匹配)
    '''
    arr = []
    res = re.findall(regex, text)
    if res:
        for r in res:
            arr.append(r)
    return arr 

def getShopHtml(shop_url):
    cj = cookielib.CookieJar()
    opener=url.build_opener(url.HTTPCookieProcessor(cj))
    opener.addheaders = [('User-agent', 'Opera/9.23')]
    url.install_opener(opener)
    req=url.Request(shop_url)
    response =url.urlopen(req)
    html = response.read().decode('gbk')
    return html

def main():
	s1 = "http://shoucang.taobao.com/shop_gallery_n.htm?spm=a1z0k.7386009.1997989141.d4919229.bmVuvX&id=113752575&cat=7&sellerId=378087038"
	shop_html = getShopHtml(s1)
	print shop_html

    #注意要用非贪婪匹配
    goods_details = getList(u"<a data-spm=\"d4909061\"[\s\S]*?href=\"(.*?)\"[\s\S]*?title=\"(.*?)\"[\s\S]*?target", str(shop_html.encode('utf-8')).strip() )
    for gd in goods_details:
        print "link=%s, title=%s" %(gd[0], gd[1] )

if __name__ == '__main__':
    main()
