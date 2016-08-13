#!/usr/bin/python
#coding:utf-8
#作者：Byron
#博客：http://jiabin.tk
 
import urllib.request
import re
import time

#定义程序主函数
def qiubai(page):
    url = "http://www.qiushibaike.com/hot/page/%d/?s=4901659" % page
    print('url=' + url)
    re_qb = re.compile(r'<div\s*class="content">(.*?)</div>',re.DOTALL)
    requestData = urllib.request.Request(url=url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:10.0.1) Gecko/20100101 Firefox/10.0.1'})
    html = urllib.request.urlopen(requestData).read().decode('utf-8')
    #print(html)
    my_qiubai = re_qb.findall(html)
    n = len(my_qiubai)
    for i in range(0,n,3):
        for j in range(3):
            if(i*3+j<n):
                print("-" * 40)
                print (my_qiubai[i*3+j].replace('<br/>','\r\n'))

#定义程序循环体
def for_qb():
    for page in range(int(p),280):
        print ("-" * 18 + "第" + str(page) + "页" + "-" * 18)
        try:
            qiubai(page)
        except Exception as e:
            print(e)
        time.sleep(10)
 
#该部分代码的目是为了设计的严谨，尽可能的使程序不发生崩溃
def if_qb():
    global p
    p = input("输入要看的页数1~280:")
    if p == "q":
        exit()
    elif not p.isdigit() or p == "0" or int(p) > 280:
        if_qb()
    else:
        for_qb()
print("-" * 40)
print("糗百命令行版——Byron")
print("一入糗百深似海，从此节操是路人")
print('输入"q"退出程序')
print("-" * 40)
 
if_qb()
