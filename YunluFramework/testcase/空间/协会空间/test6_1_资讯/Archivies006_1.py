__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from YunluFramework.testcase.空间.协会空间.test6_1_资讯 import *


# 资讯发布
@ddt.ddt
class space_ArchiviesA(unittest.TestCase):
    # 1.全局测试数据
    d = DataInfo("space.xls")  # 创建DataInfo()对象
    spacename_1 = d.cell("test008-协会资讯", 2, 3)  # 协会测试123
    title_1 = d.cell("test008-协会资讯", 2, 1)  # 协会测试123
    typelist_1 = int(d.cell("test008-协会资讯", 2, 2))  # 类型列表:经典作品

    # 2.初始化
    @classmethod
    def setUpClass(self):
        # 1.建立连接信息
        cnn = Connect()
        self.driver = cnn.connect()
        # 2.创建工具类
        self.tools = Tools(self.driver)  # tools工具
        # 3.创建 _SPACEHANDLE5公有定位控件对象
        self.handle = SPACEHANDLE5(self.driver)
        # 4.创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')
        # 5.获取截图路径、日志路径、日志名
        self.screen_path = cf.getParam('space', "ass_path_006_1")  # 通过配置文件获取截图的路径
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名
        # 6.创建日志记录模块
        self.log = Log(self.logfile)
        # 7.创建Archiviese对象
        self.spaceAr = NewArchivies()
        self.spaceDe = DeleteArchivies()
        sleep(1)
        # 8.打印日志
        self.log.info('****************************************用例开始！****************************************')
        self.log.info("------------START:test5_8资讯Archivies006_1.py------------")

    # 3.释放资源
    @classmethod
    def tearDownClass(self):
        # 1.打印日志
        self.log.info("------------END:test5_8资讯Archivies006_1.py------------")
        self.log.info('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~用例结束！~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        # 2.关闭driver
        self.driver.quit()

    # 4.测试用例
    @ddt.data([spacename_1, title_1, typelist_1])
    @ddt.unpack
    def test_archivies(self, spacename, title, typelist):
        """资讯发布"""
        try:
            # 1.空间首页
            self.handle.Kjlb_click()
            self.log.info('进入空间首页')
            # 2.选择空间:协会测试123
            self.handle.Kjlb_browseorgspaceByName_click(spacename)
            self.log.info('进入空间：%s' % spacename)
            # 3.资讯发布
            self.spaceAr.newarchivies(self.driver, title, typelist)
            # 4.删除资讯，还原测试场景
            self.spaceDe.deletearchivies(self.driver, spacename)
        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("Archivies Outside : %s" % err)
            raise err
