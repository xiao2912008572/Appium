__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import unittest
from time import sleep

from StoneUIFramework.testcase.空间.机构空间.test1_1创建机构空间.CreateSpace import CreateSpace
from StoneUIFramework.testcase.空间.机构空间.test1_1创建机构空间.CloseSpace import CloseSpace
from StoneUIFramework.public.common.Connect import Connect
from StoneUIFramework.public.common.publicfunction import Tools
from StoneUIFramework.config.globalparam import GlobalParam
from StoneUIFramework.public.handle.space.SPACEHANDLE5 import _SPACEHANDLE5
from StoneUIFramework.public.common.datainfo import DataInfo
from StoneUIFramework.public.common.log import Log
import ddt


# 创建机构空间
@ddt.ddt
class space_CreateO(unittest.TestCase):
    # 1.全局测试数据
    d = DataInfo("space.xls")  # 创建DataInfo()对象
    fullname1 = d.cell("test001-创建", 2, 1)  # fullname
    easyname1 = d.cell("test001-创建", 2, 2, )  # easyname
    province1 = (d.cell("test001-创建", 2, 4))  # 北京
    city1 = (d.cell("test001-创建", 2, 5))  # 东城
    soverbank1 = d.cell("test001-创建", 2, 7)  # 开户行
    sovermybank1 = d.cell("test001-创建", 2, 8)  # 支行
    soverbanknub1 = int(d.cell("test001-创建", 2, 9))  # 银行账号
    customertype1 = int(d.cell("test001-创建", 2, 3))  # 客户类型
    industry1 = int(d.cell("test001-创建", 2, 10))  # 产业角色

    # 2.初始化
    def setUp(self):
        # 1.建立连接信息
        cnn = Connect()
        self.driver = cnn.connect()
        # 2.创建工具类
        self.tools = Tools(self.driver)  # tools工具
        # 3.创建_BrowseOrgSpace公有定位控件对象
        self.handle = _SPACEHANDLE5(self.driver)
        # 4.创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')
        # 5.获取截图路径、日志路径、日志名
        self.screen_path = cf.getParam('space', "org_path_001_1")  # 通过配置文件获取截图的路径
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名
        # 6.创建日志记录模块
        self.log = Log(self.logfile)
        # 7.创建Createspace和Closespace对象
        self.cr = CreateSpace()
        self.cl = CloseSpace()
        sleep(1)
        # 8.打印日志
        self.log.info('****************************************用例开始！****************************************')
        self.log.info("------------START:test1_1创建机构空间.CreateOrgSpace001_1.py------------")

    # 3.释放资源
    def tearDown(self):
        # 1.打印日志
        self.log.info("------------END:test1_1创建机构空间.CreateOrgSpace001_1.py------------")
        self.log.info('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~用例结束！~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        # 2.关闭driver
        self.driver.quit()

    # 4.测试用例
    @ddt.data([fullname1, easyname1, province1, city1,
               soverbank1, sovermybank1, soverbanknub1,
               customertype1, industry1])
    @ddt.unpack
    def test_spacecreate(self, fullname, easyname, province,
                         city, soverbank, sovermybank, soverbanknub,
                         customertype, industry):
        '''创建机构空间'''
        try:
            # -------------创建机构空间------------
            # 先进行判断，空间是否存在，如果不存在，创建；如果存在，先删除后创建
            sleep(1)
            self.handle.Kjlb_click()  # 进入空间列表
            self.log.info('进入空间列表')
            # 遍历空间列表，查找是否存在该空间
            self.flag = 0
            for element in self.handle.Kjlb_browseorgspace_getElements():
                spacename = element.text
                if spacename == easyname:
                    self.flag = 1
                    self.log.info('已存在该空间')
                    break
                else:
                    pass
            # 如果机构存在
            if self.flag == 1:
                self.cl.closeSpace(self.driver)  # 关闭
                self.cr.createSpace(self.driver, fullname, easyname, province,
                                    city, soverbank, sovermybank, soverbanknub,
                                    customertype, industry)  # 关闭之后,重新创建机构空间
                self.cl.closeSpace(self.driver)
            else:
                self.cr.createSpace(self.driver, fullname, easyname, province,
                                    city, soverbank, sovermybank, soverbanknub,
                                    customertype, industry)  # 创建机构空间
                self.cl.closeSpace(self.driver)
        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("CreateOrgSpace Outside : %s" % err)
            raise err
