__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import unittest
from time import sleep
import logging

from StoneUIFramework.testcase.空间.机构空间.test1_1创建机构空间.CreateSpace import CreateSpace
from StoneUIFramework.testcase.空间.机构空间.test1_1创建机构空间.CloseSpace import CloseSpace
from StoneUIFramework.public.common.Connect import Connect
from StoneUIFramework.public.common.publicfunction import Tools
from StoneUIFramework.config.globalparam import GlobalParam
from StoneUIFramework.public.handle.space.SPACEHANDLE5 import _SPACEHANDLE5
from StoneUIFramework.public.common.datainfo import DataInfo

#创建机构空间
class space_Create(unittest.TestCase):
    @classmethod#装饰器，类方法
    def setUpClass(self):#最开始执行
        #建立连接信息
        cnn = Connect()
        self.driver = cnn.connect()
        #创建工具类
        self.tools = Tools(self.driver)#tools工具
        #创建_BrowseOrgSpace公有定位控件对象
        self.handle = _SPACEHANDLE5(self.driver)
        #创建读取配置信息对象
        cf = GlobalParam('config','path_file.conf')
        #获取截图路径、日志路径、日志名
        self.screen_path = cf.getParam('space',"org_path_001_1")#通过配置文件获取截图的路径
        self.log_path = cf.getParam('space',"log")#通过配置文件获取日志的路径
        self.logfile = cf.getParam('space',"logfile")#日志文件名
        #创建Createspace和Closespace对象
        self.cr = CreateSpace()
        self.cl = CloseSpace()
        sleep(1)
        #测试数据
        d = DataInfo("space.xls")#创建DataInfo()对象
        self.fullname = d.cell("test001-创建",2,1)#fullname
        self.easyname = d.cell("test001-创建",2,2,)#easyname
    def test_spacecreate(self):
        '''创建机构空间'''
        try:
            # self.tools.coverUpdate(self.log_path,self.screen_path)#覆盖更新日志,覆盖更新截图
            self.tools.getLog(self.logfile)#打印日志
            #-------------创建机构空间------------
            #先进行判断，空间是否存在，如果不存在，创建；如果存在，先删除后创建
            sleep(1)
            self.handle.Kjlb_click()#进入空间列表
            name = self.handle.Kjlb_browseorgspaceByID_text(0)#获取第一家空间
            if name == self.easyname:#检查当前的机构简称，如果已经有了，就关闭
                self.cl.closeSpace(self.driver)#关闭
                self.cr.createSpace(self.driver,self.fullname,self.easyname)#关闭之后,重新创建机构空间
                self.cl.closeSpace(self.driver)
            else:
                self.cr.createSpace(self.driver,self.fullname,self.easyname)#创建机构空间
                self.cl.closeSpace(self.driver)
            logging.info("success@@!!!!!!!")#宣布成功
        except Exception as err:
            self.tools.getScreenShot(self.screen_path,"ExceptionShot")
            logging.error("Error Information outside : %s"%err)
            raise err
        finally:
            self.driver.quit()