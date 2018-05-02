# a = [[1, 'Space - 私人空间类型列表', '获取私人空间下面的可选类型列表', '/api/v1/space_classes', 'GET', '', "{'token': '${self.token}'}", '', '[\n    {\n        "aliaz": "food",\n        "id": 67,\n        "name": "食物"\n    },\n    {\n        "aliaz": "house",\n        "id": 68,\n        "name": "居住"\n    },\n    {\n        "aliaz": "traffic",\n        "id": 69,\n        "name": "出行"\n    },\n    {\n        "aliaz": "education",\n        "id": 70,\n        "name": "学习"\n    },\n    {\n        "aliaz": "health",\n        "id": 71,\n        "name": "健康"\n    },\n    {\n        "aliaz": "intercourse",\n        "id": 72,\n        "name": "社交"\n    },\n    {\n        "aliaz": "vocation",\n        "id": 73,\n        "name": "工作"\n    },\n    {\n        "aliaz": "art",\n        "id": 74,\n        "name": "文艺"\n    },\n    {\n        "aliaz": "amusement",\n        "id": 75,\n        "name": "娱乐"\n    },\n    {\n        "aliaz": "beauty",\n        "id": 76,\n        "name": "美护"\n    },\n    {\n        "aliaz": "other",\n        "id": 77,\n        "name": "其他"\n    },\n    {\n        "aliaz": "clothing",\n        "id": 66,\n        "name": "穿衣"\n    }\n]', '', 'YES', 200, '${class_id}=[0][id]'], [2, 'Space - 热门空间名', '获取常用空间名', '/api/v1/spaces/names', 'GET', '', "{'count':'10','class_id':'${class_id}'}", '', '{\n    "names": [\n        "舌尖上的中国",\n        "美食",\n        "民以食为天",\n        "茶",\n        "厨艺秀",\n        "正宗东海海鲜《海鲜大礼》",\n        "吃货世界",\n        "吃货的世界",\n        "我的衣柜",\n        "我的店铺"\n    ],\n    "success": true\n}', '', 'NO', 200, ''], [3, 'Space - 空间创建（私人空间）', '当前用户创建私人空间', '/api/v1/clusters', 'POST', '', "{'token': '${self.token}', 'name': 'api测试','class_id': '${class_id}'}", 'true=[success]', '', '', 'NO', 201, '${cluster_id}=[id]'], [4, 'Space - 空间列表', '获取指定用户的空间列表', '/api/v1/spaces', 'GET', '', "{'token': '${self.token}','q': 'api测试', 'class': None}", '', '', '', 'NO', 200, ''], [5, 'Space - 空间更新（私人空间）', '更新私人空间', '/api/v1/clusters/${cluster_id}', 'PUT', '', "{'token': '${self.token}','id': '${cluster_id}','name': '测试api','class_id':'68'}", '', '', '', 'NO', 200, ''], [6, 'Space - 空间删除（私人空间）', '删除当前用户的私人空间', '/api/v1/clusters/${cluster_id}', 'DELETE', '', "{'token': '${self.token}', 'cluster_id': '${cluster_id}'}", '', '', '', 'NO', 200, ''], [14, 'Space - 文件夹创建', '创建文件夹到私人空间', '/api/v1/galleries', 'POST', '', '', '', '', '', 'NO', 200, '']]

import unittest
import ddt


# list = [['a', 'a1', 'a2'], ['b', 'b1', 'b2'], ['c1', 'c2', 'c3']]


class AAA():
    def analysis_data(self, listA):
        a = listA[0]
        b = listA[1]
        c = listA[2]
        print('a = ', a)
        print('b = ', b)
        print('c = ', c)


@ddt.ddt
class B(unittest.TestCase):
    list = [
        [1110,'a1', 'a2', 'a3'],
        [1111,'b2', 'b2', 'b3'],
        [1112,'c1', 'c2', 'c3'],
        [1113,'d1', 'd2', 'd3'],
        [1114,'e1', 'e2', 'e3'],
        [1115,'f1', 'f2', 'f3'],
        [1116,'g1', 'g2', 'g3'],
        [1117,'h1', 'h2', 'h3'],
        [1118,'i1', 'i2', 'i3'],
        [1119,'j1', 'j2', 'j3'],
        [1120,'k1', 'k2', 'k3'],
        [1121,'l1', 'l2', 'l3']
    ]

    list1 = [
        ['0001', 'a1', 'a2', 'a3'],
        ['0002', 'b2', 'b2', 'b3'],
        ['0003', 'c1', 'c2', 'c3'],
        ['0004', 'd1', 'd2', 'd3'],
        ['0005', 'e1', 'e2', 'e3'],
        ['0006', 'f1', 'f2', 'f3'],
        ['0007', 'g1', 'g2', 'g3'],
        ['0008', 'h1', 'h2', 'h3'],
        ['0009', 'i1', 'i2', 'i3'],
        ['0010', 'j1', 'j2', 'j3'],
        ['0011', 'k1', 'k2', 'k3'],
        ['0012', 'l1', 'l2', 'l3']
    ]

    list2 = [
        ['1', 'a1', 'a2', 'a3'],
        ['2', 'b2', 'b2', 'b3'],
        ['3', 'c1', 'c2', 'c3'],
        ['4', 'd1', 'd2', 'd3'],
        ['5', 'e1', 'e2', 'e3'],
        ['6', 'f1', 'f2', 'f3'],
        ['7', 'g1', 'g2', 'g3'],
        ['8', 'h1', 'h2', 'h3'],
        ['9', 'i1', 'i2', 'i3'],
        ['1', 'j1', 'j2', 'j3'],
        ['11', 'k1', 'k2', 'k3'],
        ['12', 'l1', 'l2', 'l3']
    ]

    # @ddt.data(list[0])
    # @ddt.unpack
    # def test01(self, A, B, C):
    #     print('A = ', A)
    #     print('B = ', B)
    #     print('C = ', C)

    @ddt.data(*list2)
    # @ddt.unpack
    def test02(self, A):
        print('A = ', A)

        a = AAA()
        a.analysis_data(A)
        print()
