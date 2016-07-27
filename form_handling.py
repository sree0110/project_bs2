import requests
params = {'firstname': 'Krishna', 'lastname': 'Pawankar'}
r = requests.post("http://pythonscraping.com/files/processing.php", data=params)
print(r.text)

#upload a file
import requests
files = {'uploadFile': open("D:\logo.png", 'rb')}
r = requests.post("http://pythonscraping.com/pages/processing2.php",
files=files)
print(r.text)