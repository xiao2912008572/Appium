import json

data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
print('data的数据类型是：', type(data))

data_json = json.dumps(data)
print("data_json的数据类型是：", type(data_json))
print(data_json)

a = json.dumps(data_json, sort_keys=True, indent=4, separators=(',', ':'))


