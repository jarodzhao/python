import cgi

form = cgi.FieldStorage()

print('Content-type: text/html\n')
print('<title>Reply Page</title>')

if not 'user' in form:
	print('<h1>你是谁？</h1>')
else:
	print('%s' % cgi.escape(form['user'].value))