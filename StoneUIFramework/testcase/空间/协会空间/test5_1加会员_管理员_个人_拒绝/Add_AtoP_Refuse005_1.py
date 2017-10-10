__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import unittest
from time import sleep

from StoneUIFramework.public.common.Connect import Connect
from StoneUIFramework.public.common.publicfunction import Tools
from StoneUIFramework.config.globalparam import GlobalParam
from StoneUIFramework.public.handle.space.SPACEHANDLE5 import _SPACEHANDLE5
from StoneUIFramework.public.handle.login.LOGINHANDLE2 import _LOGINHANDLE2
from StoneUIFramework.testcase.空间.协会空间.test5_1加会员_管理员_个人_拒绝.AddPerVip import AddPerVip
from StoneUIFramework.testcase.登录.test1_1登录.LoginA import LoginA
from StoneUIFramework.testcase.登录.test2_1退出登录.LoginoutA import LoginoutA
from StoneUIFramework.public.common.datainfo import DataInfo
from StoneUIFramework.public.common.log import Log


# 加会员_管理员_个人_拒绝
class AddAtoPRefuseA(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    @classmethod  # 装饰器，类方法
    def setUpClass(self):  # 最开始执行
        # 建立连接信息
        cnn = Connect()
        self.driver = cnn.connect()
        # 创建工具类
        self.tools = Tools(self.driver)  # tools工具
        # 创建_LOGINHANDLE2和_SPACEHANDLE5公有定位控件对象
        self.handleL = _LOGINHANDLE2(self.driver)
        self.handleS = _SPACEHANDLE5(self.driver)
        # 创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')
        # 获取截图路径、日志路径、日志名
        self.screen_path = cf.getParam('space', "ass_path_005_1")  # 通过配置文件获取截图的路径
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名
        # 创建日志记录模块
        self.log = Log(self.logfile)
        # 测试数据
        d = DataInfo("space.xls")  # 创建DataInfo()对象
        self.spacename = d.cell("test007-会员", 2, 1)  # 协会测试123
        self.vipname = d.cell("test007-会员", 2, 2)  # 人脉姓名
        self.phone1 = int(d.cell("test007-会员", 2, 3))  # 账号1:17607136211
        self.password1 = int(d.cell("test007-会员", 2, 4))  # 密码:12345678
        self.phone2 = int(d.cell("test007-会员", 2, 5))  # 账号2:13027104206
        self.password2 = int(d.cell("test007-会员", 2, 6))  # 密码2:12345678
        # 创建LoginA对象
        self.login = LoginA()
        self.loginout = LoginoutA()
        self.addvip = AddPerVip()

    def test_addAtoPRefuse(self):
        '''+个人会员:【管理员邀请-受邀个人对象拒绝】'''
        try:
            self.log.info("------------START:test5_1加会员_管理员_个人_拒绝.Add_AtoP_Refuse005_1.py------------")
            sleep(1)
            # 1.空间首页
            self.handleS.Kjlb_click()
            self.log.info('点击空间首页')
            # 2.选择空间:协会测试123
            self.handleS.Kjlb_browseorgspaceByName_click(self.spacename)
            self.log.info('进入协会空间：{0}'.format(self.spacename))
            # 3.+会员
            self.addvip.addPerVip(self.driver)
            # 4.退出账号,登录受邀账号处理消息
            # 4.1调用loginout模块:退出当前账号
            self.loginout.loginout(self.driver, 4)  # 空间页设置
            # 4.2调用loginA模块:登录受邀账号
            self.login.login(self.driver, self.phone1, self.password1)
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
            self.driver.find_element_by_id("com.yunlu6.stone:id/invite_cancle").click()
            self.log.info('点击拒绝')
            # 7.7返回到云视
            self.driver.find_element_by_id("com.yunlu6.stone:id/buildstione_backe").click()
            self.log.info('点击返回云视')
            # 7.8退出受邀账号
            self.loginout.loginout(self.driver, 1)
            # 8.登录邀请账号-检查各处消息
            # 8.1登录
            self.login.login(self.driver, self.phone2, self.password2)
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
            assert message == self.vipname + ' 回绝邀请 贵公司的 会员 邀请', "Error Message Handled"
            self.log.info('检查是否收到拒绝消息')
            # 8.4返回-空间主界面
            self.driver.find_element_by_id("com.yunlu6.stone:id/buildstione_backe").click()
            self.log.info('点击返回，返回至空间主界面')
            self.log.info("------------END:test5_1加会员_管理员_个人_拒绝.Add_AtoP_Refuse005_1.py------------")
        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("Add_AtoP_Refuse Outside : %s" % err)
            raise err
        finally:
            self.driver.quit()
