from dev import jarod, bing

import shelve

#保存：使用 shelve 将对象保存到文件'
def make_db_shelve():
	db = shelve.open('people-shelve')
	db['jarod'] = jarod
	db['bing'] = bing
	db.close()

#还原：使用 shelve 还原文件中的对象
def dump_db_shelve():
	db = shelve.open('people-shelve')
	for key in db:
		print(key, '=>\n', db[key])
	db.close()

#更新：使用 shelve 更新对象
def update_db_shelve():
	db = shelve.open('people-shelve')

	jarod = db['jarod'] 	#还原对象
	jarod['pay'] += 15000	#更新内存中的对象
	db['jarod'] = jarod 	#更新数据库中的对象

	bing = db['bing']
	bing['pay'] -= 50000
	db['bing'] = bing
	db.close()

#模块启动方式打开时执行
if __name__ == '__main__':
	# update_db_shelve()
	dump_db_shelve()
	# make_db_shelve()