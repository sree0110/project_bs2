import unittest
from sql_data1 import responseJson
from sql_data1 import l
from sql_data1 import query
import mysql.connector

class OutcomesTest(unittest.TestCase):
    def setUp(self):
        print ("executing setup")

    def test_responseJson(self):
        x = [(u'city', u'North Chelmsford'), (u'region_code', u'MA'), (u'region_name', u'Massachusetts'), 
             (u'ip', u'50.78.253.58'), (u'time_zone', u'America/New_York'), (u'longitude', -71.3888), 
             (u'metro_code', 506), (u'latitude', 42.632), (u'country_code', u'US'), (u'country_name', u'United States'),
              (u'zip_code', u'01863')]
        l = responseJson.items()
        self.assertEqual(x,l)
       
       
    def test_chk(self):
        cnx = mysql.connector.connect(user='root', password='mysql', host='127.0.0.1', database='place')
        cursor =  cnx.cursor()
        query = """SELECT * FROM place"""
        cursor.execute(query)
#        data = cursor.fetchall()
        data = tuple(cursor)
        print data
        self.assertIsNotNone(tuple(data),(None))  
       
    

    def tearDown(self):
        print ("Executing tearDown")
        
suite = unittest.TestLoader().loadTestsFromTestCase(OutcomesTest)
unittest.TextTestRunner().run(suite)
