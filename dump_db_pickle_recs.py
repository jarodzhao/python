import pickle, glob

#循环载入所有 pkl 类型文件
#还原文件到对象并输出
for filename in glob.glob('*.pkl'):
	recfile = open(filename, 'rb')
	record = pickle.load(recfile)
	print(filename , "=>\n", record)

#示例
jarodfile = open('jarod.pkl', 'rb')
print(pickle.load(jarodfile)['pay'])