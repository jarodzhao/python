import getSMZDM as zdm
import time, datetime
import sqlite3
from smzdm.faxian import FaxianItem as Item

item = Item
item.title = '苏泊尔 CFXB40HC3T-120 球釜IH电磁加热电饭煲4L 智能电饭锅家用3-5-6人'

# item.time_ = '09:11'

# print(zdm.has_item(item))



conn = sqlite3.connect('smzdm.db')
cursor = conn.cursor()

sql = "select * from faxian where title = ?"
result = cursor.execute(sql, (item.title,)).fetchall()   #一个坑，不调用 fetchall() 方法，返回的数量始终为 -1

print(result)
# try:
#     result = cursor.execute(sql, (item.title)).fetchall()   #一个坑，不调用 fetchall() 方法，返回的数量始终为 -1
#     if len(result) > 0:
#         print(1)
# except:
# 	print(0)
#     # pass    #首次运行时会引发异常，找不到表（刚刚建的库，没有表！）
# finally:
conn.close()


