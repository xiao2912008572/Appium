import requests
import json

url = 'https://test.yunlu6.com/api/v1/team/4835/products'
headers = {'content-type': 'application/json'}
print(type(headers))
payload = {
    "archive_ids": [],
    "file_ids": [155737],
    "name": "111",
    "prices": [{
        "amount": "",
        "money": ""
    }],
    "properties": [],
    "published": "true",
    "token": "29f421b91e370c00855da1f54e93d7ef"
}
print('payload修改前')
payload = json.dumps(payload)
print('type - payload : ', type(payload))

with requests.Session() as s:
    # r = s.post(url, data=json.dumps(payload), headers=headers)
    r = s.post(url, data=(payload), headers=headers)
    print(r.text)
