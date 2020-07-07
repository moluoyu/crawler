#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'luoyu'
__mtime__ = '2020/7/7'
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
from pyppeteer import launch
from pyquery import PyQuery as pq
async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://dynamic2.scrape.cuiqingcai.com/')
    await page.waitForSelector('.item .name')
    doc = pq(await page.content())
    names = [item.text() for item in doc('.item .name').items()]
    print('names:',names)
    await browser.close()
    asyncio.get_event_loop().run_until_complete(main())