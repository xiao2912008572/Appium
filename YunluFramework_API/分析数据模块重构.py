data = {
    'delivery_id':
    37,
    'groups': [{
        'items': [{
            'price_id': 62732,
            'quantity': 1,
        }],
        'message': '',
        'organization_id': '${test_team_id}'
    }],
    'token':
    '${.token1}'
}
# correlationDict = {}
correlationDict = {
    '${.token}': '2fc79e702c878b0ad5b584c9ad4fe927',
    '${.token1}': '6bc91e372785ece0f7ed8e0b1c99e37c',
    '${space_name}': 'api测试',
    '${test_team_id}': 5114
}

list1 =[]
def fun(data):
    if type(data) == type({}):
        for key,value in data.items():
            fun(value)
    elif type(data) == type([]):
        for i in data:
            fun(i)
    else:
        list1.append(data)
        # print(data)
    return list1

# list_c = fun(data)
import json
data = json.dumps(data)
print(type(data))
if '${test_team_id}' in data:
    data = data.replace("${test_team_id}","4815")
    print(data)
    data = json.loads(data)
    print(data)
    print(type(data))

