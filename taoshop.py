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
    ''' 这个链接抓不到动态
    shop_url = "http://mukwo.taobao.com/dongtai.htm"
    shop_html = getShopHtml(shop_url)
    '''
    s1 = "http://dongtai.taobao.com/microshop/front.htm?shopOwnerId=47195748&_tb_token_=ATMrAIvJ54hE&tracelog=shop_middle_page"
    shop_html = getShopHtml(s1)
    #print shop_html

    '''
    <a data-spm="d4909061"  href="http://item.taobao.com/item.htm?id=38223338865"
    title="14年 5月 小布 blythe Ashley&#39;s Secret 预订 订金" target="_blank">
    '''
    #注意要用非贪婪匹配
    goods_details = getList(u"<a data-spm=\"d4909061\"[\s\S]*?href=\"(.*?)\"[\s\S]*?title=\"(.*?)\"[\s\S]*?target", str(shop_html.encode('utf8')).strip() )
    for gd in goods_details:
        print "link=%s, title=%s" %(gd[0], gd[1] )

if __name__ == '__main__':
    main()
