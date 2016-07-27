from urllib2 import request, parse
url = "http://httpbin.org/get"
parms={ 'name1' : 'value1',  'name2' : 'value2' }
qrystr = parse.urlencode(parms)
u = request.urlopen(url + '?' + qrystr)
resp = u.read()
print(resp)