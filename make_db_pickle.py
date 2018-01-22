from dev import db

import pickle

dbfile = open('people-pickle', 'wb')

'通过 pickle 写入二进制的对象到文件'
pickle.dump(db, dbfile)

dbfile.close()


if __name__ == '__main__':

	dbfile2 = open('people-pickle', 'rb')

	'通过 pickle 从文件中读取并还原对象'
	db = pickle.load(dbfile2)
	
	dbfile2.close()

	print(db)