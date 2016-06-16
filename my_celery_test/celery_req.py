#!/usr/bin/python
# coding: utf-8

"""
先开启 redis-server
需cd至该文件目录下
celery worker -A celery_req -l info
最后 运行该文件
http://www.cnblogs.com/oneapm/p/4772154.html
"""


import time

import requests
from celery import Celery

# 也可在调用其他机器的redis 'redis://192.168.240.1' 这是虚拟机的celery调用本机
app = Celery('celery_req', broker='redis://localhost:6379')


@app.task
def get_it(url):
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    
    }
    rsp = requests.get(url, headers=HEADERS)
    print rsp.status_code

def hand(urls):
    s = time.time()
    for url in urls:
        get_it.delay(url)

    print 'using time:', time.time()-s

    
if __name__ == '__main__':
    urls = [
        'http://www.baidu.com',
        'http://www.huxiu.com',
        'http://www.zhihu.com',
        'http://www.lagou.com',
    ]
    hand(urls)
