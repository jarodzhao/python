from urllib import request

url = 'http://125.46.33.20:8011/sysadmin'

response = request.urlopen(url)
html = response.read()

fp = open('sysadmin.html', 'w+b')
fp.write(html)
fp.close()

# help(response)
print(response.geturl())
