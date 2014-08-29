#!/usr/bin/python
#encoding:utf8
import re
import time
import sys
import urllib2 as url 
import string
import urllib
import cookielib
from commom.mailman import sendEmailByDefault

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
    has = "tb-btn-buy" #有货的显示tobuy
    g1 = "http://item.taobao.com/item.htm?spm=2013.1.0.0.qJBnOc&scm=1007.10010.1402.0&id=40162868536"
    out = "tb-key tb-out-of-date tb-key-off-sale" # 无货的
    g2 = "http://item.taobao.com/item.htm?id=40885368993&_fb=MWQwOWo0fDExaTczfDNwfDExNzk3Njk5MzkzfGcwZnwwYjQ4MDE%3D&spm=a1z10.10.w4039-3617802373.4.Xj0eum"
    g3 = "http://item.taobao.com/item.htm?id=40848475546&spm=a310v.4.88.1"

    f=open('run.log','a+')
    counter = 0
    for gs in (g2, g3):
        goods_html = getShopHtml(gs)
        #print goods_html
        shop = ""
        if counter == 0 :
            print >> f , "wakong >>>>>>>>>"
            shop = "wakong"
        else:
            print >> f, "maybedoll >>>>>>>>>"
            shop = "maybe doll"
        print >> f, time.strftime('%Y-%m-%d %X', time.localtime() )    
        if has in str(goods_html.encode('utf8')):
            
            print >> f, "has go to buy" 
            sendEmailByDefault("上新啦，快抢！！！" + shop, "上新啦，快抢！！！" + shop, "上新啦，快抢！！！" + shop)
        else:
            print >> f, "sell out" 
            sendEmailByDefault("::>_<:: " + shop, "::>_<:: " + shop, "::>_<:: " + shop)
        counter += 1
    
    f.close()
if __name__ == '__main__':
    main()
