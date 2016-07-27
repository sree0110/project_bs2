from bs4 import BeautifulSoup
import urllib2
import lxml


url = "http://www.pythonscraping.com/pages/warandpeace.html"

content = urllib2.urlopen(url).read()
#print content

soup = BeautifulSoup(content, 'lxml')

con = soup.find_all('span',{"class":"green"})
for words in con:
    print words.text


title = soup.find_all('h1')
for words in title:
    print words.text


    




