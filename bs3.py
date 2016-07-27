from bs4 import BeautifulSoup
import urllib2
import lxml

File = urllib2.urlopen("http://www.pythonscraping.com/pages/page3.html")
Html = File.read()
File.close()

soup = BeautifulSoup(Html,'lxml')

for image in soup.find_all('img'):
    print (image.get('src'))
