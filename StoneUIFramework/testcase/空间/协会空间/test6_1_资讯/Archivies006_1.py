__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import unittest
from time import sleep
import logging

from StoneUIFramework.public.common.Connect import Connect
from StoneUIFramework.public.common.publicfunction import Tools
from StoneUIFramework.config.globalparam import GlobalParam
from StoneUIFramework.public.handle.space.SPACEHANDLE5 import _SPACEHANDLE5
from StoneUIFramework.testcase.空间.协会空间.test6_1_资讯.NewArchivies import NewArchivies
from StoneUIFramework.public.common.datainfo import DataInfo

#资讯发布
class space_ArchiviesA(unittest.TestCase):
    @classmethod#装饰器，类方法
    def setUpClass(self):#最开始执行
        #建立连接信息
        cnn = Connect()
        self.driver = cnn.connect()
        #创建工具类
        self.tools = Tools(self.driver)#tools工具
        #创建 _SPACEHANDLE5公有定位控件对象
        self.handle = _SPACEHANDLE5(self.driver)
        #创建读取配置信息对象
        cf = GlobalParam('config','path_file.conf')
        #获取截图路径、日志路径、日志名
        self.screen_path = cf.getParam('space',"ass_path_006_1")#通过配置文件获取截图的路径
        self.log_path = cf.getParam('space',"log")#通过配置文件获取日志的路径
        self.logfile = cf.getParam('space',"logfile")#日志文件名
        #创建Archiviese对象
        self.spaceAr = NewArchivies()
        sleep(1)
        #测试数据
        d = DataInfo("space.xls")#创建DataInfo()对象
        self.spacename = d.cell("test008-协会资讯",2,3)#协会测试123
    def test_archivies(self):
        """资讯发布"""
        try:
            # self.tools.coverUpdate(self.log_path,self.screen_path)#覆盖更新日志,覆盖更新截图
            self.tools.getLog(self.logfile)#打印日志
        #1.空间首页
            self.handle.Kjlb_click()
            self.tools.getScreenShot(self.screen_path,"空间首页")
        #2.选择空间:协会测试123
            self.handle.Kjlb_browseorgspaceByName_click(self.spacename)
        #3.资讯发布
            self.spaceAr.newarchivies(self.driver)
            logging.info("success@@!!!!!!!")#宣布成功
        except Exception as err:
            self.tools.getScreenShot(self.screen_path,"ExceptionShot")
            logging.error("Error_006_1 Information Archivies Outside : %s"%err)
            raise err
        finally:
            self.driver.quit()