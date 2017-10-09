__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import unittest
from time import sleep

from StoneUIFramework.public.common.Connect import Connect
from StoneUIFramework.public.common.publicfunction import Tools
from StoneUIFramework.config.globalparam import GlobalParam
from StoneUIFramework.public.handle.space.SPACEHANDLE5 import _SPACEHANDLE5
from StoneUIFramework.testcase.空间.协会空间.test2_1编辑.Edit import Edit
from StoneUIFramework.public.common.datainfo import DataInfo
from StoneUIFramework.public.common.log import Log


# 编辑
class space_EditA(unittest.TestCase):
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
        self.screen_path = cf.getParam('space', "ass_path_002_1")  # 通过配置文件获取截图的路径
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名
        # 创建日志记录模块
        self.log = Log(self.logfile)
        # 创建Edit对象
        self.spaceE = Edit()
        sleep(2)
        # 测试数据
        d = DataInfo("space.xls")  # 创建DataInfo()对象
        self.spacename = d.cell("test005-企业名片", 3, 7)  # 测试空间123

    def test_edit(self):
        """协会名片编辑"""
        try:
            self.log.info("------------START:test1_2协会编辑.Edit002_1.py------------")
            # self.tools.coverUpdate(self.log_path,self.screen_path)#覆盖更新日志,覆盖更新截图
            # 1.空间首页
            self.handle.Kjlb_click()
            self.log.info('点击空间首页')
            # 2.选择空间:测试空间123
            self.handle.Kjlb_browseorgspaceByName_click(self.spacename)
            self.log.info('进入空间：%s' % self.spacename)
            # 3.企业名片
            self.spaceE.edit(self.driver)
            self.log.info("------------END:test1_2协会编辑.Edit002_1.py------------")
        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("Outside : %s" % err)
            raise err
        finally:
            self.driver.quit()
