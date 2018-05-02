import requests
import json

url = "https://3bxid9fg.api.lncld.net/1.1/rtm/messages/history"

headers = {
    'X-LC-Id': "3BXiD9Fga5RtswdyrJSFQ3h3-gzGzoHsz",
    'X-LC-Sign': "7396816f73bdbcf70281b09dc2c1b3b9,1517046641139,master",
    'Cache-Control': "no-cache",
    'Postman-Token': "8cc4694e-2004-850c-dedb-3b8dfa4e5186"
    }

data = {
    'convid':"e86a750a9bad543a4535c40ef1e45bac"
}
response = requests.request("GET", url, headers=headers)

print(response.text)
