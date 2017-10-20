__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from StoneUIFramework.testcase.登录.test1_1登录 import *

'''
用ddt数据驱动去准备username和password（ddt不会别说）
1.主流程：正确的username和password 验证登录，然后验证页面跳转是否登录成功
2.辅流程1：错误的username和正确的passwrod，验证登录，然后验证页面不跳转，提示错误
3.辅流程2：正确的usrname和错误的pasword，验证登录，然后验证页面不跳转，提示错误
4.辅流程3：空usernaem或者空password，验证登录，然后验证页面不跳转，提示为空信息
思路：
1.登录后，截图，并且验证页面和提示信息，然后登出，用下一组（辅助流程）数据再登录，登出，依次循环
2.三个模块：登录模块。登出模块。控制登录和登出的控制+验证模块
3.每个模块有日志记录、异常截图等验证。
4.
'''


# 登录
@ddt.ddt
class Login(unittest.TestCase):
    # 1.全局测试数据
    d = DataInfo("login.xls")  # 创建DataInfo()对象
    phone1 = int(d.cell("test001", 2, 1))  # 手机号1
    password1 = int(d.cell("test001", 2, 2, ))  # 密码1
    phone2 = int(d.cell("test001", 2, 3))  # 手机号1
    password2 = int(d.cell("test001", 2, 4, ))  # 密码1

    # 2.初始化
    def setUp(self):
        # 1.建立连接信息
        cnn = Connect()
        self.driver = cnn.connect()
        # 2.创建工具类
        self.tools = Tools(self.driver)  # tools工具
        # 3.创建_LOGINHANDLE2公有定位控件对象
        self.handle = LOGINHANDLE2(self.driver)
        # 4.创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')
        # 5.获取截图路径、日志路径、日志名
        self.screen_path = cf.getParam('login', "login_path_001_1")  # 通过配置文件获取截图的路径
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名
        # 6.创建日志记录模块
        self.log = Log(self.logfile)
        # 7.创建LoginA、LoginoutA对象
        self.login = LoginA()
        self.loginout = LoginoutA()
        # 8.打印日志
        self.log.info('****************************************用例开始！****************************************')
        self.log.info("------------START:test1_1登录.Login001_1.py------------")

    # 3.释放资源
    def tearDown(self):
        # 1.打印日志
        self.log.info("------------END:test1_1登录.Login001_1.py------------")
        self.log.info('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~用例结束！~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        # 2.关闭driver
        self.driver.quit()

    # 4.测试用例
    @ddt.data([phone1, password1],
              [phone2, password2])
    @ddt.unpack
    def test_login(self, phone, password):
        '''登录'''
        try:
            sleep(1)
            # 1.登录
            self.login.login(self.driver, phone, password)
            # 2.判断登录是否成功
            assert self.driver.find_element_by_id("com.yunlu6.stone:id/sv_cloundview") is not None, "Error Login Failed!"
            self.log.info('检查是否登录成功')
            # 3.登出
            self.loginout.loginout(self.driver, 1)  # 云视页设置
        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("Login Outside : %s" % err)
            raise err
