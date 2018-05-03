
__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from YunluFramework.testcase.空间.机构空间.test3_1团队人事任免 import *


# 团队人事任免
@ddt.ddt
class team_AssignO(unittest.TestCase):
    # 1.创建数据库操作对象
    d = DataMysql()
    sql01 = "select * from test3_1_orgteamassign_01"
    sql03 = "select * from test3_1_orgteamassign_03"
    sql04 = "select * from test3_1_orgteamassign_04"
    sql05 = "select * from test3_1_orgteamassign_05"
    sql07 = "select * from test3_1_orgteamassign_07"
    sql10 = "select * from test3_1_orgteamassign_10"
    data01 = d.select(sql01, 0)
    data03 = d.select(sql03, 0)
    data04 = d.select(sql04, 0)
    data05 = d.select(sql05, 0)
    data07 = d.select(sql07, 0)
    data10 = d.select(sql10, 0)

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
        self.setting = SETTINGHANDLE4(self.driver)
        self.yunshi = YUNSHIHANDLE1(self.driver)

        # 4.创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')

        # 5.获取截图路径、日志路径、日志名
        self.screen_path = cf.getParam('space', "org_path_003_1")  # 通过配置文件获取截图的路径
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名

        # 6.创建日志记录模块
        self.log = Log(self.logfile)

        # 7.创建Space公有对象
        self.common = CommonSpace(self.handle, self.log, self.tools)
        self.common_logout = CommonSpace(self.setting, self.log, self.tools)
        self.loginA = LoginA()

        # 8.打印日志
        self.log.info('****************************************用例开始！****************************************')
        self.log.info("------------Start:test3_1团队人事任免.TeamAssignJob003_1.py------------")

    # 3.释放资源
    @classmethod
    def tearDownclass(self):

        # 1.打印日志
        self.log.info("------------End:test3_1团队人事任免.TeamAssignJob003_1.py------------")
        self.log.info('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~用例结束！~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

        # 2.关闭driver
        # self.driver.quit()

    # 4.测试用例
    # 4.1 进入空间
    @ddt.data(data01)
    @ddt.unpack
    def test_teamAssign01(self, spacename):
        '''进入空间
        :param spacename:空间名
        :return:
        '''
        try:
            # 1.进入空间
            self.log.info('进入空间：{0}'.format(spacename))
            self.common.enter_space(spacename)
            # kj = self.driver.find_element_by_id('android:id/list')
            # kjs = kj.find_elements_by_class_name('android.widget.RelativeLayout')
            # kjs[0].click()
            self.log.info('点击进入%s' % spacename)

        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_teamAssign01 : %s" % err)
            raise err

    # 4.2 进入团队
    def test_teamAssign02(self):
        '''进入团队
        :return:
        '''
        try:
            # 1.进入团队
            self.log.info('进入团队：')
            self.common.click_org_menu('team')

        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_teamAssign02 : %s" % err)
            raise err

    # 4.3 团队编辑，编辑各职位人数
    @ddt.data(data03)
    @ddt.unpack
    def test_teamAssign03(self, AdmNum, SalNum, AssNum):
        '''团队编辑，编辑各职位人数
        :param AdmNum: 管理员人数
        :param SalNum: 销售员人数
        :param AssNum: 行政助理人数
        :return:
        '''
        try:
            '''编辑各职位人数
            :return:
            '''
            # 1.管理员人数:2人
            self.hanedle.Kjlb_browseorgspace_menu_team_teamedit_click()  # 点击编辑
            self.log.info('点击编辑')
            # self.handle.Kjlb_browseorgspace_menu_team_teamedit_numeidt_click(self.AdministratorLoc)#编辑管理员人数
            self.driver.find_elements_by_id("com.yunlu6.yunlu:id/companyteam_item_edit")[0].click()
            self.log.info('编辑管理员人数')
            self.handle.Kjlb_browseorgspace_menu_team_teamedit_numeidt_jobsnumedit_claer()  # 清空
            self.log.info('清空输入框')
            self.handle.Kjlb_browseorgspace_menu_team_teamedit_numeidt_jobsnumedit_sendkeys(AdmNum)  # 2人
            self.log.info('设置管理员人数：%s' % AdmNum)
            self.handle.Kjlb_browseorgspace_menu_team_teamedit_numeidt_confirm_click()  # 点击是
            self.log.info('点击是')

            # 2.销售员人数:3人
            # self.handle.Kjlb_browseorgspace_menu_team_teamedit_numeidt_click(self.SalespersonLoc)#编辑销售员人数
            self.driver.find_elements_by_id("com.yunlu6.yunlu:id/companyteam_item_edit")[1].click()
            self.log.info('编辑销售员人数')
            self.handle.Kjlb_browseorgspace_menu_team_teamedit_numeidt_jobsnumedit_claer()  # 清空
            self.log.info('清空输入框')
            self.handle.Kjlb_browseorgspace_menu_team_teamedit_numeidt_jobsnumedit_sendkeys(SalNum)  # 3人
            self.log.info('设置销售员人数：%s' % SalNum)
            self.handle.Kjlb_browseorgspace_menu_team_teamedit_numeidt_confirm_click()  # 点击是
            self.log.info('点击是')

            # 3.行政助理人数:4人
            # self.handle.Kjlb_browseorgspace_menu_team_teamedit_numeidt_click(self.AssistantLoc)#编辑助理人数
            self.driver.find_elements_by_id("com.yunlu6.yunlu:id/companyteam_item_edit")[3].click()
            self.log.info('编辑助理人数')
            self.handle.Kjlb_browseorgspace_menu_team_teamedit_numeidt_jobsnumedit_claer()  # 清空
            self.log.info('清空输入框')
            self.handle.Kjlb_browseorgspace_menu_team_teamedit_numeidt_jobsnumedit_sendkeys(AssNum)  # 4人
            self.log.info('设置助理人数：%s' % AssNum)
            self.handle.Kjlb_browseorgspace_menu_team_teamedit_numeidt_confirm_click()  # 点击是
            self.log.info('点击是')

        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_teamAssign03 : %s" % err)
            raise err

    # 4.4 检查各职位人数是否保存生效
    @ddt.data(data04)
    @ddt.unpack
    def test_teamAssign04(self, AdmNum, SalNum, AssNum):
        '''检查各职位人数是否保存生效
        :param AdmNum: 管理员人数
        :param SalNum: 销售员人数
        :param AssNum: 行政助理人数
        :return:
        '''
        try:
            # 1.检查管理员人数编辑是否生效
            # handle.Kjlb_browseorgspace_menu_team_teamedit_numeidt_click(self.AdministratorLoc)#编辑管理员人数
            self.driver.find_elements_by_id("com.yunlu6.yunlu:id/companyteam_item_edit")[0].click()
            self.log.info('点击编辑管理员人数')
            AdmNumm = int(self.handle.Kjlb_browseorgspace_menu_team_teamedit_numeidt_jobsnumedit_text())
            self.log.info('当前管理员人数：{0}'.format(AdmNumm))
            self.log.info('预期管理员人数：{0}'.format(AdmNum))
            assert AdmNum == AdmNumm, "编辑管理员人数保存后未生效"
            self.log.info('检查管理员人数编辑是否生效')
            self.handle.Kjlb_browseorgspace_menu_team_teamedit_numeidt_cancel_click()  # 点击否
            self.log.info('点击否')

            # 2.检查销售员人数编辑是否生效
            # handle.Kjlb_browseorgspace_menu_team_teamedit_numeidt_click(self.SalespersonLoc)#编辑管理员人数
            self.driver.find_elements_by_id("com.yunlu6.yunlu:id/companyteam_item_edit")[1].click()
            self.log.info('点击编辑销售员人数')
            SalNumm = int(self.handle.Kjlb_browseorgspace_menu_team_teamedit_numeidt_jobsnumedit_text())
            self.log.info('当前销售员人数：{0}'.format(SalNumm))
            self.log.info('预期销售员人数：{0}'.format(SalNum))
            assert SalNum == SalNumm, "编辑销售员人数保存后未生效"
            self.log.info('检查销售人员人数编辑是否生效')
            self.handle.Kjlb_browseorgspace_menu_team_teamedit_numeidt_cancel_click()  # 点击否
            self.log.info('点击否')

            # 3.检查行政助理人数编辑是否生效
            # handle.Kjlb_browseorgspace_menu_team_teamedit_numeidt_click(self.AssistantLoc)#编辑管理员人数
            self.driver.find_elements_by_id("com.yunlu6.yunlu:id/companyteam_item_edit")[3].click()
            self.log.info('点击行政助理人数')
            AssNumm = int(self.handle.Kjlb_browseorgspace_menu_team_teamedit_numeidt_jobsnumedit_text())
            self.log.info('当前行政助理人数：{0}'.format(AssNumm))
            self.log.info('预期行政助理人数：{0}'.format(AssNum))
            assert AssNum == AssNumm, "编辑行政助理人数后未生效"
            self.log.info('检查行政助理人数编辑是否生效')
            self.handle.Kjlb_browseorgspace_menu_team_teamedit_numeidt_cancel_click()  # 点击否
            self.log.info('点击否')
            self.handle.Kjlb_browseorgspace_menu_team_teamedit_click()  # 点击编辑按钮
            self.log.info('点击编辑按钮')

        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_teamAssign04 : %s" % err)
            raise err

    # 4.5 人事任免-邀请人脉加入团队
    @ddt.data(data05)
    @ddt.unpack
    def test_teamAssign05(self, Name, Director):
        '''人事任免-邀请人脉加入团队
        :param Name: 姓名
        :param Director: 董事会
        :return:
        '''
        try:
            # 1.点击菜单栏
            self.handle.Kjlb_browseorgspace_menu_team_menu_click()  # 点击菜单栏
            self.log.info('点击菜单栏')

            # 2.点击人事任免
            self.handle.Kjlb_browseorgspace_menu_team_menu_assignjob_click()  # 点击人事任免
            self.log.info('点击人事任免')

            # 3.判断等待任免列表是否为空
            try:
                if self.driver.find_elements_by_id("com.yunlu6.yunlu:id/removaljobs_name") != []:  # 列表是否为空
                    listT = self.handle.Kjlb_browseorgspace_menu_team_menu_assignjob_contact()
                    for i in range(len(listT)):  # 遍历列表
                        if self.handle.Kjlb_browseorgspace_menu_team_menu_assignjob_contact_text(
                                i) == Name:  # 再判断是否该人已被任免
                            self.handle.Kjlb_browseorgspace_menu_team_menu_assignjob_contact_click(0)  # 待任免联系人
                            self.log.info('判断该人是否已被任免')
                            self.log.info('点击待任免联系人')
                            self.handle.Kjlb_browseorgspace_menu_team_menu_assignjob_contact_delete_click()  # 点击移除
                            self.log.info('点击移除')
                        else:
                            pass
                else:
                    pass

            except Exception as e:
                self.log.info('等待人士任免列表为空，错误信息为：%s' % e)

            # 4.点击人事任免新增
            self.handle.Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_click()  # 点击人事任免新增按钮
            self.log.info('点击人事任免新增按钮')

            # 5.搜索姓名:肖静远
            self.handle.Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_search_sendkeys(Name)  # 搜索关键字
            self.log.info('搜索人脉关键字：%s' % Name)
            self.handle.Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_searchbtn_click()  # 点击搜索
            self.log.info('点击搜索')

            # 6.勾选，返回
            # 6.1点击搜索的结果,添加
            self.handle.Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_choose_click(0)  # 勾选
            self.log.info('勾选')
            self.handle.Kjlb_browseorgspace_menu_team_menu_assignjob_addperson_confirm_click()  # 添加
            self.log.info('添加')

            # 6.2返回
            self.handle.Kjlb_browseorgspace_menu_team_menu_assignjob_back_click()
            self.log.info('返回团队页面')
            self.handle.Kjlb_browseorgspace_menu_team_back_click()
            self.log.info('返回到空间名片页面')
            self.handle.Kjlb_browseorgspace_back_click()
            self.log.info('返回搜索结果页面')
            self.handle.Kjlb_search_back_click()
            self.log.info('点击搜索返回按钮，返回空间列表页面')

        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_createProduct05 : %s" % err)
            raise err

    # 4.6 退出当前账号
    def test_teamAssign06(self):
        '''退出当前账号：13027104206
        :return:
        '''
        try:
            # 1.退出当前账号
            self.log.info('退出当前账号：13636059628')
            self.common_logout.logout_from_page(4)

        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_teamAssign06 : %s" % err)
            raise err

    # 4.7 登录新账号
    @ddt.data(data07)
    @ddt.unpack
    def test_teamAssign07(self, phone, password):
        '''登录新账号17607136211 处理请求
        :param login: 账号
        :param password: 密码
        :return:
        '''
        try:
            # 1.调用LoginA模块
            self.loginA.login(self.driver, phone, password)

        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_teamAssign07 : %s" % err)
            raise err

    # 4.8 处理邀请团队的请求
    def test_teamAssign08(self):
        '''处理邀请团队请求
        :return:
        '''
        try:
            # 1.点击通知
            self.yunshi.YS_flow_click()
            self.log.info('点击通知')

            # 2.处理团队成员邀请请求
            self.driver.find_elements_by_name('团队成员邀请')[0].click()
            self.log.info('点击团队成员邀请消息')

            # 3.同意邀请
            self.driver.find_element_by_id('com.yunlu6.yunlu:id/btAgree').click()
            self.log.info('点击同意')

            # 4.返回云视
            self.driver.find_element_by_id('com.yunlu6.yunlu:id/buildstione_backe').click()
            self.log.info('点击返回云视页')

        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_teamAssign08 : %s" % err)
            raise err

    # 4.9 退出当前账号
    def test_teamAssign09(self):
        '''退出当前账号：17607136211
        :return:
        '''
        try:
            # 1.退出当前账号
            self.log.info('退出当前账号：17786174226')
            self.common_logout.logout_from_page(1)

        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_teamAssign09 : %s" % err)
            raise err

    # 4.10 登录邀请账号
    @ddt.data(data10)
    @ddt.unpack
    def test_teamAssign10(self, phone, password):
        '''登录邀请账号：13636059628
        :param phone: 手机号
        :param password: 密码
        :return:
        '''
        try:
            # 1.调用调用LoginA模块
            self.loginA.login(self.driver, phone, password)

        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_teamAssign10 : %s" % err)
            raise err

    # 4.11 进入空间-团队中
    @ddt.data(data01)
    @ddt.unpack
    def test_teamAssign11(self, spacename):
        '''进入空间-团队中
        :param spacename: 空间名
        :return:
        '''
        try:
            # 1.进入空间
            self.log.info('进入空间：{0}'.format(spacename))
            self.common.enter_space(spacename)

            # 2.进入团队
            self.log.info('进入团队：')
            self.common.click_org_menu('team')

        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_teamAssign11 : %s" % err)
            raise err

    # 4.12 人事任免-给待任免列表员工任职
    @ddt.data(data05)
    @ddt.unpack
    def test_teamAssign12(self, Name, Director):
        '''人事任免-给待任免列表员工任职
        :param Name: 姓名
        :param Director: 职位
        :return:
        '''
        try:
            # 0. 菜单栏
            self.handle.Kjlb_browseorgspace_menu_team_menu_click()
            self.log.info('点击菜单栏')
            self.handle.Kjlb_browseorgspace_menu_team_menu_assignjob_click()
            self.log.info('点击人事任免')

            # 1.待任免列表点击联系人-任免职位-勾选-返回
            # 1.1待任免联系人
            self.handle.Kjlb_browseorgspace_menu_team_menu_assignjob_contact_click(0)  # 待任免联系人
            self.log.info('点击待任免联系人')

            # 1.2查找董事会
            self.handle.Kjlb_browseorgspace_menu_team_menu_assignjob_contact_department_click(Director)  # 董事会
            self.log.info('点击董事会')

            # 1.3勾选董事长
            self.handle.Kjlb_browseorgspace_menu_team_menu_assignjob_contact_jobname_click(0)  # 董事长
            self.log.info('勾选董事长')

            # 1.4确定
            self.handle.Kjlb_browseorgspace_menu_team_menu_assignjob_contact_confrim_click()  # 勾选
            self.log.info('勾选')

            # 1.5返回
            self.handle.Kjlb_browseorgspace_menu_team_menu_assignjob_contact_back_click()  # 返回
            self.log.info('返回')

            # 1.6检查董事长姓名
            name = self.driver.find_elements_by_id("com.yunlu6.yunlu:id/companyteam_item_name")[0].text  # 获取董事长姓名
            assert Name == name, "董事长任免失败"
            self.log.info('判断该人脉董事长职位是否任免成功')

        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_createProduct12 : %s" % err)
            raise err

    # 4.13 移除任免
    def test_teamAssign13(self):
        '''移除任免
        :return:
        '''
        try:
            # 1.点击菜单栏
            self.handle.Kjlb_browseorgspace_menu_team_menu_click()  # 点击菜单栏
            self.log.info('点击菜单栏')

            # 2.人事任免
            self.handle.Kjlb_browseorgspace_menu_team_menu_assignjob_click()  # 点击人事任免
            self.log.info('点击人事任免')

            # 3.带任免联系人
            self.handle.Kjlb_browseorgspace_menu_team_menu_assignjob_contact_click(0)  # 待任免联系人
            self.log.info('待任免联系人')

            # 4.点击移除
            self.handle.Kjlb_browseorgspace_menu_team_menu_assignjob_contact_delete_click()  # 点击移除
            self.log.info('点击移除')

        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_createProduct13 : %s" % err)
            raise err
