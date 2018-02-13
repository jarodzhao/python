import sqlite3

'''创建数据库并写入测试数据'''
def createDB():
	cursor = conn.execute('create table if not exists my (id int, name text, mobile text)')

	for i in range(1, 101):
		#参数化查询
		cursor.execute('insert into my values (?, "jarod zhao", "18625500030")', (i,))
	conn.commit()

	cursor.close()
	conn.close()

'''读取数据库中的所有记录'''
def loadItem():
	sql = 'select * from my'
	cursor = conn.execute(sql)

	for row in cursor:
		print(row, end='00\n')

if __name__ == '__main__':
	conn = sqlite3.connect('hello.db')
	# createDB()
	loadItem()