__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import unittest
from time import sleep

from StoneUIFramework.public.common.Connect import Connect
from StoneUIFramework.public.common.publicfunction import Tools
from StoneUIFramework.config.globalparam import GlobalParam
from StoneUIFramework.public.handle.space.SPACEHANDLE5 import _SPACEHANDLE5
from StoneUIFramework.testcase.空间.机构空间.test4_1资讯.NewArchivies import NewArchivies
from StoneUIFramework.testcase.空间.机构空间.test4_1资讯.DeleteArchivies import DeleteArchivies
from StoneUIFramework.public.common.datainfo import DataInfo
from StoneUIFramework.public.common.log import Log

#资讯发布
class space_ArchiviesO(unittest.TestCase):
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
        self.screen_path = cf.getParam('space',"org_path_004_1")#通过配置文件获取截图的路径
        self.logfile = cf.getParam('log',"logfile")#日志文件名
        #创建Archiviese对象
        self.spaceAr = NewArchivies()
        self.spaceDe = DeleteArchivies()
        sleep(1)
        #测试数据
        d = DataInfo("space.xls")#创建DataInfo()对象
        self.spacename = d.cell("test004-资讯",2,3)#测试空间123
        #创建日志记录模块
        self.log = Log(self.logfile)
    def test_archivies(self):
        """资讯发布"""
        try:
            self.log.info('------------START:test4_1资讯.Archivies004_1.py------------')
        #1.空间首页
            self.handle.Kjlb_click()
            self.log.info('进入空间首页')
        #2.选择空间:测试空间123
            self.handle.Kjlb_browseorgspaceByName_click(self.spacename)
            self.log.info('进入空间：%s'%self.spacename)
        #3.资讯发布
            self.spaceAr.newarchivies(self.driver)
        #4.删除资讯，还原测试场景
            self.spaceDe.deletearchivies(self.driver,self.spacename)
            self.log.info("------------END:test4_1资讯.Archivies004_1.py------------")#宣布成功
        except Exception as err:
            self.tools.getScreenShot(self.screen_path,"ExceptionShot")
            self.log.error("Archivies Outside : %s"%err)
            raise err
        finally:
            self.driver.quit()