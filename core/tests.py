from googleapiclient.discovery import build

 

import requests 
ip = requests.get('http://ipinfo.io/json').json()['ip']
print(ip)