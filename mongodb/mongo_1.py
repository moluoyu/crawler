#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'luoyu'
__mtime__ = '2020/5/20'
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
import pymongo
client = pymongo.MongoClient(host='localhost',port=27017)
db = client.test
collection = db.students
student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
student2 = {
    'id': '20170102',
    'name': 'Jordan',
    'age': 22,
    'gender': 'male'
}
condition = {'age':27}
students = collection.delete_one(condition)
# students['age'] = 26
# result =collection.update_one(condition,{'$inc':{'age':1}})
print(students.deleted_count)
# print(result.matched_count,result.modified_count)