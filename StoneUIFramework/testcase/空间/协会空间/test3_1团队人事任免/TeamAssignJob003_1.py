__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import unittest

from StoneUIFramework.public.common.Connect import Connect
from StoneUIFramework.public.common.publicfunction import Tools
from StoneUIFramework.config.globalparam import GlobalParam
from StoneUIFramework.public.handle.space.SPACEHANDLE5 import _SPACEHANDLE5
from StoneUIFramework.testcase.空间.协会空间.test3_1团队人事任免.TeamAssignJob import TeamAssignJob
from StoneUIFramework.public.common.datainfo import DataInfo
from StoneUIFramework.public.common.log import Log


# 团队人事任免
class team_AssignA(unittest.TestCase):
    @classmethod  # 装饰器，类方法
    def setUpClass(self):  # 最开始执行
        # 建立连接信息
        cnn = Connect()
        self.driver = cnn.connect()
        # 创建工具类
        self.tools = Tools(self.driver)  # tools工具
        # 创建_SPACEHANDLE5公有定位控件对象
        self.handle = _SPACEHANDLE5(self.driver)
        # 创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')
        # 获取截图路径、日志路径、日志名
        self.screen_path = cf.getParam('space', "ass_path_003_1")  # 通过配置文件获取截图的路径
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名
        # 创建TeamAssignJob对象
        self.SpaceTa = TeamAssignJob()
        # 测试数据
        d = DataInfo("space.xls")  # 创建DataInfo()对象
        self.spacename = d.cell("test003-团队", 4, 1)  # 协会测试123
        # 创建日志记录模块
        self.log = Log(self.logfile)

    def test_teamassign(self):
        """团队人事任免"""
        try:
            self.log.info("------------Start:test3_1团队人事任免.TeamAssignJob003_1.py------------")
            # 1.空间首页
            self.handle.Kjlb_click()
            self.log.info('点击空间首页')
            # 2.选择空间:协会测试123
            self.handle.Kjlb_browseorgspaceByName_click(self.spacename)
            self.log.info('进入空间：{0}'.format(self.spacename))
            # 3.任免+移除Kjlb_browseascspace_menu_team_menu_assignjob_addperson_confirm
            self.SpaceTa.teamAssignJob(self.driver)
            self.log.info("------------End:test3_1团队人事任免.TeamAssignJob003_1.py------------")
        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("TeamAssignJob Outside : %s" % err)
            raise err
        finally:
            self.driver.quit()
