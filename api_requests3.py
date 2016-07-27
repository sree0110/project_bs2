import requests

resp = requests.head('https://www.python.org/index.html')

status = resp.status_code
print(status)
last_modified = resp.headers.get('last-modified')
content_type = resp.headers.get('content-type')
content_length = resp.headers.get('content-length')

print("last_modified :", last_modified , " content_type : ", content_type, " content_length :  ", content_length)