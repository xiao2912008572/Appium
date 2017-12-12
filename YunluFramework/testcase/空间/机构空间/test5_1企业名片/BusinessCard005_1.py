__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from YunluFramework.testcase.空间.机构空间.test5_1企业名片 import *


# 企业名片
@ddt.ddt
class space_BusinessCardO(unittest.TestCase):
    # 1.全局测试数据
    d = DataInfo("space.xls")  # 创建DataInfo()对象
    spacename_1 = d.cell("test005-企业名片", 2, 7)  # 测试空间123
    contact_1 = d.cell("test005-企业名片", 2, 1)  # 联系人
    phone_1 = int(d.cell("test005-企业名片", 2, 2))  # 手机号
    tel_1 = int(d.cell("test005-企业名片", 2, 3))  # 座机号
    email_1 = d.cell("test005-企业名片", 2, 4)  # 邮箱
    QQ_1 = int(d.cell("test005-企业名片", 2, 5))  # QQ
    website_1 = d.cell("test005-企业名片", 2, 6)  # 网址

    # 2.初始化
    def setUp(self):
        # 1.建立连接信息
        cnn = Connect()
        self.driver = cnn.connect()
        # 2.创建工具类
        self.tools = Tools(self.driver)  # tools工具
        # 3.创建_SPACEHANDLE5公有定位控件对象
        self.handle = SPACEHANDLE5(self.driver)
        # 4.创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')
        # 5.获取截图路径、日志路径、日志名
        self.screen_path = cf.getParam('space', "org_path_004_1")  # 通过配置文件获取截图的路径
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名
        # 6.创建BusinessCard对象
        self.spaceBu = BusinessCard()
        sleep(2)
        # 7.创建日志记录模块
        self.log = Log(self.logfile)
        # 8.打印日志
        self.log.info('****************************************用例开始！****************************************')
        self.log.info('------------START:test5_1编辑.BusinessCard005_1.py------------')

    # 3.释放资源
    def tearDown(self):
        # 1.打印日志
        self.log.info("------------END::test5_1编辑.BusinessCard005_1.py------------")  # 宣布成功
        self.log.info('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~用例结束！~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        # 2.关闭driver
        self.driver.quit()

    # 4.测试用例
    @ddt.data([spacename_1, contact_1, phone_1, tel_1, email_1, QQ_1, website_1])
    @ddt.unpack
    def test_businesscard(self, spacename, contact, phone, tel, email, QQ, website):
        """企业名片编辑"""
        try:
            # 1.空间首页
            self.handle.Kjlb_click()
            self.log.info('点击空间首页')
            # 2.选择空间:测试空间123
            self.tools.find_space_by_name(spacename)
            self.log.info('搜索栏搜索结果:{0}'.format(spacename))
            self.handle.Kjlb_browseorgspaceByID_click(0)
            self.log.info('进入空间：%s' % spacename)
            # 3.企业名片
            self.spaceBu.businesscard(self.driver, contact, phone, tel, email, QQ, website)
        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error('BusinessCard Outside : %s' % err)
            raise err
