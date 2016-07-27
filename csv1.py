import json

import csv

import urllib2


ip_data = urllib2.urlopen("http://freegeoip.net/json/50.78.253.58").read().decode("utf-8")
responseJson = json.loads(ip_data)
#print responseJson

# open a file for writing

responseJson = open(', 'w')
# create the csv writer object

csvwriter = csv.writer(responseJson)

count = 0

for i in ip_data:

      if count == 0:

             header = ip.keys()

             csvwriter.writerow(header)

             count += 1

      csvwriter.writerow(place.values())

responseJson.close()
