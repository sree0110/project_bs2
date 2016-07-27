import json
import urllib2
import demjson
import mysql.connector
from mysql.connector import Error



response = urllib2.urlopen("http://freegeoip.net/json/50.78.253.58").read().decode("utf-8")
responseJson = json.loads(response)
print(responseJson)
l = responseJson.items()
print l

# for key in responseJson:
#     diction = (key , "  :: " ,responseJson[key])
#     print diction
    
query = "INSERT INTO place(params,details) VALUES(%s,%s)"
try:
    conn = mysql.connector.connect(host='localhost', database='place', user='root', password='mysql')
    cursor = conn.cursor()
    cursor.executemany(query, l)
    conn.commit()
    cursor.close()
    conn.close()
except Error as e:
    print('Error:', e)