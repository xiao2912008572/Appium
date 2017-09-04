__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import unittest
from time import sleep
import logging

from StoneUIFramework.public.common.Connect import Connect
from StoneUIFramework.public.common.publicfunction import Tools
from StoneUIFramework.config.globalparam import GlobalParam
from StoneUIFramework.public.handle.space.SPACEHANDLE5 import _SPACEHANDLE5
from StoneUIFramework.testcase.空间.协会空间.test3_1团队人事任免.TeamAssignJob import TeamAssignJob
from StoneUIFramework.public.common.datainfo import DataInfo

# 团队人事任免
class team_Assign(unittest.TestCase):
    @classmethod  #装饰器，类方法
    def setUpClass(self):  #最开始执行
        #建立连接信息
        cnn = Connect()
        self.driver = cnn.connect()
        #创建工具类
        self.tools = Tools(self.driver)  #tools工具
        #创建_SPACEHANDLE5公有定位控件对象
        self.handle = _SPACEHANDLE5(self.driver)
        #创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')
        #获取截图路径、日志路径、日志名
        self.screen_path = cf.getParam('space', "org_path_003_1")  #通过配置文件获取截图的路径
        self.log_path = cf.getParam('space', "log")  #通过配置文件获取日志的路径
        self.logfile = cf.getParam('space', "logfile")  #日志文件名
        #创建TeamAssignJob对象
        self.SpaceTa = TeamAssignJob()
        sleep(1)
        #测试数据
        d = DataInfo("space.xls")  #创建DataInfo()对象
        self.spacename = d.cell("test003-团队",4,1)  #协会测试123

    def test_teamassign(self):
        """团队人事任免"""
        try:
            # self.tools.coverUpdate(self.log_path,self.screen_path)#覆盖更新日志,覆盖更新截图
            self.tools.getLog(self.logfile)  #打印日志
            #1.空间首页
            self.handle.Kjlb_click()
            self.tools.getScreenShot(self.screen_path, "空间首页")
            #2.选择空间:协会测试123
            self.handle.Kjlb_browseorgspaceByName_click(self.spacename)
            #3.任免+移除
            self.SpaceTa.teamAssignJob(self.driver)
            logging.info("success@@!!!!!!!")  #宣布成功
        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            logging.error("Error Information TeamAssignJob Outside : %s" % err)
            raise err
        finally:
            self.driver.quit()