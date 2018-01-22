# 开始学习 python

jarod = {'name':'jarod zhao', 'age':38, 'pay':45000, 'job':'dev'}
bing = {'name':'bing chen', 'age':34, 'pay': 150000, 'job':'sale'}

db = {}
db['jarod'] = jarod
db['bing'] = bing

if __name__ == '__main__':
	for key in db:
		print(key, '=>\n', db[key])