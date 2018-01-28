# import cgi
#
# form = cgi.FieldStorage()
#
print('Content-type: text/html\n')
# print('<title>Reply Page</title>')
#
# if not 'user' in form:
# 	print('<h1> there is not anyone!</h1>')
# else:
# 	print('%s' % cgi.escape(form['user'].value))

import json, shelve
db = shelve.open('people-shelve')
jarod = db['jarod']
jarod_json = json.dumps(jarod)
print(jarod_json)
db.close()
