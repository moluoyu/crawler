#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'luoyu'
__mtime__ = '2020/5/22'
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
import logging
import re
import pymongo
from pyquery import PyQuery as pq
from urllib.parse import urljoin
from multiprocessing import Pool
from pprint import pprint

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s:%(message)s')
BASE_URL = 'https://static1.scrape.cuiqingcai.com'
TOTAL_PAGE = 1


def scrape_page(url):
    logging.info('%s', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        logging.error('get invalid status code %s while scraping %s', response.status_code, url)
    except requests.RequestException:
        logging.error('error occurred while scraping %s', url, exc_info=True)


def parse_index(html):
    doc = pq(html)
    links = doc('.el-card .name')
    for link in links.items():
        href = link.attr('href')
        detail_url = urljoin(BASE_URL, href)
        logging.info('get the detail url %s' % detail_url)
        yield detail_url


def scrape_index(page):
    index_url = f'{BASE_URL}/page/{page}'
    return scrape_page(index_url)


def scrape_detail(url):
    return scrape_page(url)


def parse_detail(html):
    doc = pq(html, timeout=120)
    cover = doc('img.cover').attr('src')
    name = doc('h2.m-b-sm').text()
    categories = doc('.categories span').text()
    move_info = doc('.info:contains(上映)').text()
    published_time = re.search(r'(\d{4}-\d{2}-\d{2})', move_info).group(1) if re.search(r'(\d{4}-\d{2}-\d{2})',
                                                                                        move_info) and move_info else None
    dram = doc('div.drama p').text()
    score = doc('p.score').text()
    score = float(score) if score else None
    return {
        'cover': cover,
        'name': name,
        'categories': categories,
        'published_at': published_time,
        'dram': dram,
        'score': score
    }


MOONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGO_DB_NAME = 'movies'
MONGO_COLLECTION_NAME = 'movies'
client = pymongo.MongoClient(MONGO_COLLECTION_NAME)
db = client['movies']
collection = db[MONGO_COLLECTION_NAME]


def save_data(data):
    collection.update_one({'name': data.get('name')}, {'$set': data}, upsert=True)


def main(page):
    page_index = scrape_index(page)
    detail_urls = parse_index(page_index)
    for detail_url in detail_urls:
        detail_html = scrape_detail(detail_url)  #
        movie_data = parse_detail(detail_html)  # 传入pyquery 如果是网站的url,则经常出现timeout,原因不明.
        logging.info('get movie detail data is %s', movie_data)
        logging.info('saving data to mongodb')
        save_data(movie_data)
        logging.info(' data saved successfully')


if __name__ == '__main__':
    pool = Pool()
    pages = range(1, TOTAL_PAGE + 1)
    pool.map(main, pages)
    pool.close()
    pool.join()
# res = parse_detail('https://static1.scrape.cuiqingcai.com/detail/1')
# pprint(res)
