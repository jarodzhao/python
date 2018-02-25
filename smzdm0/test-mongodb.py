from pymongo import MongoClient

''' MongoDB 测试 '''
__author__ = 'jarod zhao'

'''
MongoDb 库名及表名
mydb.test.find()
'''

conn = MongoClient('127.0.0.1', 27017)
db = conn.mydb

db.test.insert({'name':'jarod zhao', 'mobile': '18625500030', 'email': '3245121@qq.com'})

mySet = db.test.find({'age':{'$lt':5}})		# age < 5 的记录

for s in mySet:
	print(s)
