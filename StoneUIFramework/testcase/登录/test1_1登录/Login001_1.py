__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import unittest
from time import sleep
import logging

from StoneUIFramework.public.common.Connect import Connect
from StoneUIFramework.public.common.publicfunction import Tools
from StoneUIFramework.config.globalparam import GlobalParam
from StoneUIFramework.public.handle.login.LOGINHANDLE2 import _LOGINHANDLE2
from StoneUIFramework.public.common.datainfo import DataInfo
from StoneUIFramework.testcase.登录.test1_1登录.LoginA import LoginA

#登录
class Login(unittest.TestCase):
    @classmethod#装饰器，类方法
    def setUpClass(self):#最开始执行
        #建立连接信息
        cnn = Connect()
        self.driver = cnn.connect()
        #创建工具类
        self.tools = Tools(self.driver)#tools工具
        #创建_LOGINHANDLE2公有定位控件对象
        self.handle = _LOGINHANDLE2(self.driver)
        #创建读取配置信息对象
        cf = GlobalParam('config','path_file.conf')
        #获取截图路径、日志路径、日志名
        self.screen_path = cf.getParam('login',"login_path_001_1")#通过配置文件获取截图的路径
        self.log_path = cf.getParam('login',"log")#通过配置文件获取日志的路径
        self.logfile = cf.getParam('login',"logfile")#日志文件名
        sleep(1)
        #测试数据
        d = DataInfo("login.xls")#创建DataInfo()对象
        self.phone = int(d.cell("test001",2,1))#手机号
        self.password = int(d.cell("test001",2,2,))#密码
        #创建LoginA对象
        self.login = LoginA()
    def test_login(self):
        '''登录'''
        try:
            self.tools.getLog(self.logfile)#打印日志
            sleep(1)
            #1.登录
            self.login.login(self.driver,self.phone,self.password)
            #2.判断登录是否成功
            assert self.driver.find_element_by_id("com.yunlu6.stone:id/sv_cloundview") is not None ,"Error Login Failed!"
            logging.info("success@@!!!!!!!")#宣布成功
        except Exception as err:
            self.tools.getScreenShot(self.screen_path,"ExceptionShot")
            logging.error("Error Information Login Outside : %s"%err)
            raise err
        finally:
            self.driver.quit()