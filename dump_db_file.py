

from make_db_file import loadDbase

db = loadDbase()

db['jarod']['pay'] += 15000

for key in db:
	print(key, '=>\n ', db[key])
# print(db['jarod']['pay'])