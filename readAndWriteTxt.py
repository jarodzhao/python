
#读取文件内容
fp = open('jwt.txt', 'r', encoding='UTF-8')
print(fp.readlines())
fp.close()


#写入文件
test = '我的名字赵海涛...'
wp = open('chinavvv.txt', 'w', encoding='UTF-8')

#第一种写入文件方法
for i in range(1, 5):
	print(test + str(i), file=wp)

#另一种写入文件方法
wp.write('到这里结束！')

wp.close()

# help('open')