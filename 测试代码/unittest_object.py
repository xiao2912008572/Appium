# Author:Xiaojingyuan
__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from YunluFramework_API.testcase.SpaceAPI import *
import json


# Space
@ddt.ddt
class SpaceAPI_Private(unittest.TestCase):
    testData3 = [{'token': 'self.token', 'q': 'api测试', 'class': None},
                 {'token': 'self.token', 'q': 'api测试', 'class': None}]

    # 4.Space - 空间列表
    @ddt.data(*testData3)
    def test04_Space_list_api(self, name):
        '''Space - 空间列表 : 获取指定用户的空间列表
        :param name : 空间名称
        :return:
        '''

        try:
            print(name)

        except Exception as err:
            self.log.error("test11_Space_private_delete_id_api : %s" % err)
            raise err

