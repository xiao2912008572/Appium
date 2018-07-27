__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from YunluFramework.testcase.空间.协会空间.test5_1加会员_管理员_个人_拒绝 import *

# 团队人事任免
@ddt.ddt
class team_AssignA(unittest.TestCase):
    # 1.全局测试数据
    d = DataInfo("space.xls")  # 创建DataInfo()对象
    spacename_1 = d.cell("test003-团队", 4, 1)  # 协会测试321  #行、列

    """  此处暂用不上
    AdministratorLoc_1 = int(d.cell("test003-团队", 3, 2))  # 管理员编辑
    SalespersonLoc_1 = int(d.cell("test003-团队", 3, 3))  # 理事编辑
    AssistantLoc_1 = int(d.cell("test003-团队", 3, 4))  # 常务理事
    Director_1 = int(d.cell("test003-团队", 3, 5))  # 理事长
    VicePresident_1 = int(d.cell("test003-团队", 3, 6))  # 副会长
    Standingvicepresident_1 = int(d.cell("test003-团队", 3, 7))  # 常务副会长
    Member_1 = int(d.cell("test003-团队", 3, 8))  # 会员
    """

    AdmNum_1 = int(d.cell("test003-团队", 4, 2))  # 管理员人数
    AssNum_1 = int(d.cell("test003-团队", 4, 3))  # 理事人数
    SdrNum_1 = int(d.cell("test003-团队", 4, 4))  # 常务理事人数
    DglNum_1 = int(d.cell("test003-团队", 4, 5))  # 理事长人数
    VptNum_1 = int(d.cell("test003-团队", 4, 6))  # 副会长人数
    SvpNum_1 = int(d.cell("test003-团队", 4, 7))  # 常务副会长人数
    MemNum_1 = int(d.cell("test003-团队", 4, 8))  # 会员人数
    Name_1 = d.cell("test003-团队", 2, 8)  # 董祥祥
    phone1_1 = int(d.cell("test007-会员", 2, 3))  # 账号1:17786174226
    password1_1 = int(d.cell("test007-会员", 2, 4))  # 密码:88888888
    phone2_1 = int(d.cell("test007-会员", 2, 5))  # 账号2:13636059628
    password2_1 = int(d.cell("test007-会员", 2, 6))  # 密码2:88888888

    # 2.初始化
    @classmethod
    def setUpClass(self):

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

        # 7.创建日志记录模块
        self.log = Log(self.logfile)

        # 8. 创建LoginA对象
        self.login = LoginA()
        self.loginout = LoginoutA()
        self.addvip = AddPerVip()

        # 9.打印日志
        self.log.info('****************************************用例开始！****************************************')
        self.log.info("------------Start:test3_1团队人事任免.TeamAssignJob003_1.py------------")

    # 3.释放资源
    @classmethod
    def tearDownClass(self):
        # 1.打印日志
        self.log.info("------------End:test3_1团队人事任免.TeamAssignJob003_1.py------------")
        self.log.info('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~用例结束！~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

        # 2.关闭driver
        # self.driver.quit()

    # 4.进入空间
    @ddt.data([spacename_1])
    @ddt.unpack
    def test_teamassign01(self, spacename):
        '''进入空间
        :param spacename: 协会名称：测试协会321
        :return:
        '''
        self.log.info("------------Start:test3_1团队人事任免.test_teamassign01.进入空间------------")

        try:
            sleep(1)
            # 1.空间首页
            self.handle.Kjlb_click()
            self.log.info('点击空间首页')

            # 2.选择空间:协会测试123
            self.handle.Kjlb_click()  # 点击进入空间列表
            self.log.info('点击进入空间列表')
            self.tools.find_space_by_name(spacename)
            self.log.info('搜索栏搜索结果:{0}'.format(spacename))

            # 3.尝试定位该空间，若该该空间存在，则进入，不存在则提示‘空间不存在’
            try:
                self.handle.Kjlb_browseorgspaceByID_click()
                self.log.info('进入空间：{0}'.format(spacename))
            except Exception as err:
                self.log.info('空间不存在')

            """
            3.任免+移除Kjlb_browseascspace_menu_team_menu_assignjob_addperson_confirm
            self.SpaceTa.teamAssignJob(self, spacename, AdminstratorLoc, SalespersonLoc, AssistantLoc, Director,VicePresident,Standingvicepresident,Member, AdmNum, AssNum, SdrNum, DglNum, VptNum, SvpNum, MemNum, Name, phone1,password1, phone2,password2)
            """

        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_teamassign01 : %s" % err)
            raise err

    # 5.团队编辑
    @ddt.data([AdmNum_1, AssNum_1, SdrNum_1, DglNum_1, VptNum_1, SvpNum_1, MemNum_1])
    @ddt.unpack
    def test_teamassign02(self, AdmNum, AssNum, SdrNum, DglNum, VptNum, SvpNum, MemNum):
        '''团队编辑
        :param AdmNum: 管理员人数：2人
        :param AssNum: 理事人数：1人
        :param SdrNum: 常务理事人数：3人
        :param DglNum: 理事长人数：2人
        :param VptNum: 副会长人数：3人
        :param SvpNum: 常务副会长人数：4人
        :param MemNum: 会员人数：1人
        :return:
        '''
        self.log.info("------------Start:test3_1团队人事任免.test_teamassign02.团队编辑------------")
        try:
            handle = SPACEHANDLE5(self.driver)
            sleep(1)
            handle.Kjlb_browseascspace_menu_click()  # 右上角菜单
            self.log.info('点击右上角菜单')
            handle.Kjlb_browseascspace_menu_team_click()  # 点击团队
            self.log.info('点击团队')

            # 1.团队编辑，编辑各职位人数
            # 1.1 管理员人数:2人
            handle.Kjlb_browseascspace_menu_team_teamedit_click()  # 点击编辑
            self.log.info('点击编辑')
            self.driver.find_elements_by_id("com.yunlu6.yunlu:id/companyteam_item_edit")[0].click()
            self.log.info('编辑管理员人数')
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit_clear()  # 清空
            self.log.info('清空输入框')
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit_sendkeys(AdmNum)  # 2人
            self.log.info('设置管理员人数：%s' % AdmNum)
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_confirm_click()  # 点击是
            self.log.info('点击是')

            # 1.2 理事人数:1人
            self.driver.find_elements_by_id("com.yunlu6.yunlu:id/companyteam_item_edit")[1].click()
            self.log.info('编辑理事人数')
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit_clear()  # 清空
            self.log.info('清空输入框')
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit_sendkeys(AssNum)  # 3人
            self.log.info('设置理事人数：%s' % AssNum)
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_confirm_click()  # 点击是
            self.log.info('点击是')

            # 1.3常务理事人数：3人
            self.driver.find_elements_by_id("com.yunlu6.yunlu:id/companyteam_item_edit")[2].click()
            self.log.info('编辑常务理事人数')
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit_clear()  # 清空
            self.log.info('清空输入框')
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit_sendkeys(SdrNum)
            self.log.info('设置常务理事人数：%s' % SdrNum)
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_confirm_click()  # 点击是
            self.log.info('点击是')

            # 1.4理事长人数
            self.driver.find_elements_by_id("com.yunlu6.yunlu:id/companyteam_item_edit")[3].click()
            self.log.info('编辑理事长人数')
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit_clear()  # 清空
            self.log.info('清空输入框')
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit_sendkeys(DglNum)
            self.log.info('理事长人数：%s' % DglNum)
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_confirm_click()  # 点击是
            self.log.info('点击是')

            # 1.5副会长人数
            self.driver.find_elements_by_id("com.yunlu6.yunlu:id/companyteam_item_edit")[4].click()
            self.log.info('编辑副会长人数')
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit_clear()  # 清空
            self.log.info('清空输入框')
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit_sendkeys(VptNum)
            self.log.info('副会长人数：%s' % VptNum)
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_confirm_click()  # 点击是
            self.log.info('点击是')

            # 1.6常务副会长人数
            self.driver.find_elements_by_id("com.yunlu6.yunlu:id/companyteam_item_edit")[5].click()
            self.log.info('编辑常务副会长人数')
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit_clear()  # 清空
            self.log.info('清空输入框')
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit_sendkeys(SvpNum)
            self.log.info('常务副会长人数：%s' % SvpNum)
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_confirm_click()  # 点击是
            self.log.info('点击是')

            # 1.7会员人数
            self.driver.find_elements_by_id("com.yunlu6.yunlu:id/companyteam_item_edit")[6].click()
            self.log.info('编辑会员人数')
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit_clear()  # 清空
            self.log.info('清空输入框')
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit_sendkeys(MemNum)
            self.log.info('会员人数：%s' % MemNum)
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_confirm_click()  # 点击是
            self.log.info('点击是')

            # 2.检查各职位人数是否保存生效
            # 2.1 检查管理员人数编辑是否生效
            # handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_click(self.AdministratorLoc)#编辑管理员人数
            self.driver.find_elements_by_id("com.yunlu6.yunlu:id/companyteam_item_edit")[0].click()
            self.log.info('点击编辑管理员人数')
            AdmNumm = int(handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit_text())
            self.log.info('当前管理员人数：{0}'.format(AdmNumm))
            self.log.info('预期管理员人数：{0}'.format(AdmNum))
            assert AdmNum == AdmNumm, "编辑管理员人数保存后未生效"
            self.log.info('检查管理员人数编辑是否生效')
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_cancel_click()  # 点击否
            self.log.info('点击否')

            # 2.2 检查理事人数编辑是否生效
            # handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_click(self.SalespersonLoc)#编辑管理员人数
            self.driver.find_elements_by_id("com.yunlu6.yunlu:id/companyteam_item_edit")[1].click()
            self.log.info('点击编辑理事人数')
            AssNumm = int(handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit_text())
            self.log.info('当前理事人数：{0}'.format(AssNumm))
            self.log.info('预期理事人数：{0}'.format(AssNum))
            assert AssNum == AssNumm, "编辑理事人数保存后未生效"
            self.log.info('检查理事人数编辑是否生效')
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_cancel_click()  # 点击否
            self.log.info('点击否')

            # 2.3 检查常务理事人数编辑是否生效
            self.driver.find_elements_by_id("com.yunlu6.yunlu:id/companyteam_item_edit")[2].click()
            self.log.info('点击常务理事人数')
            SdrNumm = int(handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit_text())
            self.log.info('当前常务理事人数：{0}'.format(SdrNumm))
            self.log.info('预期常务理事人数：{0}'.format(SdrNum))
            assert SdrNum == SdrNumm, "编辑常务理事人数后未生效"
            self.log.info('检查常务理事人数编辑是否生效')
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_cancel_click()  # 点击否
            self.log.info('点击否')

            # 2.4 检查理事长人数编辑是否生效
            self.driver.find_elements_by_id("com.yunlu6.yunlu:id/companyteam_item_edit")[3].click()
            self.log.info('点击理事长人数')
            DglNumm = int(handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit_text())
            self.log.info('当前理事长人数：{0}'.format(DglNumm))
            self.log.info('预期理事长人数：{0}'.format(DglNum))
            assert DglNum == DglNumm, "编辑理事长人数后未生效"
            self.log.info('检查理事长人数编辑是否生效')
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_cancel_click()  # 点击否
            self.log.info('点击否')

            # 2.5检查副会长人数编辑是否生效
            self.driver.find_elements_by_id("com.yunlu6.yunlu:id/companyteam_item_edit")[4].click()
            self.log.info('点击副会长人数')
            VptNumm = int(handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit_text())
            self.log.info('当前副会长人数：{0}'.format(VptNumm))
            self.log.info('预期副会长人数：{0}'.format(VptNum))
            assert VptNum == VptNumm, "编辑副会长人数后未生效"
            self.log.info('检查副会长人数编辑是否生效')
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_cancel_click()  # 点击否
            self.log.info('点击否')

            # 2.6检查常务副会长人数编辑是否生效
            self.driver.find_elements_by_id("com.yunlu6.yunlu:id/companyteam_item_edit")[5].click()
            self.log.info('点击常务副会长人数')
            SvpNumm = int(handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit_text())
            self.log.info('当前常务副会长人数：{0}'.format(SvpNumm))
            self.log.info('预期常务副会长人数：{0}'.format(SvpNum))
            assert SvpNum == SvpNumm, "编辑常务副会长人数后未生效"
            self.log.info('检查常务副会长人数编辑是否生效')
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_cancel_click()  # 点击否
            self.log.info('点击否')

            # 2.7检查会员人数编辑是否生效
            self.driver.find_elements_by_id("com.yunlu6.yunlu:id/companyteam_item_edit")[6].click()
            self.log.info('点击会员人数')
            MemNumm = int(handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_jobsnumedit_text())
            self.log.info('当前会员人数：{0}'.format(MemNumm))
            self.log.info('预期会员人数：{0}'.format(MemNum))
            assert MemNum == MemNumm, "编辑会员人数后未生效"
            self.log.info('检查会员人数编辑是否生效')
            handle.Kjlb_browseascspace_menu_team_teamedit_numeidt_cancel_click()  # 点击否
            self.log.info('点击否')

            # 2.8关闭编辑
            handle.Kjlb_browseascspace_menu_team_teamedit_click()  # 点击编辑按钮
            self.log.info('点击编辑按钮')

        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_teamassign02 : %s" % err)
            raise err

    # 6.菜单栏-人事任免
    @ddt.data([Name_1])
    @ddt.unpack
    def test_teamassign03(self, Name):
        '''菜单栏-人事任免
        :param Name: 姓名：董祥
        :return:
        '''
        try:
            self.log.info("------------Start:test3_1团队人事任免.test_teamassign03.人事任免邀请------------")

            # 1 点击菜单栏
            self.handle.Kjlb_browseascspace_menu_team_menu_click()  # 点击菜单栏
            self.log.info('点击菜单栏')

            # 2点击人事任免
            self.handle.Kjlb_browseascspace_menu_team_menu_assignjob_click()  # 点击人事任免
            self.log.info('点击人事任免')

            # 3判断等待任免列表是否为空
            try:
                if self.driver.find_elements_by_id("com.yunlu6.yunlu:id/removaljobs_name") != []:  # 列表是否为空
                    listT = self.handle.Kjlb_browseascspace_menu_team_menu_assignjob_contact()
                    for i in range(len(listT)):  # 遍历列表
                        if self.handle.Kjlb_browseascspace_menu_team_menu_assignjob_contact()[
                            i].text == Name:  # 再判断是否该人已被任免
                            self.handle.Kjlb_browseascspace_menu_team_menu_assignjob_contact_click(0)  # 待任免联系人
                            self.log.info('判断该人是否已被任免')
                            self.log.info('点击待任免联系人')
                            self.handle.Kjlb_browseascspace_menu_team_menu_assignjob_contact_delete_click()  # 点击移除
                            self.log.info('点击移除')
                        else:
                            pass
                else:
                    pass
            except Exception as e:
                self.log.info('等待人事任免列表为空：错误信息为：%s' % e)

            # 4点击人事任免新增按钮
            self.handle.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_click()  # 点击人事任免新增按钮
            self.log.info('点击人事任免新增按钮')

            # 5.搜索姓名:董祥
            self.handle.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_search_sendkeys(Name)  # 搜索关键字
            self.log.info('搜索人脉关键字：%s' % Name)
            self.handle.Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_searchbtn_click()  # 点击搜索
            self.log.info('点击搜索')

            # 6.点击搜索的结果,添加
            self.handle.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_choose_click(0)  # 勾选
            self.log.info('勾选')
            self.handle.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_confirm_click()  # 添加
            self.log.info('添加')

        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_teamassign03 : %s" % err)
            raise err

    # 7.返回空间列表
    def test_teamassign04(self):
        '''返回空间列表
        :return:
        '''
        self.log.info("------------Start:test3_1团队人事任免.test_teamassign04.返回空间列表------------")
        try:

            # 1返回团队页面
            self.handle.Kjlb_browseorgspace_menu_team_menu_assignjob_back_click()  # 返回团队页面
            self.log.info('返回团队页面')

            # 2返回空间名片页面
            self.handle.Kjlb_browseorgspace_menu_team_back_click()  # 返回空间名片页面
            self.log.info('返回到空间名片页面')

            # 3返回搜索结果页面
            self.handle.Kjlb_browseorgspace_back_click()  # 返回搜索结果页面
            self.log.info('返回搜索结果页面')

            try:
                self.handle.Kjlb_search_back_click()
                self.log.info('点击搜索返回按钮，返回空间列表页面')  # 返回空间列表
            except Exception as e:
                self.log.info('未找到该控件，不执行返回空间列表页面操作')

        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_teamassign04 : %s" % err)
            raise err

    # 8.登录受邀账号-同意邀请
    @ddt.data([phone1_1, password1_1])
    @ddt.unpack
    def test_teamassign05(self, phone1, password1):
        '''同意邀请
        :param phone1: 账号：17786174226
        :param password1: 密码：88888888
        :return:
        '''
        self.log.info("------------Start:test3_1团队人事任免.test_teamassign05.登录受邀账号-同意邀请------------")

        try:
            # 1.退出账号,登录受邀账号处理消息
            # 1.1调用loginout模块:退出当前账号
            self.log.info('退出当前账号')
            self.loginout.loginout(self.driver, 4)  # 空间页设置
            self.log.info('退出当前账号完毕')

            # 1.2调用loginA模块:登录受邀账号
            self.log.info('登录受邀账号：{0},{1}'.format(phone1, password1))
            self.login.login(self.driver, phone1, password1)
            self.log.info('登录受邀账号完毕')
            sleep(1)

            # 1.3点击流程
            self.driver.find_element_by_id("com.yunlu6.yunlu:id/icon_flow").click()
            self.log.info('点击流程')

            # 1.4点击消息第一条
            self.driver.find_element_by_id("com.yunlu6.yunlu:id/reminditem_content").click()
            self.log.info('点击第1条消息')

            # 1.5点击同意
            self.driver.find_element_by_id("com.yunlu6.yunlu:id/btAgree").click()
            self.log.info('点击同意')

            # 1.6返回到云视
            self.driver.find_element_by_id('com.yunlu6.yunlu:id/buildstione_backe').click()
            self.log.info('点击返回云视页')

            # 1.7退出受邀账号
            self.log.info('退出受邀账号')
            self.loginout.loginout(self.driver, 1)
            self.log.info('退出受邀账号完毕')

        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_teamassign05 : %s" % err)
            raise err

    # 9.登录邀请账号-进行人事任免
    @ddt.data([phone2_1, password2_1, spacename_1, Name_1])
    @ddt.unpack
    def test_teamassign06(self, phone2, password2, spacename, Name):
        '''登录邀请账号-进行人事任免
        :param phone2: 账号：13636059628
        :param password2: 密码：88888888
        :param spacename: 空间名：协会测试321
        :param Name: 姓名：董祥
        :return:
        '''
        self.log.info("------------Start:test3_1团队人事任免.test_teamassign06.登录邀请账号-进行任免------------")
        try:
            # 9.登录邀请账号-检查各处消息
            # 9.1登录
            self.log.info('登录邀请账号:{0},{1} 检查各处消息'.format(phone2, password2))
            self.login.login(self.driver, phone2, password2)
            self.log.info('登录邀请账号完毕')
            sleep(1)

            # 9.2空间首页
            self.handle.Kjlb_click()
            self.log.info('点击空间首页')

            # 9.3选择空间:协会测试123
            self.handle.Kjlb_click()  # 点击进入空间列表
            self.log.info('点击进入空间列表')
            self.tools.find_space_by_name(spacename)
            self.log.info('搜索栏搜索结果:{0}'.format(spacename))
            self.handle.Kjlb_browseorgspaceByID_click()
            self.log.info('进入协会：%s' % spacename)
            self.handle.Kjlb_browseascspace_menu_click()  # 右上角菜单
            self.log.info('点击右上角菜单')
            self.handle.Kjlb_browseascspace_menu_team_click()  # 点击团队
            self.log.info('点击团队')
            self.handle.Kjlb_browseascspace_menu_team_menu_click()  # 点击菜单栏
            self.log.info('点击菜单栏')
            self.handle.Kjlb_browseascspace_menu_team_menu_assignjob_click()  # 点击人事任免
            self.log.info('点击人事任免')

            # 9.4待任免列表点击联系人-任免职位-勾选-返回
            self.handle.Kjlb_browseascspace_menu_team_menu_assignjob_contact_click(0)  # 待任免联系人
            self.log.info('点击待任免联系人')
            self.handle.Kjlb_browseascspace_menu_team_menu_assignjob_contact_department_click(0)  # 秘书处
            self.log.info('点击秘书处')
            self.handle.Kjlb_browseascspace_menu_team_menu_assignjob_contact_jobname_click(1)  # 秘书长
            self.log.info('勾选秘书长')
            self.handle.Kjlb_browseascspace_menu_team_menu_assignjob_contact_confrim_click()  # 勾选
            self.log.info('勾选')
            self.handle.Kjlb_browseascspace_menu_team_menu_assignjob_addperson_back_click()  # 返回
            self.log.info('返回')
            namee = self.driver.find_elements_by_id("com.yunlu6.yunlu:id/companyteam_item_name")[1].text  # 获取秘书长姓名
            self.log.info('判断该人脉秘书长职位是否任免成功')
            assert Name == namee, "秘书长任免失败"
            self.log.info('任免成功')
        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_teamassign06 : %s" % err)
            raise err

    # 移除任免,还原
    def test_teamassign07(self):
        '''移除任免
        :return:
        '''
        self.log.info("------------Start:test3_1团队人事任免.test_teamassign07.移除任免，还原------------")

        try:
            self.handle.Kjlb_browseascspace_menu_team_menu_click()  # 点击菜单栏
            self.log.info('点击菜单栏')
            self.handle.Kjlb_browseascspace_menu_team_menu_assignjob_click()  # 点击人事任免
            self.log.info('点击人事任免')
            self.handle.Kjlb_browseascspace_menu_team_menu_assignjob_contact_click(0)  # 待任免联系人
            self.log.info('待任免联系人')
            self.handle.Kjlb_browseascspace_menu_team_menu_assignjob_contact_delete_click()  # 点击移除
            self.log.info('点击移除')
        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_teamassign07 : %s" % err)
            raise err
