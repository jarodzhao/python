from dev import jarod, bing

import pickle

# 将对象的字节流写入文件
for(key, record) in [('jarod', jarod), ('bing', bing)]:
	recfile = open(key + '.pkl', 'wb')
	pickle.dump(record, recfile)
	recfile.close()

