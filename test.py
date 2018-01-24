<<<<<<< HEAD
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
=======
import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = '.'
port = 80

os.chdir(webdir)
srvraddr = ('', port)
srvrobj = HTTPServer(srvraddr, CGIHTTPRequestHandler)
srvrobj.serve_forever()
>>>>>>> 7285b261a8d8b20f0acde41160b8054df7f42a8a
