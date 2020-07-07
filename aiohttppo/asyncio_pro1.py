#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'luoyu'
__mtime__ = '2020/7/4'
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
import asyncio
import json

import aiohttp
import logging
from motor.motor_asyncio import AsyncIOMotorClient


logging.basicConfig(level=logging.INFO, format='%(asctime)s-%(levelname)s:%(message)s')
INDEX_URL = 'https://dynamic5.scrape.cuiqingcai.com/api/book/?limit=18&offset={offset}'
DETAIL_URL = 'https://dynamic5.scrape.cuiqingcai.com/api/book/{id}'
PAGE_SIZE = 18
CONCURRENCY = 10
PAGE_NUMBER = 100

MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGO_DB_NAME = 'books'
NONGO_COLLECTION_NAME = 'books'
client = AsyncIOMotorClient(MONGO_CONNECTION_STRING)
db = client[MONGO_DB_NAME]
collection = db[NONGO_COLLECTION_NAME]



semaphore = asyncio.Semaphore(CONCURRENCY)
session = None


async def scrape_index(page):
    url = INDEX_URL.format(offset=((page - 1) * PAGE_SIZE))
    return await scrape_api(url)


async def scrape_api(url):
    async with semaphore:
        try:
            logging.info('scraping %s', url)
            async with session.get(url) as response:
                return await response.json()
        except aiohttp.ClientError:
            logging.error('error occurred while scraping %s', url, exc_info=True)



async def sava_data(data):
    logging.info('saving data %s',data)
    if data:
        return await collection.update_one({
            'id':data.get('id')
        },{
            '$set':data
        },upsert=True)


async def scrape_detail(id):
    detail_url = DETAIL_URL.format(id=id)
    data = await scrape_api(detail_url)
    await sava_data(data)




async def main():
    global session
    ids = []
    session = aiohttp.ClientSession()
    scrape_index_tasks = [asyncio.ensure_future(scrape_index(page)) for page in range(1, PAGE_NUMBER + 1)]
    result = await asyncio.gather(*scrape_index_tasks)
    logging.info('result %s', json.dumps(result, ensure_ascii=False, indent=2))


    for index_data in result:
        if not index_data: continue
        for item in index_data.get('results'):
            ids.append(item.get('id'))
    scrape_detail_tasks = [asyncio.ensure_future(scrape_detail(id)) for id in ids]
    await asyncio.wait(scrape_detail_tasks)
    await session.close()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
