import time, datetime, random
import sqlite3

# 精选频道

item = Item
item.title = 'IPASON/攀升 AMD A8 7650K四核集显组装台式电脑主机游戏DIY整机'

conn = sqlite3.connect('smzdm.db')
cursor = conn.cursor()

sql = "select first from faxian where title = ?"
result = cursor.execute(sql, (item.title,)).fetchall()

if len(result) > 0 and result[0][0] == 1:                       #坑二，不调用 fetchall() 方法，返回的数量始终为 -1
    print(2)
elif len(result) > 0:
    print(1)
else:
	print(0)

conn.close()


# try:
#     result = cursor.execute(sql, (item.title,)).fetchall()          #坑一，使用占位符，记得在值后面加 ,
#     if len(result) > 0 and result[0][0] == 1:                       #坑二，不调用 fetchall() 方法，返回的数量始终为 -1
#         return 2
#     else: 
#         return 1
# except:
#     pass    #首次运行时会引发异常，找不到表（刚刚建的库，没有表！）
# finally:
#     conn.close()

# print(zdm.has_item(item))