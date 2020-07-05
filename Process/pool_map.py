#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'luoyu'
__mtime__ = '2020/5/5'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
 """
from multiprocessing import Process,Pool
import urllib.request
import urllib.error

def scrape(url):
    try:
        urllib.request.urlopen(url)
        print(f'{url} was Scraped')
    except (urllib.error.HTTPError, urllib.error.URLError):
        print(f'{url} was failed')


if __name__ == '__main__':
    pool = Pool(processes=3)
    urls = [
        "https://www.baidu.com/",
        "http://www.meituan.com/",
        "http://blog.csdn.net",
        "http://xxy.net"
    ]
    pool.map(scrape,urls)
    pool.close()

