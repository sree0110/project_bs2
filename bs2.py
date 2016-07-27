from bs4 import BeautifulSoup
import urllib2

File = urllib2.urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
Html = File.read()
File.close()

soup = BeautifulSoup(Html,"lxml")
All = soup.find_all("a")
i =1
for links in All:
    if i>10:
        break
    print links.get("title")
    i = i+1
#    print (links.get('href'))
