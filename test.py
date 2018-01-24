import shelve

def ins():
	tt = shelve.open('test')
	tt['a'] = 'aaa'
	tt['b'] = 'bbb'
	tt.close()

def lod():
	tt = shelve.open('test')
	print(tt)
	print(tt['b'])
	tt.close()


lod()