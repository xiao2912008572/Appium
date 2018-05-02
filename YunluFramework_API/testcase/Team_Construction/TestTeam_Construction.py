# Author:Xiaojingyuan
__author__ = 'Administrator'
from YunluFramework_API.testcase.SpaceAPI import *
import json


# Space
@ddt.ddt
class SpaceAPI_Private(unittest.TestCase):
    # 声明数据库操作对象
    d = DataMysql()

    # 私人空间创建：私人空间name
    data_test03_Space_private_create_api = d.select(sql='select * from Space_private_create_api_table')[0][0]

    sql01 = 'select * from test_SpaceAPI_01'
    sql03 = 'select * from test_SpaceAPI_02'

    # 1.类开始
    @classmethod
    def setUpClass(self):
        # 1.创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')

        # 2.获取截图路径、日志路径、日志名
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名

        # 3.创建日志记录模块
        self.log = Log(self.logfile)

        # 4.打印日志
        self.log.info('****************************************SpaceAPI_Private：开始****************************************')

        # 5.创建登录对象
        self.S = Space()

    # 2.类结束
    @classmethod
    def tearDownClass(self):
        # 1.打印日志
        self.log.info('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~SpaceAPI_Private：结束~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

    # 3.测试方法开始
    def setUp(self):
        # 1.查询私人空间更新：私人空间id
        self.data_test05_Space_update_id_api = self.d.select(sql='select * from Space_update_id_api_table')[0][0]

        # 2.私人空间文件夹更新：私人空间文件夹id
        self.data_test07_Space_folder_update_id_api = self.d.select(sql='select * from Space_folder_update_id_api_table')[0][0]

    # 4.测试用例
    '''
    4.1 覆盖接口
    Space - 空间类型列表（私人空间）
    Space - 热门空间名
    Space - 空间创建（私人空间）
    Space - 空间列表
    Space - 空间更新（私人空间）
    Space - 文件夹创建
    Space - 文件夹更新
    Space - 文件夹列表
    Space - 空间概况（私人空间）
    Space - 文件夹删除
    Space - 空间删除（私人空间）

    4.2 测试流程
    空间创建
    热门空间名：根据空间列表获取的类型
    空间类型列表：获取
    空间列表：查询
    空间更新：名称
    文件夹创建
    文件夹更新：名称
    文件夹列表：查询
    空间概况：浏览文件夹信息
    文件夹删除
    空间删除
    '''

    # 1.Space - 私人空间类型列表
    def test01_Space_type_list_api(self):
        '''Space - 私人空间类型列表 ：获取空间或目录类型列表
        :return:
        '''

        try:
            self.log.info("------------START:test01_Space_type_list_api()------------")
            # 1.调用请求
            response = self.S.Space_private_type_list_api()

            # 2.检查状态码
            self.log.info('1.判断返回状态码：{0} ?= {1}:'.format(200, response[0]))
            assert 200 == response[0], '返回状态不正确：{0}'.format(response[0])
            self.log.info('status_code：OK')

            # 3.查询数据库原始数据
            self.log.info('2.判断返回数据与数据库中数据是否相等：')
            data_sql = self.d.data_assembly(sql='select * from Space_private_type_list_api_table')
            self.log.info('数据库原始数据为：{0}'.format(data_sql))

            # 4.解析返回值数据
            data_res = json.loads(response[1])  # 转换成列表
            self.log.info('返回的结果数据为：{0}'.format(data_res))

            # 5.检查数据
            assert data_res == data_sql, 'Error Information：返回的结果与数据库中不匹配'
            self.log.info('返回数据：OK')
            self.log.info("------------END:test01_Space_type_list_api()------------\n")

        except Exception as err:
            self.log.error("test01_Space_type_list_api : %s" % err)
            raise err

    # 2.Space - 热门空间名
    def test02_Space_popular_name_api(self):
        '''Space - 热门空间名 ：获取常用空间名
        :return:
        '''

        try:
            self.log.info("------------START:test02_Space_popular_name_api()------------")
            # 1.获取空间类型
            self.log.info('调用Space_private_type_list_api接口获取私人空间类型')
            data_res = json.loads(self.S.Space_private_type_list_api()[1])
            class_id = data_res[0]['id']

            # 1.调用请求
            response = self.S.Space_popular_name_api(class_id=class_id)

            # 2.检查状态码
            self.log.info('1.判断返回状态码：{0} ?= {1}:'.format(200, response[0]))
            assert 200 == response[0], '返回状态不正确：{0}'.format(response[0])
            self.log.info('status_code：OK')

            # 3.检查返回值
            response = json.loads(response[1])
            self.log.info('2.判断success：{0} ?= {1}：'.format('True', response['success']))
            assert True == response['success'], 'success状态不正确：{0}'.format(response['success'])
            self.log.info('success：OK')

            # 4.检查字段
            self.log.info('3.判断names：names ? <> None:')
            assert None != response['names'], 'names字段返回为空不正确'
            self.log.info('names：OK')
            self.log.info("------------End:test02_Space_popular_name_api()------------\n")

        except Exception as err:
            self.log.error("test02_Space_popular_name_api : %s" % err)
            raise err

    # 3.Space - 私人空间创建
    @ddt.data([data_test03_Space_private_create_api])
    @ddt.unpack
    def test03_Space_private_create_api(self, name):
        '''Space - 空间创建（私人空间）：当前用户创建私人空间
        :return:
        '''
        try:
            self.log.info("------------Start:data_test03_Space_private_create_api()------------")
            # 1.获取空间类型
            self.log.info('调用Space_private_type_list_api接口获取私人空间类型')
            data_res = json.loads(self.S.Space_private_type_list_api()[1])
            class_id = data_res[0]['id']

            # 1.调用请求
            response = self.S.Space_private_create_api(name, class_id=class_id)

            # 2.检查状态码
            self.log.info('1.判断返回状态码：{0} ?= {1}:'.format(201, response[0]))
            assert 201 == response[0], '返回状态不正确：{0}'.format(response[0])
            self.log.info('status_code：OK')

            # 3.检查返回值
            response = json.loads(response[1])
            self.log.info('2.判断success：{0} ?= {1}:'.format('True', response['success']))
            assert True == response['success'], 'success状态不正确：{0}'.format(response['success'])
            self.log.info('success：OK')

            # 4.将私人空间id存入数据库中
            id = response["id"]
            self.d.update(sql='update Space_update_id_api_table set id = %s' % id)
            self.log.info('更新数据库"Space_update_id_api_table"中私人空间id：{0}'.format(id))
            self.log.info("------------End:data_test03_Space_private_create_api()------------\n")

        except Exception as err:
            self.log.error("test03_Space_private_create_api : %s" % err)
            raise err

    # 4.Space - 空间列表
    @ddt.data([data_test03_Space_private_create_api])
    @ddt.unpack
    def test04_Space_list_api(self, name):
        '''Space - 空间列表 : 获取指定用户的空间列表
        :param name : 空间名称
        :return:
        '''

        try:
            self.log.info("------------Start:test04_Space_list_api()------------")
            # 1.调用请求
            response = self.S.Space_list_api(q=name)

            # 2.检查状态码
            self.log.info('1.判断返回状态码：{0} ?= {1}:'.format(200, response[0]))
            assert 200 == response[0], '返回状态不正确：{0}'.format(response[0])
            self.log.info('status_code：OK')

            # 3.检查返回值
            response = json.loads(response[1])
            self.log.info('2.判断返回值中name：{0} 和数据库中name：{1} 是否一致?:'.format(response[0]["name"], name))
            assert name == response[0]["name"], 'name和数据库中name不一致'
            self.log.info('name：OK')
            self.log.info("------------End:test04_Space_list_api()------------\n")

        except Exception as err:
            self.log.error("test04_Space_list_api : %s" % err)
            raise err

    # 5.Space - 空间更新（私人空间）
    def test05_Space_update_id_api(self):
        '''Space - 空间更新（私人空间）: 更新私人空间
        :param id : 私人空间id
        :return:
        '''

        try:
            self.log.info("------------Start:test05_Space_update_id_api()------------")
            # 1.获取空间类型
            self.log.info('调用Space_private_type_list_api接口获取私人空间类型')
            data_res = json.loads(self.S.Space_private_type_list_api()[1])

            # 2.更新class_id,选取返回值列表中第二个字典对象的id值
            class_id = str(data_res[1]['id'])
            self.log.info('获取class_id，并选取新的id：{0}'.format(class_id))

            # 3.调用请求
            response = self.S.Space_update_id_api(id=self.data_test05_Space_update_id_api, name='测试api', class_id=class_id)

            # 4.检查状态码
            self.log.info('1.判断返回状态码：{0} ?= {1}:'.format(200, response[0]))
            assert 200 == response[0], '返回状态不正确：{0}'.format(response[0])
            self.log.info('status_code：OK')

            # 5.检查返回值
            response = json.loads(response[1])
            self.log.info('2.判断success：{0} ?= {1}：'.format('True', response['success']))
            assert True == response['success'], 'success状态不正确：{0}'.format(response['success'])
            self.log.info('success：OK')
            self.log.info("------------End:test05_Space_update_id_api()------------\n")

        except Exception as err:
            self.log.error("test05_Space_update_id_api : %s" % err)
            raise err

    # 6.Space - 文件夹创建
    def test06_Space_folder_create_api(self):
        '''Space - 文件夹创建 : 创建文件夹到私人空间
        :param cluster_id : 私人空间id
        :return:
        '''

        try:
            self.log.info("------------Start:test06_Space_folder_create_api()------------")
            # 1.调用请求
            response = self.S.Space_folder_create_api(cluster_id=self.data_test05_Space_update_id_api, name='api测试文件夹')

            # 2.检查状态码
            self.log.info('1.判断返回状态码：{0} ?= {1}:'.format(201, response[0]))
            assert 201 == response[0], '返回状态不正确：{0}'.format(response[0])
            self.log.info('status_code：OK')

            # 3.检查返回值
            response = json.loads(response[1])
            self.log.info('2.判断success：{0} ?= {1}：'.format('True', response['success']))
            assert True == response['success'], 'success状态不正确：{0}'.format(response['success'])
            self.log.info('success：OK')

            # 4.将文件夹id存入数据库中
            id = response["id"]
            self.d.update(sql='update Space_folder_update_id_api_table set id = %s' % id)
            self.log.info('更新数据库"Space_folder_create_api_table"中文件夹id：{0}'.format(id))
            self.log.info("------------End:test06_Space_folder_create_api()------------\n")

        except Exception as err:
            self.log.error("test06_Space_folder_create_api : %s" % err)
            raise err

    # 7.Space - 文件夹更新
    def test07_Space_folder_update_id_api(self):
        '''Space - 文件夹更新
        :param id :         文件夹ID
        :param cluster_id : 私有空间ID
        :param name :       文件夹名称
        :return:
        '''

        try:
            self.log.info("------------Start:test07_Space_folder_update_id_api()------------")
            # 1.调用请求
            response = self.S.Space_folder_update_id_api(id=self.data_test07_Space_folder_update_id_api, cluster_id=self.data_test05_Space_update_id_api, name='测试文件夹api')

            # 2.检查状态码
            self.log.info('1.判断返回状态码：{0} ?= {1}:'.format(200, response[0]))
            assert 200 == response[0], '返回状态不正确：{0}'.format(response[0])
            self.log.info('status_code：OK')

            # 3.检查返回值
            response = json.loads(response[1])
            self.log.info('2.判断success：{0} ?= {1}：'.format('True', response['success']))
            assert True == response['success'], 'success状态不正确：{0}'.format(response['success'])
            self.log.info('success：OK')
            self.log.info("------------End:test07_Space_folder_update_id_api()------------\n")

        except Exception as err:
            self.log.error("test07_Space_folder_update_id_api : %s" % err)
            raise err

    # 8.Space - 文件夹列表
    def test08_Space_folder_list_api(self):
        '''Space - 文件夹列表 ： 获取当前用户的文件夹
        :return:
        '''

        try:
            self.log.info("------------Start:test08_Space_folder_list_api()------------")
            # 1.调用请求
            response = self.S.Space_folder_list_api(cluster_id=self.data_test05_Space_update_id_api)

            # 2.检查状态码
            self.log.info('1.判断返回状态码：{0} ?= {1}:'.format(200, response[0]))
            assert 200 == response[0], '返回状态不正确：{0}'.format(response[0])
            self.log.info('status_code：OK')

            # 3. 遍历文件夹，看name是否修改成功，文件夹id是否正确返回
            # 3.1文件夹
            response = json.loads(response[1])
            self.log.info("2.判断文件夹id返回是否正确：")
            self.log.info('数据库中创建时文件夹的id：{0}'.format(self.data_test07_Space_folder_update_id_api))
            self.log.info('返回文件夹列表结果中gallery的id：{0} '.format(response["gallery"][0]["id"]))
            assert self.data_test07_Space_folder_update_id_api == str(response["gallery"][0]["id"]), '文件夹id返回失败！'
            self.log.info('文件夹id返回正确')

            # 3.2name
            self.log.info("3.判断文件夹name返回是否正确：")
            self.log.info('更新文件夹的name：测试文件夹api')
            self.log.info('返回文件夹列表结果中gallery的name：{0}'.format(response["gallery"][0]["name"]))
            assert "测试文件夹api" == response["gallery"][0]["name"], "文件夹name更新失败"
            self.log.info('文件夹name返回正确')
            self.log.info("------------End:test08_Space_folder_list_api()------------\n")

        except Exception as err:
            self.log.error("test08_Space_folder_list_api : %s" % err)
            raise err

    # 9. Space - 空间概况（私人空间）
    def test09_Space_overview_id_api(self):
        '''Space - 空间概况（私人空间）：空间概况
        :return:
        '''

        try:
            self.log.info("------------Start:test09_Space_overview_id_api()------------")
            # 1.调用请求
            response = self.S.Space_overview_id_api(id=self.data_test05_Space_update_id_api)

            # 2.检查状态码
            self.log.info('1.判断返回状态码：{0} ?= {1}:'.format(200, response[0]))
            assert 200 == response[0], '返回状态不正确：{0}'.format(response[0])
            self.log.info('status_code：OK')

            # 3.检查返回值
            self.log.info('2.判断返回值 ?<> None：')
            assert None != response[1], '返回值为空'
            self.log.info('response_content：OK')

        except Exception as err:
            self.log.error("test09_Space_overview_id_api : %s" % err)
            raise err

    # 10.Space - 文件夹删除
    def test10_Space_folder_delete_id_api(self):
        '''Space - 文件夹删除
        :return:
        '''

        try:
            self.log.info("------------Start:test10_Space_folder_delete_id_api()------------")
            # 1.调用请求
            response = self.S.Space_folder_delete_id_api(id=self.data_test07_Space_folder_update_id_api)

            # 2.检查状态码
            self.log.info('1.判断返回状态码：{0} ?= {1}:'.format(200, response[0]))
            assert 200 == response[0], '返回状态不正确：{0}'.format(response[0])
            self.log.info('status_code：OK')

            # 3.检查返回值
            response = json.loads(response[1])
            self.log.info('2.判断success：{0} ?= {1}：'.format('True', response['success']))
            assert True == response['success'], 'success状态不正确：{0}'.format(response['success'])
            self.log.info('success：OK')
            self.log.info("------------End:test07_Space_folder_update_id_api()------------\n")

        except Exception as err:
            self.log.error("test10_Space_folder_delete_id_api : %s" % err)
            raise err

    # Space - 空间删除（私人空间）
    def test11_Space_private_delete_id_api(self):
        '''Space - 空间删除（私人空间）
        :return:
        '''

        try:
            self.log.info("------------Start:test11_Space_private_delete_id_api()------------")
            # 1.调用请求
            response = self.S.Space_private_delete_id_api(id=self.data_test05_Space_update_id_api)

            # 2.检查状态码
            self.log.info('1.判断返回状态码：{0} ?= {1}:'.format(200, response[0]))
            assert 200 == response[0], '返回状态不正确：{0}'.format(response[0])
            self.log.info('status_code：OK')

            # 3.检查返回值
            response = json.loads(response[1])
            self.log.info('2.判断success：{0} ?= {1}：'.format('True', response['success']))
            assert True == response['success'], 'success状态不正确：{0}'.format(response['success'])
            self.log.info('success：OK')
            self.log.info("------------End:test11_Space_private_delete_id_api()------------\n")

        except Exception as err:
            self.log.error("test11_Space_private_delete_id_api : %s" % err)
            raise err

    # @ddt.data([sql01, 0])
    # @ddt.unpack
    # def test_SpaceAPI_01(self, sql, d_index):
    #     '''创建机构空间
    #     :param sql: sql语句
    #     :param d_index: 数据索引1
    #     :return:
    #     '''
    #     try:
    #         # 1. 调用创建请求
    #         response = self.S.Space_org_create_api(sql, d_index)
    #         # 1.1.更新数据库
    #         organization_id = json.loads(response[1])['organization_id']
    #         sql = 'UPDATE test_SpaceAPI_02 SET organization_id = %s' % organization_id
    #         self.d.update(sql)
    #
    #         # 2. 解析数据，断言
    #         # 2.1状态码
    #         self.log.info('1.判断返回状态码：{0} = {1}'.format(201, response[0]))
    #         assert 201 == response[0], '返回状态不正确：{0}'.format(response[0])
    #         self.log.info('status_code：OK')
    #
    #         # 2.2返回数据
    #         response = json.loads(response[1])
    #         self.log.info('2.判断success：{0} = {1}'.format('True', response['success']))
    #         assert True == response['success'], 'success状态不正确：{0}'.format(response['success'])
    #         self.log.info('success：OK')
    #
    #     except Exception as err:
    #         self.log.error("test_SpaceAPI_01 : %s" % err)
    #         raise err
    #
    # def test_SpaceAPI_02(self):
    #     '''访问空间列表'''
    #     try:
    #         # 1.调用空间列表接口
    #         response = self.S.Space_list_api()
    #
    #         # 2.解析数据，断言
    #         # 2.1 状态码
    #         self.log.info('1.判断返回状态码：{0} = {1}'.format(200, response[0]))
    #         assert 200 == response[0], '返回状态不正确：{0}'.format(response[0])
    #         self.log.info('status_code：OK')
    #
    #         # 2.2 将结果转换成列表，然后遍历结果，检查是否创建成功
    #         re = json.loads(response[1])
    #         for r in re:
    #             if r["company"] == '测试空间123':
    #                 self.log.info('2.遍历结果，结果中包含创建的空间:{0}'.format(r['company']))
    #                 break
    #
    #     except Exception as err:
    #         self.log.error("test_SpaceAPI_02 : %s" % err)
    #         raise err
    #
    # @ddt.data([sql03])
    # @ddt.unpack
    # def test_SpaceAPI_03(self, sql):
    #     '''关闭机构空间
    #     :param sql: sql语句
    #     :param d_index: 数据索引1
    #     :return:
    #     '''
    #     try:
    #         # 1. 调用删除空间接口
    #         response = self.S.Space_delete_api(sql)
    #
    #         # 2. 解析数据，断言
    #         # 2.1状态码
    #         self.log.info('1.判断返回状态码：{0} = {1}'.format(200, response[0]))
    #         assert 200 == response[0], '返回状态不正确：{0}'.format(response[0])
    #         self.log.info('status_code：OK')
    #
    #         # 2.2返回数据
    #         response = json.loads(response[1])
    #         self.log.info('2.判断success：{0} = {1}'.format('True', response['success']))
    #         assert True == response['success'], 'success状态不正确：{0}'.format(response['success'])
    #         self.log.info('success：OK')
    #
    #     except Exception as err:
    #         self.log.error("test_SpaceAPI_02 : %s" % err)
    #         raise err
