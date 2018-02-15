from pymongo import MongoClient

''' MongoDB 测试'''
__author__ = 'jarod zhao'

conn = MongoClient('127.0.0.1', 27017)
db = conn.mydb

my_set = db.test

#遍历所有文档
for item in my_set.find():
	print(item)

print()

#条件查询文档
for item in my_set.find({'name': '赵天玮'}):
	print(item)

#循环插入100条文档记录
for i in range(100):
	i += 1
	my_set.insert({'name':'hello' + str(i), 'age':i})