# Author:Xiaojingyuan
__author__ = 'Administrator'
from YunluFramework_API.api.登陆 import *


# 登录
@ddt.ddt
class Login(Handle):
    # 调用父类的初始化函数
    def __init__(self):
        # 方法一：
        Handle.__init__(self)  # 注意名字是父类

        # 方法二：
        # super(Login, self).__init__()  # 注意名字是子类，而且init后是self之外的参数

        # 1.接口路由
        self.url = self.cf.getURL('login', 'login_url')

    # 2.发送请求
    def loginRequest(self, sql, d_index):
        '''发送登录请求
        :param sql: sql查询语句
        :param d_index: 数据索引
        :param r_index: 返回值索引
        :return:
        '''
        try:
            # 1. 创建请求对象
            r = RequestForHttp()

            # 2.组装数据-[{...},{...}...]对象 列表-字典
            data = self.d.data_assembly(sql)
            data = data[d_index]

            # 3. 发送请求
            response = r.post_function(self.url, data)

            # 4.打印日志
            # self.plog.printlog(data, response, describle='登录接口', url=self.url, method='post')

            # 5.保留token值
            # 5.1获取token
            token = str(json.loads(response[1])['authentication_token'])

            # 5.2提供更新语句
            token = "'" + token + "'"
            sql = 'UPDATE test_token SET token = %s' % token

            # 5.3执行更新
            self.d.update(sql)
            return response

        except Exception as err:
            self.log.error("Function loginRequest error : %s" % err)
            raise err

    # 3.获取token
    def get_token(self):
        '''
        从数据库中查询token
        :return:
        '''
        try:
            # 1.查询语句
            sql = 'select * from test_token'

            # 2.执行
            token = self.d.select(sql)
            return token[0][0]

        except Exception as err:
            self.log.error("Function get_token error : %s" % err)
            raise err
        # 3.获取token

    def get_token1(self):
        '''
        从数据库中查询token
        :return:
        '''
        try:
            # 1.查询语句
            sql = 'select * from test_token'

            # 2.执行
            token = self.d.select(sql)
            return token[0][1]

        except Exception as err:
            self.log.error("Function get_token error : %s" % err)
            raise err
    

    def get_token88(self):
        '''
        从数据库中查询token
        :return:
        '''
        try:
            # 1.查询语句
            sql = 'select * from test_token'

            # 2.执行
            token = self.d.select(sql)
            return token[0][2]

        except Exception as err:
            self.log.error("Function get_token error : %s" % err)
            raise err
    
    def get_token89(self):
        '''
        从数据库中查询token
        :return:
        '''
        try:
            # 1.查询语句
            sql = 'select * from test_token'

            # 2.执行
            token = self.d.select(sql)
            return token[0][3]

        except Exception as err:
            self.log.error("Function get_token error : %s" % err)
            raise err

# a = Login()
# a.loginRequest(sql='select * from test1_1_login_01', d_index=0)
# token = a.get_token1()
# print(token)