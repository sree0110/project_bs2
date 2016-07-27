import csv
import json
import urllib2

ip_data = urllib2.urlopen("http://freegeoip.net/json/50.78.253.58").read().decode("utf-8")
responseJson = json.loads(ip_data)

f = open("place_data.csv", 'w+')
try:
    writer = csv.writer(f) 
    writer.writerow(('parameters', 'details'))
    for k,v in responseJson.iteritems():
        print k,v
        writer.writerow((k,v))
finally:
   f.close()
