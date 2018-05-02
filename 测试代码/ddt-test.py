# Author:Xiaojingyuan
import unittest
import ddt




testData1=[{"username":"selenium群"},
          # {"username":"python群"},
          {"username":"appium群"}]


a1 = [["{'token': 'self.token', 'parent_id': None}", "{'token': 'self.token'}"],
      ["{'token1': 'self.token', 'parent_id1': None}", "{'token1': 'self.token'}"]]

testData2 = ['appium测试空间', 'appium测试空间', '北京', '东城', 1]
testData3 = [{'token': 'self.token','q': 'api测试', 'class': None},
             {'token': 'self.token','q': 'api测试', 'class': None}]


excel = [["{'token': 'self.token','q': 'api测试', 'class': None}", 12.0], ["{'token': 'self.token','q': 'api测试', 'class': None}", 13.0]]

@ddt.ddt
class space_CreateO(unittest.TestCase):
    # @ddt.data(a1)
    # @ddt.unpack
    # def test01(self,A,B):
    #     print(A)
    #     print(B)

    @ddt.data(*excel)
    def test02(self,A):
        print(A[0])


# data1 = {'token': 'self.token', 'parent_id': None}
# data2 = ['123','223']
# data3 = ['123','223']
#
#
#
#
# @ddt.ddt
# class Test1(unittest.TestCase):
#     # @ddt.data((1, 1, 2), (1, 2, 3))
#     @ddt.data((data1, data2, data3), (data1, data2, data3))
#     @ddt.unpack
#     def test_addnum(self, a, b, expected_value):
#         print(a,b,expected_value)
