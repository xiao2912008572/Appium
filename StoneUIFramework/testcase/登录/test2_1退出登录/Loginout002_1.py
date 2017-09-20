__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import unittest
from time import sleep
import logging

from StoneUIFramework.public.common.Connect import Connect
from StoneUIFramework.public.common.publicfunction import Tools
from StoneUIFramework.config.globalparam import GlobalParam
from StoneUIFramework.public.handle.setting.SETTINGHANDLE4 import _SETTINGHANDLE4
from StoneUIFramework.testcase.登录.test2_1退出登录.LoginoutA import LoginoutA

#退出登录
class Loginout(unittest.TestCase):
    @classmethod#装饰器，类方法
    def setUpClass(self):#最开始执行
        #建立连接信息
        cnn = Connect()
        self.driver = cnn.connect()
        #创建工具类
        self.tools = Tools(self.driver)#tools工具
        #创建_SETTINGHANDLE4公有定位控件对象
        self.handle = _SETTINGHANDLE4(self.driver)
        #创建读取配置信息对象
        cf = GlobalParam('config','path_file.conf')
        #获取截图路径、日志路径、日志名
        self.screen_path = cf.getParam('login',"login_path_002_1")#通过配置文件获取截图的路径
        self.log_path = cf.getParam('login',"log")#通过配置文件获取日志的路径
        self.logfile = cf.getParam('login',"logfile")#日志文件名
        sleep(1)
        #创建LoginoutA对象
        self.loginout = LoginoutA()

    def test_loginout(self):
        '''退出登录'''
        try:
            self.tools.getLog(self.logfile)#打印日志
            sleep(1)
            #1.退出登录
            self.loginout.loginout(self.driver,1)#云视页设置
            #2.判断退出是否成功
            assert self.driver.find_element_by_id("com.yunlu6.stone:id/login_btn") is not None,"Error Loginout Failed!"
            logging.info("success@@!!!!!!!")#宣布成功
        except Exception as err:
            self.tools.getScreenShot(self.screen_path,"ExceptionShot")
            logging.error("Error Information Loginout Outside : %s"%err)
            raise err
        finally:
            self.driver.quit()