__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from StoneUIFramework.testcase.空间.协会空间.test1_1创建协会空间 import *

# 创建机构空间
@ddt.ddt
class ascspace_CreateA(unittest.TestCase):
    # 1.全局测试数据
    d = DataInfo("space.xls")  # 创建DataInfo()对象
    fullname_1 = d.cell("test001-创建", 3, 1)  # fullname
    easyname_1 = d.cell("test001-创建", 3, 2, )  # easyname
    province_1 = (d.cell("test001-创建", 2, 4))  # 北京
    city_1 = (d.cell("test001-创建", 2, 5))  # 东城
    soverbank_1 = d.cell("test001-创建", 2, 7)  # 开户行
    sovermybank_1 = d.cell("test001-创建", 2, 8)  # 支行
    soverbanknub_1 = int(d.cell("test001-创建", 2, 9))  # 银行账号
    customertype_1 = int(d.cell("test001-创建", 2, 3))  # 客户类型
    industry_1 = int(d.cell("test001-创建", 2, 10))  # 产业角色

    # 2.初始化
    def setUp(self):
        # 1.建立连接信息
        cnn = Connect()
        self.driver = cnn.connect()
        # 2.创建工具类
        self.tools = Tools(self.driver)  # tools工具
        # 3.创建_BrowseOrgSpace公有定位控件对象
        self.handle = SPACEHANDLE5(self.driver)
        # 4.创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')
        # 5.获取截图路径、日志路径、日志名
        self.screen_path = cf.getParam('space', "ass_path_001_1")  # 通过配置文件获取截图的路径
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名
        # 6.创建日志记录模块
        self.log = Log(self.logfile)
        # 7.创建CreateAscSpace和CloseAscSpace对象
        self.cr = CreateAscSpace()
        self.cl = CloseAscSpace()
        sleep(1)
        # 8.打印日志
        self.log.info('****************************************用例开始！****************************************')
        self.log.info("------------START:test1_1创建协会空间.CreateASCSpace001_1.py------------")

    # 3.释放资源
    def tearDown(self):
        # 1.打印日志
        self.log.info("------------END:test1_1创建机构空间.CreateASCSpace001_1.py------------")
        self.log.info('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~用例结束！~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        # 2.关闭driver
        self.driver.quit()

    # 4.测试用例
    @ddt.data([fullname_1, easyname_1, province_1, city_1,
               soverbank_1, sovermybank_1, soverbanknub_1,
               customertype_1, industry_1])
    @ddt.unpack
    def test_ascspacecreate(self, fullname, easyname, province,
                            city, soverbank, sovermybank, soverbanknub,
                            customertype, industry):
        '''创建机构空间'''
        try:
            # -------------创建机构空间------------
            # 先进行判断，空间是否存在，如果不存在，创建；如果存在，先删除后创建
            sleep(1)
            self.handle.Kjlb_click()  # 进入空间列表
            # 遍历空间列表，查找是否存在该空间
            self.flag = 0
            for element in self.handle.Kjlb_browseorgspace_getElements():
                spacename = element.text
                if spacename == easyname:
                    self.flag = 1
                    self.log.info('该协会已存在')
                    break
                else:
                    pass
            # 如果机构存在
            if self.flag == 1:
                self.cl.closeAsscSpace(self.driver, easyname)  # 关闭
                self.cr.createAscSpace(self.driver, fullname, easyname, province,
                                       city, soverbank, sovermybank, soverbanknub,
                                       customertype, industry)  # 关闭之后,重新创建协会空间
                self.cl.closeAsscSpace(self.driver, easyname)
            else:
                self.cr.createAscSpace(self.driver, fullname, easyname, province,
                                       city, soverbank, sovermybank, soverbanknub,
                                       customertype, industry)  # 创建协会空间
                self.cl.closeAsscSpace(self.driver, easyname)
        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("CreateAscSpace Outside : %s" % err)
            raise err
