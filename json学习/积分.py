import requests
import json
import random

list1 = []
# 生成500条数据
for i in range(1, 20):
    # 随机生成手机号码
    # no = random.randint(111, 999)
    # phone = '13027104' + str(no)
    # phone = '+86  ' + phone

    # 生成手机号
    if i < 10:
        i = '00{}'.format(i)
    elif i >= 10 and i < 100:
        i = '0{}'.format(i)
    phone = '13027105' + str(i)
    phone = '+86  ' + phone
    # print(phone)

    # 随机生成姓名
    tuple1 = ('qwertyuipqweropiuksldjhafsdfkjlhzxmczxcvnmasdf')
    name = random.sample(tuple1, 5)
    name = "".join(name)

    # 将生成的电话号码存到文件中
    with open('//Users/xiaojingyuan/Desktop/1.txt', 'a') as f:
        f.write(phone)
        f.write('\n')
        f.close()

    # 组装数据
    dict_t = {"name": name, "numbers": [{"value": phone, "type": "other"}]}
    # print(dict_t)
    list1.append(dict_t)
# print(list1)


# 组装数据
# list1 = [{"name": "小杜3", "numbers": [{"value": "+86  13797074796", "type": "other"}]}, ]
list1 = json.dumps(list1)  # 将列表转成str——json类型
print(list1)
# print(type(list1))

querystring = {
    "token": "07a45170f6df0b11c4e1385bb83ba8e3",
    'list': list1
}
print(type(querystring))  # 字典类型

url = "https://api.yunlu6.com/api/v1/people/phonebook"
headers = {
    'Cache-Control': "no-cache",
    'Postman-Token': "a225a0dd-8934-e4bf-5ecf-d4099e51321c"
}
response = requests.post(url, data=querystring)
print(response.text)
