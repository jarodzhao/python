from dev import db

import pickle

dbfile = open('people-pickle', 'wb')		#写入模式打开

'通过 pickle 写入二进制的对象到文件'
pickle.dump(db, dbfile)						#写入操作
dbfile.close()

'通过 pickle 从文件中读取并还原对象'
if __name__ == '__main__':
	dbfile2 = open('people-pickle', 'rb')	#读取模式打开
	db = pickle.load(dbfile2)				#读取操作
	dbfile2.close()
	print(db)