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
from StoneUIFramework.testcase.空间.协会空间.test5_7加会员_管理员_企业_同意.AddOrgVip import AddOrgVip
from StoneUIFramework.testcase.空间.协会空间.test4_4会员_企业_移除.DeleteOrgVip import DeleteOrgVip
from StoneUIFramework.testcase.登录.test1_1登录.LoginA import LoginA
from StoneUIFramework.testcase.登录.test2_1退出登录.LoginoutA import LoginoutA
from StoneUIFramework.public.common.datainfo import DataInfo

#加会员_个人_企业_同意
class AddPtoOAgree(unittest.TestCase):
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
        self.screen_path = cf.getParam('space',"ass_path_005_8")#通过配置文件获取截图的路径
        self.log_path = cf.getParam('space',"log")#通过配置文件获取日志的路径
        self.logfile = cf.getParam('space',"logfile")#日志文件名
        sleep(1)
        #测试数据
        d = DataInfo("space.xls")#创建DataInfo()对象
        self.spacename = d.cell("test007-会员",9,1)               #协会测试789
        self.orgname = d.cell("test007-会员",9,2)                 #明月
        self.orgname1 = d.cell("test007-会员",9,9)                #明月俱乐部
        self.phone1 = int(d.cell("test007-会员",9,3))             #账号1:15102761413
        self.password1 =  int(d.cell("test007-会员",9,4))         #密码:12345678
        self.phone2 =  int(d.cell("test007-会员",9,5))            #账号2:13027104206
        self.password2 =  int(d.cell("test007-会员",9,6))         #密码2:12345678
        self.phone3 = int(d.cell("test007-会员",9,7))             #账号3:17607136211
        self.password3 =  int(d.cell("test007-会员",9,8))         #密码3:12345678
        #创建LoginA对象
        self.login = LoginA()
        self.loginout = LoginoutA()
        self.addvip = AddOrgVip()
        self.delete = DeleteOrgVip()
    def test_addAtoOAgree(self):
        '''+企业会员:【管理员邀请：受邀企业对象拒绝】'''
        try:
            self.tools.getLog(self.logfile)#打印日志
            sleep(1)
        #1.空间首页
            self.handleS.Kjlb_click()
        #2.选择空间:测试空间123
            self.handleS.Kjlb_browseorgspaceByName_click(self.spacename)
        #3.+会员
            self.addvip.addOrgVip(self.driver,self.orgname)
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
            #7.6点击同意 (拒绝com.yunlu6.stone:id/ass_invite_cancle)
            self.driver.find_element_by_id("com.yunlu6.stone:id/ass_invite_commit").click()
            #7.7返回到云视
            self.driver.find_element_by_id("com.yunlu6.stone:id/title_back_icon").click()
            self.driver.find_element_by_id("com.yunlu6.stone:id/buildstione_backe").click()
            #7.8退出受邀账号
            self.loginout.loginout(self.driver,1)
        #8.登录管理员账号-检查各处消息
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
            assert message == self.orgname +' 机构已确认 贵公司的企业会员邀请',"Error Message Handled"
            #8.4返回-空间主界面
            self.driver.find_element_by_id("com.yunlu6.stone:id/buildstione_backe").click()
        #8.5进入列表处理同意消息
            #8.5.1 进入空间列表
            self.handleS.Kjlb_click()
            #8.5.2 进入[协会测试789]协会
            self.handleS.Kjlb_browseorgspaceByName_click(self.spacename)
            #8.5.3 菜单栏-会员-菜单栏-管理
            self.handleS.Kjlb_browseascspace_menu_click()                   #菜单栏
            self.handleS.Kjlb_browseascspace_menu_vip_click()               #会员
            self.handleS.Kjlb_browseascspace_menu_vip_menu_click()          #菜单栏
            self.handleS.Kjlb_browseascspace_menu_vip_menu_manage_click()   #管理
            #8.5.4 编辑-选中-同意
            self.handleS.Kjlb_browseascspace_menu_vip_menu_manage_edit_click()                  #编辑
            self.handleS.Kjlb_browseascspace_menu_vip_menu_manage_edit_choosecompany_click(0)   #选中
            self.handleS.Kjlb_browseascspace_menu_vip_menu_manage_edit_agree_click()            #同意
            #8.5.5 取消
            self.handleS.Kjlb_browseascspace_menu_vip_menu_manage_edit_cancel_click()           #取消
            self.handleS.Kjlb_browseascspace_menu_vip_back_click()                              #返回
            self.handleS.Kjlb_browseascspace_menu_vip_back_click()                              #返回->协会名片首页
            #8.5.6 企业会员
            self.handleS.Kjlb_browseascspace_ovip_click()                                       #企业会员
            spacename = self.handleS.Kjlb_browseascspace_ovip_olist()[0].text
            # print('spacename =',spacename)
            # print('self.orgname1 =',self.orgname1)
            assert spacename == self.orgname1,"Error: Asccoation Vip Add Failed!"               #判断明月俱乐部是否加入成功
            self.handleS.Kjlb_browseascspace_ovip_back_click()                                  #返回->协会名片首页
        #9.还原测试场景
            '''
            9. 为临时方案,接口改动之前有效
            '''
            # #9.1空间列表
            # self.handleS.Kjlb_click()
            # #9.2进入空间
            # self.handleS.Kjlb_browseorgspaceByName_click(self.spacename)
            #9.3会员中移除企业
            self.delete.deletOrgVip(self.driver,0)
            #9.4退出登录，登录邀请账号
            self.loginout.loginout(self.driver,4)                                              #退出登录
            self.login.login(self.driver,self.phone2,self.password2)                           #登录邀请账号
        except Exception as err:
            self.tools.getScreenShot(self.screen_path,"ExceptionShot")
            logging.error("Error_005_8 Information Add_PtoO_Agree Outside : %s"%err)
            raise err
        finally:
            self.driver.quit()