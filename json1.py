import json
import urllib2
import demjson


response = urllib2.urlopen("http://freegeoip.net/json/50.78.253.58").read().decode("utf-8")
responseJson = json.loads(response)
print responseJson

for key in responseJson:
    print (key , "  :: " ,responseJson[key])
# d = demjson.decode(responseJson,strict=False)
# print (d)


