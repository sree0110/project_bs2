import urllib2
from bs4 import BeautifulSoup
import unittest

class TestWikipedia(unittest.TestCase):
    bsObj = None
    def setUpClass():
        global bsObj
        url = "http://en.wikipedia.org/wiki/Monty_Python"
        bsObj = BeautifulSoup(urllib2.urlopen(url),"html.parser")
    def test_titleText(self):
        global bsObj
        pageTitle = bsObj.find("h1").get_text()
        self.assertEqual("Monty Python", pageTitle);
    def test_contentExists(self):
        global bsObj
        content = bsObj.find("div",{"id":"mw-content-text"})
        self.assertIsNotNone(content)
  

suite = unittest.TestLoader().loadTestsFromTestCase(TestWikipedia)
unittest.TextTestRunner().run(suite)


