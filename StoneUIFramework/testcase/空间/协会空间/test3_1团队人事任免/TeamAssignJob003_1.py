__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from StoneUIFramework.testcase.空间.协会空间.test3_1团队人事任免 import *


# 团队人事任免
@ddt.ddt
class team_AssignA(unittest.TestCase):
    # 1.全局测试数据
    d = DataInfo("space.xls")  # 创建DataInfo()对象
    spacename_1 = d.cell("test003-团队", 4, 1)  # 协会测试123
    AdministratorLoc_1 = int(d.cell("test003-团队", 4, 2))  # 管理员编辑
    SalespersonLoc_1 = int(d.cell("test003-团队", 4, 2))  # 助理编辑
    AssistantLoc_1 = int(d.cell("test003-团队", 4, 4))  # 理事编辑
    AdmNum_1 = int(d.cell("test003-团队", 4, 5))  # 管理员人数
    SalNum_1 = int(d.cell("test003-团队", 4, 6))  # 助理人数
    AssNum_1 = int(d.cell("test003-团队", 4, 7))  # 理事人数
    Name_1 = d.cell("test003-团队", 2, 8)  # 肖静远
    Director_1 = int(d.cell("test003-团队", 4, 9))  # 秘书处
    Marketing_1 = int(d.cell("test003-团队", 4, 10))  # 会员组
    HR_1 = int(d.cell("test003-团队", 4, 11))  # 财务处

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
        self.screen_path = cf.getParam('space', "ass_path_003_1")  # 通过配置文件获取截图的路径
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名
        # 6.创建TeamAssignJob对象
        self.SpaceTa = TeamAssignJob()
        # 7.创建日志记录模块
        self.log = Log(self.logfile)
        # 8.打印日志
        self.log.info('****************************************用例开始！****************************************')
        self.log.info("------------Start:test3_1团队人事任免.TeamAssignJob003_1.py------------")

    # 3.释放资源
    def tearDown(self):
        # 1.打印日志
        self.log.info("------------End:test3_1团队人事任免.TeamAssignJob003_1.py------------")
        self.log.info('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~用例结束！~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        # 2.关闭driver
        self.driver.quit()

    # 4.测试用例
    @ddt.data([spacename_1, AdministratorLoc_1, SalespersonLoc_1, AssistantLoc_1,
               AdmNum_1, SalNum_1, AssNum_1, Name_1, Director_1, Marketing_1, HR_1])
    @ddt.unpack
    def test_teamassign(self, spacename, AdminstratorLoc, SalespersonLoc, AssistanLoc,
                        AdmNum, SalNum, AssNum, Name, Director, Marketing, Hr):
        """团队人事任免"""
        try:
            # 1.空间首页
            self.handle.Kjlb_click()
            self.log.info('点击空间首页')
            # 2.选择空间:协会测试123
            self.handle.Kjlb_browseorgspaceByName_click(spacename)
            self.log.info('进入空间：{0}'.format(spacename))
            # 3.任免+移除Kjlb_browseascspace_menu_team_menu_assignjob_addperson_confirm
            self.SpaceTa.teamAssignJob(self.driver, spacename, AdminstratorLoc, SalespersonLoc,
                                       AssistanLoc, AdmNum, SalNum, AssNum,
                                       Name, Director, Marketing, Hr)
        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("TeamAssignJob Outside : %s" % err)
            raise err
