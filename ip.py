import requests
import json

url = "http://localhost:3000/api/auth"
headers = {'content-type': 'application/json'}
data = {"email":"olafa@gmail.com", "password":"meia0708"}
r = requests.post(url, data=json.dumps(data), headers=headers)
print(r.status_code)

if(r.status_code==200):
    print("passou")
else:print("nao")
