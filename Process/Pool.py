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
from multiprocessing import Process, Pool
import time


def function(index):
    print(f'Start process:{index}')
    time.sleep(3)
    print(f'End process {index}')


if __name__ == '__main__':
    pool = Pool(3)
    for i in range(4):
        pool.apply_async(function, args=(i,))

    print('Main Process started')
    pool.close()
    pool.join()
    print('Main Process Ended')

