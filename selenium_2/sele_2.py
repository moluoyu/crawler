#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'luoyu'
__mtime__ = '2020/6/26'
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
import requests
import time
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s-%(levelname)s:%(message)s')
TOTAL_PAGES = 100
BASE_URL = 'https://static4.scrape.cuiqingcai.com/{id}'


start_time = time.time()
for id in range(1,TOTAL_PAGES + 1):
    url = BASE_URL.format(id=id)
    logging.info('scraping url is %s',url)
    response = requests.get(url)
end_time = time.time()
logging.info('total time is %s seconds',end_time - start_time)

