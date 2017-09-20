__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import unittest
from time import sleep
import logging

from StoneUIFramework.public.common.Connect import Connect
from StoneUIFramework.public.common.publicfunction import Tools
from StoneUIFramework.config.globalparam import GlobalParam
from StoneUIFramework.public.handle.space.SPACEHANDLE5 import _SPACEHANDLE5
from StoneUIFramework.public.handle.login.LOGINHANDLE2 import _LOGINHANDLE2
from StoneUIFramework.testcase.空间.协会空间.test5_3加会员_管理员_个人_同意.AddPerVip import AddPerVip
from StoneUIFramework.testcase.空间.协会空间.test4_1会员_个人_移除.DeletePerVip import DeletePerVip
from StoneUIFramework.testcase.登录.test1_1登录.LoginA import LoginA
from StoneUIFramework.testcase.登录.test2_1退出登录.LoginoutA import LoginoutA
from StoneUIFramework.public.common.datainfo import DataInfo

#加会员_个人_个人_同意
class AddPtoPAgreeA(unittest.TestCase):
    @classmethod#装饰器，类方法
    def setUpClass(self):#最开始执行
        #建立连接信息
        cnn = Connect()
        self.driver = cnn.connect()
        #创建工具类
        self.tools = Tools(self.driver)#tools工具
        #创建_LOGINHANDLE2和_SPACEHANDLE5公有定位控件对象
        self.handleL = _LOGINHANDLE2(self.driver)
        self.handleS = _SPACEHANDLE5(self.driver)
        #创建读取配置信息对象
        cf = GlobalParam('config','path_file.conf')
        #获取截图路径、日志路径、日志名
        self.screen_path = cf.getParam('space',"ass_path_005_4")#通过配置文件获取截图的路径
        self.log_path = cf.getParam('space',"log")#通过配置文件获取日志的路径
        self.logfile = cf.getParam('space',"logfile")#日志文件名
        sleep(1)
        #测试数据
        d = DataInfo("space.xls")#创建DataInfo()对象
        self.spacename = d.cell("test007-会员",5,1)               #协会测试123
        self.vipname = d.cell("test007-会员",5,2)                 #人脉姓名
        self.phone1 = int(d.cell("test007-会员",5,3))             #账号1:15102761413
        self.password1 =  int(d.cell("test007-会员",5,4))         #密码:12345678
        self.phone2 =  int(d.cell("test007-会员",5,5))            #账号2:13027104206
        self.password2 =  int(d.cell("test007-会员",5,6))         #密码2:12345678
        self.phone3 = int(d.cell("test007-会员",5,7))             #账号1:17607136211
        self.password3 =  int(d.cell("test007-会员",5,8))         #密码:12345678
        #创建LoginA对象
        self.login = LoginA()
        self.loginout = LoginoutA()
        self.addvip = AddPerVip()
        self.deleteVip = DeletePerVip()
    def test_addPtoPAgree(self):
        '''+个人会员:【管理员邀请-受邀个人对象同意】'''
        try:
            self.tools.getLog(self.logfile)#打印日志
            sleep(1)
        #1.空间首页
            self.handleS.Kjlb_click()
        #2.选择空间:测试空间123
            self.handleS.Kjlb_browseorgspaceByName_click(self.spacename)
        #3.+会员
            self.addvip.addPerVip(self.driver)
        #4.退出账号,登录受邀账号处理消息
            #4.1调用loginout模块:退出当前账号
            self.loginout.loginout(self.driver,4) #空间页设置
            #4.2调用loginA模块:登录受邀账号
            self.login.login(self.driver,self.phone3,self.password3)
            sleep(1)
            '''
                4.3 为临时性方案：由于云视界面还没有做元素获取封装,目前直接用driver.find....等方法获取元素
            '''
            #4.3点击流程
            self.driver.find_element_by_id("com.yunlu6.stone:id/icon_flow").click()
            #7.5点击消息第一条
            self.driver.find_element_by_id("com.yunlu6.stone:id/reminditem_content").click()
            #7.6点击同意
            self.driver.find_element_by_id("com.yunlu6.stone:id/invite_commit").click()
            #7.7返回到云视
            self.driver.find_element_by_id("com.yunlu6.stone:id/title_back_icon").click()
            self.driver.find_element_by_id("com.yunlu6.stone:id/buildstione_backe").click()
            #7.8检查空间是否有该协会
            self.handleS.Kjlb_click()
            assert self.handleS.Kjlb_browseorgspaceByName(self.spacename) is not None,"Error SpaceList Showing"
            #7.9退出受邀账号
            self.loginout.loginout(self.driver,4)
        #8.登录邀请账号-检查各处消息
            #8.1登录
            self.login.login(self.driver,self.phone1,self.password1)
            sleep(1)
            '''
                8.2 为临时性方案：由于云视界面还没有做元素获取封装,目前直接用driver.find....等方法获取元素
            '''
            #8.2点击流程
            self.driver.find_element_by_id("com.yunlu6.stone:id/icon_flow").click()
            #8.3查看消息第一条
            message = self.driver.find_element_by_id("com.yunlu6.stone:id/reminditem_content").text
            assert message == self.vipname +' 已接受 贵公司的 会员 邀请',"Error Message Handled"
            #8.4返回-空间主界面
            self.driver.find_element_by_id("com.yunlu6.stone:id/buildstione_backe").click()
        #9.移除会员,还原测试场景
            #9.1进入空间
            self.handleS.Kjlb_click()
            #9.2选择协会
            self.handleS.Kjlb_browseorgspaceByName_click(self.spacename)
            #9.3会员_个人_移除
            self.deleteVip.deletePerVip(self.driver)
        #10.退出该账号,回到邀请账号
            self.loginout.loginout(self.driver,4)
            self.login.login(self.driver,self.phone2,self.password2)
            assert self.driver.find_elements_by_id("com.yunlu6.stone:id/sv_cloundview") != [] ,"Error Login Account2 Failed"
        except Exception as err:
            self.tools.getScreenShot(self.screen_path,"ExceptionShot")
            logging.error("Error_005_4 Information Add_AtoP_Agree Outside : %s"%err)
            raise err
        finally:
            self.driver.quit()