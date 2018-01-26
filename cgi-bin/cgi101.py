import cgi

form = cgi.FieldStorage()

print('Content-type: text/html\n')
print('<title>Reply Page</title>')

u = '你是谁？'

if not 'user' in form:
	print('<h1>' + u.decode('GBK') + </h1>')
else:
	print('%s' % cgi.escape(form['user'].value))


	