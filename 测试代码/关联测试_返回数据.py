# Author:Xiaojingyuan

# correlationDict = {}
# correlationDict['${self.token}'] = 'adsfaezdjkhf78dfhjia23bljadsf'
# correlationDict['${space_name}'] = 'api测试'

correlationDict = {
    # '${self.token}': 'adsfaezdjkhf78dfhjia23bljadsf',
    # '${space_name}': 'api测试',
    # '${id}': '1',
    # '${cookie}': 'aseuqo2i34'
}

res = [
    {
        "aliaz": 'null',
        "class_id": 67,
        "cluster_id": 8371,
        "company": 'null',
        "disclosure": "off",
        "gallery_count": 0,
        "locked": 'false',
        "logo_url": 'null',
        "name": "api测试",
        "organization_id": 'null',
        "owner_class": "private",
        "service_id": 'null',
        "vocation": 'null'
    }
]

correlation_13 = '${cluster_id}=[0][cluster_id];${name}=[0][name]'
print('原始的correlation = ', correlation_13)

correlation = correlation_13.replace('\n', '').replace('\r', '').split(';')
print('分割;之后的correlation = ', correlation)
print()

for j in range(len(correlation)):
    param = correlation[j].split('=')
    print('分割=之后的correlation - param  = ', param)

    key = param[0]
    print('key = ', key)

    value = param[1]
    print('value = ', value)
    print()



