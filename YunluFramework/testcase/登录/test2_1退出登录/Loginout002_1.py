__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from YunluFramework.testcase.登录.test2_1退出登录 import *


# 退出登录
class Loginout(unittest.TestCase):
    # 1.全局测试数据
    # 2.初始化
    def setUp(self):
        # 1. 建立连接信息
        cnn = Connect()
        self.driver = cnn.connect()
        # 2. 创建工具类
        self.tools = Tools(self.driver)  # tools工具
        # 3. 创建_SETTINGHANDLE4公有定位控件对象
        self.handle = SETTINGHANDLE4(self.driver)
        # 4. 创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')
        # 5.获取截图路径、日志路径、日志名
        self.screen_path = cf.getParam('login', "login_path_002_1")  # 通过配置文件获取截图的路径
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名
        # 6. 创建日志记录模块
        self.log = Log(self.logfile)
        # 7. 创建LoginoutA对象
        self.loginout = LoginoutA()
        # 8.打印日志
        self.log.info('****************************************用例开始！****************************************')
        self.log.info("------------START:test2_1退出登录.Loginout002_1.py------------")

    # 3.释放资源
    def tearDown(self):
        # 1.打印日志
        self.log.info("------------END:test2_1退出登录.Loginout002_1.py------------")
        self.log.info('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~用例结束！~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        # 2.关闭driver
        self.driver.quit()

    def test_loginout(self):
        '''退出登录'''
        try:
            sleep(1)
            # 1.退出登录
            self.loginout.loginout(self.driver, 1)  # 云视页设置
            # 2.判断退出是否成功
            assert self.driver.find_element_by_id("com.yunlu6.yunlu:id/btn_login") is not None, "Error Loginout Failed!"
            self.log.info('判断是否退出成功')
        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("Loginout Outside : %s" % err)
            raise err
