# -*- coding: utf-8 -*-
# Author:Xiaojingyuan
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

sys.path.append("/Users/xiaojingyuan/PycharmProjects/Appium")
# sys.path.append("/root/.jenkins/workspace/AutoTest/YunluFramework_API/")
sys.path.append("/root/.jenkins/workspace/AutoTest")
import traceback

from YunluFramework_API.testcase.SpaceAPI import *
from YunluFramework_API.public.common.test_excel import Excel
from YunluFramework_API.api_test.api_request import API_REQUEST


@ddt.ddt
class SpaceAPI_Private(unittest.TestCase):
    '''
    全局接口数据：持续更新
    '''
    # 全局数据: 获取excel中行数据
    # request = API_REQUEST(sheet_name='test2')
    # excel1 = Excel(xls='data_api.xls', sheet_name='test2')
    # data = excel1.get_row_data(sheet_name='test2')

    '''
    20180417 - 订单退货退款流程接口测试
    '''
    # request = API_REQUEST(sheet_name='refund')
    # excel1 = Excel(xls='data_api.xls', sheet_name='refund')
    # data = excel1.get_row_data(sheet_name='refund')

    '''
    20180504 - 订单退货退款流程接口测试1
    '''
    # request = API_REQUEST(sheet_name='refund1')
    # excel1 = Excel(xls='data_api.xls', sheet_name='refund1')
    # data = excel1.get_row_data(sheet_name='refund1')

    '''
    20180507 - 权限模块检查
    '''
    # request = API_REQUEST(sheet_name='cando')
    # excel1 = Excel(xls='data_api.xls', sheet_name='cando')
    # data = excel1.get_row_data(sheet_name='cando')

    '''
    20180628
    '''
    # request = API_REQUEST(sheet_name='test2')
    # excel1 = Excel(xls='data_api.xls', sheet_name='test2')
    # data = excel1.get_row_data(sheet_name='test2')

    '''
    20180708 - 帖子功能接口测试
    '''
    # request = API_REQUEST(sheet_name='topics')
    # excel1 = Excel(xls='data_api.xls', sheet_name='topics')
    # data = excel1.get_row_data(sheet_name='topics')

    '''
    20180712 - 肖静远 测试发帖子功能
    '''
    request = API_REQUEST(sheet_name='topics')
    excel1 = Excel(xls='data_api.xls', sheet_name='topics')
    data = excel1.get_row_data(sheet_name='topics')



    # 1.类开始
    @classmethod
    def setUpClass(self):
        # 1.创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')

        # 2.获取截图路径、日志路径、日志名
        self.logfile = cf.getParam('log', "logfile")  # 所有运行日志文件名
        self.errfile = cf.getParam('log', 'errfile')  # 错误日志文件

        # 3.创建日志记录模块
        self.log = Log(self.logfile)  # 所有日志
        self.err = Log(self.errfile)  # 错误日志

        # 4.打印日志
        self.log.info(
            '****************************************SpaceAPI_Private：开始****************************************'
        )

        # # 5.创建登录对象
        # self.S = Space()

    # 2.类结束
    @classmethod
    def tearDownClass(self):
        # 1.打印日志
        self.log.info(
            '****************************************SpaceAPI_Private：结束****************************************\n'
        )

    # 3.测试方法开始
    def setUp(self):
        self.log.info(
            '------------------------------------用例开始------------------------------------'
        )

    # 4.测试方法结束
    def tearDown(self):
        self.log.info(
            '------------------------------------用例结束------------------------------------\n'
        )

    # 4.测试用例
    @ddt.data(*data)
    def test01_api(self, list):
        '''
        :param list: 参数化列表
        :return:
        '''
        # 1.控制器
        api_no = list[0]  # 接口编号]
        api_name = list[1]  # 接口名称
        api_describe = list[2]  # 接口描述
        api_url = list[3]  # 接口路由
        api_function = list[4]  # 接口方法
        api_headers = list[5]  # 接口头部
        api_data = list[6]  # 接口数据
        api_check = list[7]  # 接口检查
        api_hope = list[8]  # 接口预期
        api_active = list[10]  # 接口执行
        api_status = list[11]  # 预期状态
        api_correlation = list[12]  # 接口关联
        api_message = list[13]  # 消息关联

        # 2.用例执行
        response = ''
        status_code = ''

        if api_active == 'YES':
            try:
                # 发送请求
                response = self.request.api_requests(
                    api_no=api_no,
                    api_name=api_name,
                    api_describe=api_describe,
                    api_url=api_url,
                    api_function=api_function,
                    api_headers=api_headers,
                    api_data=api_data,
                    api_check=api_check,
                    api_hope=api_hope,
                    api_status=api_status,
                    api_correlation=api_correlation,
                    api_messages=api_message)

                # 解析状态码-实际状态码
                status_code = response[0]

                # 解析返回值
                response = response[1]

            except Exception as e:
                self.log.error('Exception Information : {0}'.format(e))
                self.err.error('Exception Information : {0}'.format(
                    traceback.format_exc()))

            # 断言1:status状态码是否正确
            try:
                assert status_code == api_status
            except AssertionError as e:
                self.log.error('返回状态码错误！实际返回状态码为:{0}\n'.format(status_code) +
                               traceback.format_exc())

                self.err.error('1. 接口编号 : {0} | 接口名称 : {1} '.format(
                    api_no, api_name))
                # self.err.error('2. 状态信息 : 预期结果={0} | 实际结果={1}'.format(
                #     api_status, status_code))
                self.err.error('2. 错误信息 : {0}'.format(traceback.format_exc()))
                assert False, '返回状态码错误！实际返回状态码为:{0}'.format(status_code)

            # 断言2:返回值是否为空
            # 状态码为204时
            if status_code == 204:
                try:
                    assert response == ''
                except AssertionError as e:
                    self.log.error('204状态下返回值应该为空！' + traceback.format_exc())
                    self.err.error('1. 接口编号 : {0} | 接口名称 : {1} '.format(
                        api_no, api_name))
                    self.err.error('2. 204状态下返回值应该为空！')
                    self.err.error('3. 错误信息 : {0}'.format(
                        traceback.format_exc()))
                    assert False, '204状态下返回值应该为空,当前实际不为空！'

            # 状态码不为204时
            else:
                try:
                    assert response != ''
                except AssertionError as e:
                    self.log.error('返回值为空！\n' + traceback.format_exc())
                    self.err.error('1. 接口编号 : {0} | 接口名称 : {1} '.format(
                        api_no, api_name))
                    self.err.error('2. 返回值为空！')
                    self.err.error('3. 错误信息 : {0}'.format(
                        traceback.format_exc()))
                    assert False, '返回值应该不为空,当前实际返回值为空！'

            # 断言3:检查点数据校验
            # 如果api_check不为空：
            try:
                if api_check != '':
                    # 3.1 存储检查结果
                    api_check_result = self.request.analysis_check(
                        api_no=api_no,
                        api_name=api_name,
                        api_check=api_check,
                        response=response)

                    # 3.2 断言判断，检查False是否不等于检查结果，如果等于就报错
                    assert False != api_check_result[0]
                else:
                    pass
            except AssertionError as e:
                self.log.error("'检查点:{0} | 实际返回结果:{1} | 结果错误,错误信息:{2}".format(
                    api_check, api_check_result[1], traceback.format_exc()))
                self.err.error('1. 接口编号 : {0} | 接口名称 : {1} '.format(
                    api_no, api_name))
                # self.err.error("2. 检查信息 : {0} | 实际返回结果:{1} ".format(
                #     api_check,
                #     api_check_result[1],
                # ))
                self.err.error('2. 错误信息 : {0}'.format(traceback.format_exc()))
                assert False, '检查点:{0} | 结果错误，错误信息:{1}'.format(api_check, e)

            # 断言4:返回值是否符合预期
            # 如果api_hope不为空:
            if api_hope != '':

                # 1> 先将api_hope通过json解析成对应的格式
                api_hope = json.loads(api_hope)

                # 2> 断言
                try:
                    assert api_hope == response
                except AssertionError as e:
                    self.log.error('实际结果与预期结果不符！' + traceback.format_exc())
                    self.err.error('1. 接口编号 : {0} | 接口名称 : {1} '.format(
                        api_no, api_name))
                    # self.err.error('2. 返回信息 ：预期返回={0} | 实际返回={1}'.format(
                    #     api_hope, response))
                    self.err.error('2. 错误信息 : {0}'.format(
                        traceback.format_exc()))
                    assert False, '实际结果与预期结果不符！'
            else:
                pass

        # 3.用例不执行
        elif api_active == 'NO':
            # self.log.info(list)
            self.log.info('未执行测试用例编号 : {0} | 名称 : {1}'.format(
                api_no, api_name))
            pass


if __name__ == '__main__':
    unittest.main()
