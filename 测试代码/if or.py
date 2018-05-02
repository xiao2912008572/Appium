# Author:Xiaojingyuan
# -*- coding: utf-8 -*-

list1 = ['true','false','True','False']
list2 = [
    {
        "clazz": "root",
        "description": "董事会",
        "groups": [
            {
                "clazz": "master",
                "description": "董事长",
                "id": 17,
                "name": "董事长",
                "quota": 1,
                "user_count": 0
            },
            {
                "clazz": "master",
                "description": "管理员",
                "id": 18,
                "master_name": "肖静远",
                "name": "管理员",
                "quota": 2,
                "user_count": 1
            },
            {
                "clazz": "master",
                "description": "总经理",
                "id": 19,
                "name": "总经理",
                "quota": 1,
                "user_count": 0
            }
        ],
        "id": 9,
        "name": "董事会"
    },
    {
        "clazz": "normal",
        "description": "销售部",
        "groups": [
            {
                "clazz": "master",
                "description": "销售经理",
                "id": 20,
                "name": "销售主管",
                "quota": 1,
                "user_count": 0
            },
            {
                "clazz": "normal",
                "description": "销售员",
                "id": 21,
                "name": "销售员",
                "quota": 1,
                "user_count": 0
            }
        ],
        "id": 10,
        "name": "营销部"
    },
    {
        "clazz": "normal",
        "description": "行政部",
        "groups": [
            {
                "clazz": "master",
                "description": "行政人事经理",
                "id": 22,
                "name": "人事主管",
                "quota": 1,
                "user_count": 0
            },
            {
                "clazz": "normal",
                "description": "",
                "id": 44,
                "name": "行政助理",
                "quota": 1,
                "user_count": 0
            }
        ],
        "id": 11,
        "name": "人事部"
    }
]

a = 'False'
if a in list1:
    print(a)
    print('bingo')

# b = '导购员'
b = '人事主管'
if b in list2:
    print(b)
    print('bingo2')

# param = ['true']
# if param[0] in 'true' or 'false':
#     print(123)
