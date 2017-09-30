__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import unittest
from time import sleep

from StoneUIFramework.public.common.Connect import Connect
from StoneUIFramework.public.common.publicfunction import Tools
from StoneUIFramework.config.globalparam import GlobalParam
from StoneUIFramework.public.handle.space.SPACEHANDLE5 import _SPACEHANDLE5
from StoneUIFramework.testcase.空间.协会空间.test1_1创建协会空间.CreateAscSpace import CreateAscSpace
from StoneUIFramework.testcase.空间.协会空间.test1_1创建协会空间.CloseAscSpace import CloseAscSpace
from StoneUIFramework.public.common.datainfo import DataInfo
from StoneUIFramework.public.common.log import Log

#创建机构空间
class ascspace_CreateA(unittest.TestCase):
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
        self.screen_path = cf.getParam('space',"ass_path_001_1")#通过配置文件获取截图的路径
        self.logfile = cf.getParam('log',"logfile")#日志文件名
        #创建日志记录模块
        self.log = Log(self.logfile)
        #创建CreateAscSpace和CloseAscSpace对象
        self.cr = CreateAscSpace()
        self.cl = CloseAscSpace()
        sleep(1)
        #测试数据
        d = DataInfo("space.xls")#创建DataInfo()对象
        self.fullname = d.cell("test001-创建",3,1)#fullname
        self.easyname = d.cell("test001-创建",3,2,)#easyname
    def test_ascspacecreate(self):
        '''创建机构空间'''
        try:
            self.log.info("------------START:test1_1创建机构空间.CreateASCSpace001_1.py------------")
            #-------------创建机构空间------------
            #先进行判断，空间是否存在，如果不存在，创建；如果存在，先删除后创建
            sleep(1)
            self.handle.Kjlb_click()#进入空间列表
            # 遍历空间列表，查找是否存在该空间
            self.flag = 0
            for element in self.handle.Kjlb_browseorgspace_getElements():
                spacename = element.text
                if spacename == self.easyname:
                    self.flag = 1
                    self.log.info('该协会已存在')
                    break
                else:
                    pass
            # 如果机构存在
            if self.flag == 1:
                self.cl.closeAsscSpace(self.driver, self.easyname)  # 关闭
                self.cr.createAscSpace(self.driver, self.fullname, self.easyname)  # 关闭之后,重新创建机构空间
                self.cl.closeAsscSpace(self.driver, self.easyname)
            else:
                self.cr.createAscSpace(self.driver, self.fullname, self.easyname)  # 创建机构空间
                self.cl.closeAsscSpace(self.driver, self.easyname)
            self.log.info("------------END:test1_1创建机构空间.CreateASCSpace001_1.py------------")
        except Exception as err:
            self.tools.getScreenShot(self.screen_path,"ExceptionShot")
            self.log.error("Outside : %s"%err)
            raise err
        finally:
            self.driver.quit()