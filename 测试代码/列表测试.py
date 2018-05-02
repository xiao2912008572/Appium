# Author:Xiaojingyuan
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

param = ['${cluster_id}', '[0][cluster_id]']

#1.
param_1 = param[1]
print('param[1] = ',param_1)

#2.
param = param_1[1:-1]
print('param[1][1:-1] = ',param)

#3.
param = param.split('][')
print('param[1][1:-1].spit("][") = ',param)
