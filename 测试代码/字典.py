dict1 = [
    {'a':1},
    {'a':2},
    {'a':3}
]

a = dict1[1]['a']
# print(a)

correlation_dict = {'${class_id}':123}

data = {'token': '${self.token}', 'name': 'api测试','class_id': '${class_id}'}

for k in data:
    for key in correlation_dict:
        if data[k] in key:
            data[k] = correlation_dict[key]
print(data)

