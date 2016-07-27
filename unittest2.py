import unittest

import mysql.connector


class test_place(unittest.TestCase):
    def test_chk(self):
        cnx = mysql.connector.connect(user='root', password='mysql', host='127.0.0.1', database='place')
        cursor =  cnx.cursor()
        query = """SELECT * FROM place"""
        cursor.execute(query)
#        data = cursor.fetchall()
        data = tuple(cursor)
        print data
        self.assertIsNotNone(tuple(data),(None))
        
suite = unittest.TestLoader().loadTestsFromTestCase(test_place)
unittest.TextTestRunner().run(suite)