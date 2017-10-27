__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from YunluIFramework.testcase.空间.协会空间.test5_1加会员_管理员_个人_拒绝 import *


# 加会员_管理员_个人_拒绝
@ddt.ddt
class AddAtoPRefuseA(unittest.TestCase):
    # 1.全局测试数据
    d = DataInfo("space.xls")  # 创建DataInfo()对象
    spacename_1 = d.cell("test007-会员", 2, 1)  # 协会测试123
    vipname_1 = d.cell("test007-会员", 2, 2)  # 人脉姓名
    phone1_1 = int(d.cell("test007-会员", 2, 3))  # 账号1:17607136211
    password1_1 = int(d.cell("test007-会员", 2, 4))  # 密码:12345678
    phone2_1 = int(d.cell("test007-会员", 2, 5))  # 账号2:13027104206
    password2_1 = int(d.cell("test007-会员", 2, 6))  # 密码2:12345678

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
        self.screen_path = cf.getParam('space', "ass_path_005_1")  # 通过配置文件获取截图的路径
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名
        # 6.创建日志记录模块
        self.log = Log(self.logfile)
        # 7. 创建LoginA对象
        self.login = LoginA()
        self.loginout = LoginoutA()
        self.addvip = AddPerVip()
        # 8.打印日志
        self.log.info('****************************************用例开始！****************************************')
        self.log.info("------------START:test5_1加会员_管理员_个人_拒绝.Add_AtoP_Refuse005_1.py------------")

    # 3.释放资源
    def tearDown(self):
        # 1.打印日志
        self.log.info("------------END:test5_1加会员_管理员_个人_拒绝.Add_AtoP_Refuse005_1.py------------")
        self.log.info('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~用例结束！~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        # 2.关闭driver
        self.driver.quit()

    # 4.测试用例
    @ddt.data([spacename_1, vipname_1, phone1_1, password1_1, phone2_1, password2_1])
    @ddt.unpack
    def test_addAtoPRefuse(self, spacename, vipname, phone1, password1, phone2, password2):
        '''+个人会员:【管理员邀请-受邀个人对象拒绝】'''
        try:
            sleep(1)
            # 1.空间首页
            self.handleS.Kjlb_click()
            self.log.info('点击空间首页')
            # 2.选择空间:协会测试123
            self.handleS.Kjlb_browseorgspaceByName_click(spacename)
            self.log.info('进入协会空间：{0}'.format(spacename))
            # 3.+会员
            self.addvip.addPerVip(self.driver, vipname)
            # 4.退出账号,登录受邀账号处理消息
            # 4.1调用loginout模块:退出当前账号
            self.loginout.loginout(self.driver, 4)  # 空间页设置
            # 4.2调用loginA模块:登录受邀账号
            self.login.login(self.driver, phone1, password1)
            sleep(1)
            '''
                4.3 为临时性方案：由于云视界面还没有做元素获取封装,目前直接用driver.find....等方法获取元素
            '''
            # 4.3点击流程
            self.driver.find_element_by_id("com.yunlu6.stone:id/icon_flow").click()
            self.log.info('点击流程')
            # 7.5点击消息第一条
            self.driver.find_element_by_id("com.yunlu6.stone:id/reminditem_content").click()
            self.log.info('点击第1条消息')
            # 7.6点击拒绝
            self.driver.find_element_by_id("com.yunlu6.stone:id/refuse_btn").click()
            self.log.info('点击拒绝')
            # 7.7返回到云视
            self.driver.find_element_by_id("com.yunlu6.stone:id/buildstione_backe").click()
            self.log.info('点击返回云视')
            # 7.8退出受邀账号
            self.loginout.loginout(self.driver, 1)
            # 8.登录邀请账号-检查各处消息
            # 8.1登录
            self.login.login(self.driver, phone2, password2)
            sleep(1)
            '''
                8.2 为临时性方案：由于云视界面还没有做元素获取封装,目前直接用driver.find....等方法获取元素
            '''
            # 8.2点击流程
            self.driver.find_element_by_id("com.yunlu6.stone:id/icon_flow").click()
            self.log.info('点击流程')
            # 8.3查看消息第一条
            message = self.driver.find_element_by_id("com.yunlu6.stone:id/reminditem_content").text
            self.log.info('查看第1条消息')
            assert message == vipname + ' 回绝邀请 贵公司的 会员 邀请', "Error Message Handled"
            self.log.info('检查是否收到拒绝消息')
            # 8.4返回-空间主界面
            self.driver.find_element_by_id("com.yunlu6.stone:id/buildstione_backe").click()
            self.log.info('点击返回，返回至空间主界面')
        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("Add_AtoP_Refuse Outside : %s" % err)
            raise err
