__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from StoneUIFramework.testcase.空间.协会空间.test5_8加会员_个人_企业_同意 import *


# 加会员_个人_企业_同意
@ddt.ddt
class AddPtoOAgreeA(unittest.TestCase):
    # 1.全局测试数据
    d = DataInfo("space.xls")  # 创建DataInfo()对象
    spacename_1 = d.cell("test007-会员", 9, 1)  # 协会测试789
    orgname_1 = d.cell("test007-会员", 9, 2)  # 明月
    orgname1_1 = d.cell("test007-会员", 9, 9)  # 明月俱乐部
    phone1_1 = int(d.cell("test007-会员", 9, 3))  # 账号1:15102761413
    password1_1 = int(d.cell("test007-会员", 9, 4))  # 密码:12345678
    phone2_1 = int(d.cell("test007-会员", 9, 5))  # 账号2:13027104206
    password2_1 = int(d.cell("test007-会员", 9, 6))  # 密码2:12345678
    phone3_1 = int(d.cell("test007-会员", 9, 7))  # 账号3:17607136211
    password3_1 = int(d.cell("test007-会员", 9, 8))  # 密码3:12345678

    # 2.初始化
    def setUp(self):
        # 1.建立连接信息
        cnn = Connect()
        self.driver = cnn.connect()
        # 2.创建工具类
        self.tools = Tools(self.driver)  # tools工具
        # 3.创建_LOGINHANDLE2和_SPACEHANDLE5公有定位控件对象
        self.handleL = LOGINHANDLE2(self.driver)
        self.handleS = SPACEHANDLE5(self.driver)
        # 4.创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')
        # 5.获取截图路径、日志路径、日志名
        self.screen_path = cf.getParam('space', "ass_path_005_8")  # 通过配置文件获取截图的路径
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名
        sleep(1)
        # 6.创建日志记录模块
        self.log = Log(self.logfile)
        # 7.创建LoginA对象
        self.login = LoginA()
        self.loginout = LoginoutA()
        self.addvip = AddOrgVip()
        self.delete = DeleteOrgVip()
        # 8.打印日志
        self.log.info('****************************************用例开始！****************************************')
        self.log.info("------------START:test5_8加会员_个人_企业_同意.Add_PtoO_Agreee005_8.py------------")

    # 3.释放资源
    def tearDown(self):
        # 1.打印日志
        self.log.info("------------END:test5_8加会员_个人_企业_同意.Add_PtoO_Agreee005_8.py------------")
        self.log.info('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~用例结束！~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        # 2.关闭driver
        self.driver.quit()

    # 4.测试用例
    @ddt.data([spacename_1, orgname_1, orgname1_1, phone1_1, password1_1,
               phone2_1, password2_1, phone3_1, password3_1])
    @ddt.unpack
    def test_addAtoOAgree(self, spacename, orgname, orgname1, phone1, password1,
                          phone2, password2, phone3, password3):
        '''+企业会员:【管理员邀请：受邀企业对象拒绝】'''
        try:
            sleep(1)
            # 1.空间首页
            self.handleS.Kjlb_click()
            # 2.选择空间:测试空间123
            self.handleS.Kjlb_browseorgspaceByName_click(spacename)
            # 3.+会员
            self.addvip.addOrgVip(self.driver, orgname)
            # 4.退出账号,登录受邀账号处理消息
            # 4.1调用loginout模块:退出当前账号
            self.loginout.loginout(self.driver, 4)  # 空间页设置
            # 4.2调用loginA模块:登录受邀账号
            self.login.login(self.driver, phone3, password3)
            sleep(1)
            '''
                4.3 为临时性方案：由于云视界面还没有做元素获取封装,目前直接用driver.find....等方法获取元素
            '''
            # 4.3点击流程
            self.driver.find_element_by_id("com.yunlu6.stone:id/icon_flow").click()
            # 7.5点击消息第一条
            self.driver.find_element_by_id("com.yunlu6.stone:id/reminditem_content").click()
            # 7.6点击同意 (拒绝com.yunlu6.stone:id/ass_invite_cancle)
            self.driver.find_element_by_id("com.yunlu6.stone:id/agree_btn").click()
            # 7.7返回到云视
            self.driver.find_element_by_id("com.yunlu6.stone:id/title_back_icon").click()
            self.driver.find_element_by_id("com.yunlu6.stone:id/buildstione_backe").click()
            # 7.8退出受邀账号
            self.loginout.loginout(self.driver, 1)
            # 8.登录管理员账号-检查各处消息
            # 8.1登录
            self.login.login(self.driver, phone1, password1)
            sleep(1)
            '''
                8.2 为临时性方案：由于云视界面还没有做元素获取封装,目前直接用driver.find....等方法获取元素
            '''
            # 8.2点击流程
            self.driver.find_element_by_id("com.yunlu6.stone:id/icon_flow").click()
            # 8.3查看消息第一条
            message = self.driver.find_element_by_id("com.yunlu6.stone:id/reminditem_content").text
            assert message == orgname + ' 机构已确认 贵公司的企业会员邀请', "Error Message Handled"
            # 8.4返回-空间主界面
            self.driver.find_element_by_id("com.yunlu6.stone:id/buildstione_backe").click()
            # 8.5进入列表处理同意消息
            # 8.5.1 进入空间列表
            self.handleS.Kjlb_click()
            # 8.5.2 进入[协会测试789]协会
            self.handleS.Kjlb_browseorgspaceByName_click(spacename)
            # 8.5.3 菜单栏-会员-菜单栏-管理
            self.handleS.Kjlb_browseascspace_menu_click()  # 菜单栏
            self.handleS.Kjlb_browseascspace_menu_vip_click()  # 会员
            self.handleS.Kjlb_browseascspace_menu_vip_menu_click()  # 菜单栏
            self.handleS.Kjlb_browseascspace_menu_vip_menu_manage_click()  # 管理
            # 8.5.4 编辑-选中-同意
            self.handleS.Kjlb_browseascspace_menu_vip_menu_manage_edit_click()  # 编辑
            self.handleS.Kjlb_browseascspace_menu_vip_menu_manage_edit_choosecompany_click(0)  # 选中
            self.handleS.Kjlb_browseascspace_menu_vip_menu_manage_edit_agree_click()  # 同意
            # 8.5.5 取消
            self.handleS.Kjlb_browseascspace_menu_vip_menu_manage_edit_cancel_click()  # 取消
            self.handleS.Kjlb_browseascspace_menu_vip_back_click()  # 返回
            self.handleS.Kjlb_browseascspace_menu_vip_back_click()  # 返回->协会名片首页
            # 8.5.6 企业会员
            self.handleS.Kjlb_browseascspace_ovip_click()  # 企业会员
            spacenamee = self.handleS.Kjlb_browseascspace_ovip_olist()[0].text
            assert spacenamee == orgname1, "Error: Asccoation Vip Add Failed!"  # 判断明月俱乐部是否加入成功
            self.handleS.Kjlb_browseascspace_ovip_back_click()  # 返回->协会名片首页
            # 9.还原测试场景
            '''
            9. 为临时方案,接口改动之前有效
            '''
            # #9.1空间列表
            # self.handleS.Kjlb_click()
            # #9.2进入空间
            # self.handleS.Kjlb_browseorgspaceByName_click(self.spacename)
            # 9.3会员中移除企业
            self.delete.deletOrgVip(self.driver, 0)
            # 9.4退出登录，登录邀请账号
            self.loginout.loginout(self.driver, 4)  # 退出登录
            self.login.login(self.driver, phone2, password2)  # 登录邀请账号
        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("Add_PtoO_Agree Outside : %s" % err)
            raise err
