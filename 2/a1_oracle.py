import cx_Oracle as oracle
import datetime

conn = oracle.connect("zc_sczh/zc_sczh@localhost:1521/orcl")
cursor = conn.cursor()

sql = "select tablespace_name, file_name from dba_data_files"
rows = cursor.execute(sql)

for row in rows:
	tablespace_name = row[0]
	file_name = row[1]
	print(tablespace_name + "    -    " + file_name)

conn.close()

print(datetime.datetime.now())
