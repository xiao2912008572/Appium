__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import unittest
from time import sleep
from StoneUIFramework.public.common.Connect import Connect
from StoneUIFramework.public.common.publicfunction import Tools
from StoneUIFramework.config.globalparam import GlobalParam
from StoneUIFramework.public.handle.space.SPACEHANDLE5 import _SPACEHANDLE5
from StoneUIFramework.testcase.空间.私人空间.test1_1创建私人空间.ClosePersonSpace import ClosePersonSpace
from StoneUIFramework.testcase.空间.私人空间.test1_1创建私人空间.CreatePersonSpace import CreatePersonSpace
from StoneUIFramework.public.common.datainfo import DataInfo
from StoneUIFramework.public.common.log import Log

#创建私人空间
class perspace_CreateP(unittest.TestCase):
    @classmethod#装饰器，类方法
    def setUpClass(self):#最开始执行
        #1.建立连接信息
        cnn = Connect()
        self.driver = cnn.connect()
        #2.创建工具类
        self.tools = Tools(self.driver)#tools工具
        #3.创建_CreatePersonalSpaceHandle公有定位控件对象
        self.handle = _SPACEHANDLE5(self.driver)
        #4.创建读取配置信息对象
        cf = GlobalParam('config','path_file.conf')
        #5. 获取截图路径、日志路径、日志名
        self.screen_path = cf.getParam('space', "org_path_001_1")  # 通过配置文件获取截图的路径
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名
        # 创建日志记录模块
        self.log = Log(self.logfile)
        #6.创建Createspace和Closespace对象
        self.cr = CreatePersonSpace()
        self.cl = ClosePersonSpace()
        sleep(2)
        #7.准备测试数据
        d = DataInfo("space.xls")#创建DataInfo()对象
        self.spacename = d.cell("test006-私人空间",2,13)#空间名:appium私人空间
        # self.foldername1 = d.cell("test006",2,14)#文件夹1名:appium文件夹
    def test_perspacecreate(self):
        try:
            self.log.info("------------START:test1_1创建私人空间CreatePersonSpace001_1.py------------")
            #1.进入空间列表
            sleep(1)
            self.handle.Kjlb_click()
            self.log.info('进入空间列表')
            # #2.点击主菜单
            # self.handle.Kjlb_mainmenu_click()
            # #3.点击+私人空间
            # self.handle.Kjlb_mainmenu_newpersonspace_click()
            #4.创建私人空间
            if self.driver.find_elements_by_name(self.spacename) != []:#检查当前的私人空间是否已经存在,如果存在就关闭
                self.cl.closePersonSpace(self.driver,self.spacename)#先关闭
                self.cr.createPersonSpace(self.driver,self.spacename)#再创建
                self.cl.closePersonSpace(self.driver,self.spacename)#再关闭
            else:
                self.cr.createPersonSpace(self.driver,self.spacename)#创建
                self.cl.closePersonSpace(self.driver,self.spacename)#关闭
            self.log.info("------------END:test1_1创建私人空间CreatePersonSpace001_1.py------------")
        except Exception as err:
            self.tools.getScreenShot(self.screen_path,"ExceptionShot")
            self.log.error("Outside : %s"%err)
            raise err
        finally:
            self.driver.quit()