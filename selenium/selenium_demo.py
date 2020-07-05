#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'luoyu'
__mtime__ = '2020/6/18'
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
import json
from urllib.parse import urljoin
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import logging
from os import makedirs
from os.path import exists
logging.basicConfig(level=logging.INFO,format='%(asctime)s-%(levelname)s:%(message)s')
INDEX_URL = 'https://dynamic2.scrape.cuiqingcai.com/page/{page}'
TIME_OUT = 20
TOTAL_PAGE = 10
options = webdriver.ChromeOptions()
options.add_argument('--headless')
brower = webdriver.Chrome(options=options)
wait = WebDriverWait(brower,TIME_OUT)
RESULT_DIR='results'
exists(RESULT_DIR) or makedirs(RESULT_DIR)


def scrape_page(url,condition,locator):
    logging.info('scraping%s',url)
    try:
        brower.get(url)
        wait.until(condition(locator))
    except TimeoutException:
        logging.error('error occurred while scraping %s',url,exc_info=True)

def scrape_index(page):
    url = INDEX_URL.format(page=page)
    scrape_page(url,EC.visibility_of_all_elements_located,locator=(By.CSS_SELECTOR,'#index .item'))

def parse_index():
    elements = brower.find_elements_by_css_selector('#index .item .name')
    for element in elements:
        href = element.get_attribute('href')
        yield urljoin(INDEX_URL,href)

def scrape_detail(url):
    scrape_page(url,EC.visibility_of_element_located,locator=(By.TAG_NAME,'h2'))


def parse_detail():
    url = brower.current_url
    name = brower.find_element_by_tag_name('h2').text
    categories = [element.text for element in brower.find_elements_by_css_selector('.categories button span')]
    cover = brower.find_element_by_tag_name('img').get_attribute('src')
    score = brower.find_element_by_css_selector('.score').text
    drama = brower.find_element_by_css_selector('.drama p').text
    return {'url':url,
            'name':name,
            'categories':categories,
            'cover':cover,
            'score':score,
            'drama':drama
            }


def save_data(data):
    name = data.get('name')
    data_path = f'{RESULT_DIR}/{name}.json'
    exists(data_path) or json.dump(data,open(data_path,'wt',encoding='utf-8'),ensure_ascii=False,indent=2)



if __name__ == '__main__':
    try:
        for page in range(1, TOTAL_PAGE + 1):
            scrape_index(page)
            detail_urls = parse_index()
            for detail_url in list(detail_urls): #不能对generator 进行for
                logging.info('get detail is %s',detail_url)
                scrape_detail(detail_url)
                detail_data = parse_detail()
                save_data(detail_data)
                logging.info('detail_data is %s',detail_data)
    finally:
        brower.close()
