__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from time import sleep
from StoneUIFramework.config.globalparam import GlobalParam
from StoneUIFramework.public.handle.space.SPACEHANDLE5 import _SPACEHANDLE5
from StoneUIFramework.public.common.datainfo import DataInfo
from StoneUIFramework.public.common.log import Log

#创建机构空间
class CreateSpace:
    def __init__(self):
        #初始化测试数据
        d = DataInfo("space.xls")#创建DataInfo()对象
        self.province = (d.cell("test001-创建",2,4))#北京
        self.city = (d.cell("test001-创建",2,5))#东城
        self.soverbank = d.cell("test001-创建",2,7)#开户行
        self.sovermybank = d.cell("test001-创建",2,8)#支行
        self.soverbanknub = int(d.cell("test001-创建",2,9))#银行账号
        self.customertype = int(d.cell("test001-创建",2,3))#客户类型
        self.industry = int(d.cell("test001-创建",2,10))#产业角色
        #创建读取配置信息对象
        cf = GlobalParam('config','path_file.conf')
        #获取截图路径、日志路径、日志名
        self.logfile = cf.getParam('log',"logfile")#日志文件名
        #创建日志模块
        self.log = Log(self.logfile)
    def createSpace(self,driver,fullname,easyname):
        #创建_SPACEHANDLE5公有定位控件对象
        handle = _SPACEHANDLE5(driver)
        sleep(1)
        try:
        #1.空间首页
            self.log.info('------START:test1_1创建机构空间.CreateSpace.py------')
            handle.Kjlb_click()
            self.log.info('点击进入空间首页')
        #2.点击+按钮
            handle.Kjlb_mainmenu_click()
            self.log.info('点击+按钮')
        #3.+机构空间
            handle.Kjlb_mainmenu_newspace_click()
            self.log.info('选择+机构空间')
            #--------------------------新建机构空间-------------------------
            # 机构名称:(fullname):appium测试空间
            # 机构简称:(easyname):appium测试空间
            # 机构类型:企业
            # 产业角色:工厂
            # 客户类型:石材
            # 所在地区:北京-东城
            # 详细地址:不填
            handle.Kjlb_mainmenu_newspace_orgname_sendkeys(fullname)#全称
            self.log.info('输入企业全称：%s'%fullname)
            handle.Kjlb_mainmenu_newspace_orgintro_sendkeys(easyname)#简称
            self.log.info('输入企业简称：%s'%easyname)
            handle.Kjlb_mainmenu_newspace_orgtitle_click()#点击标题
            self.log.info('点击标题')
            handle.Kjlb_mainmenu_newspace_orgtype_click()#机构类型
            self.log.info('点击机构类型')
            handle.Kjlb_mainmenu_newspace_orgtype_company_click()#机构类型：企业
            self.log.info('选择机构类型：企业')
            sleep(1)
            handle.Kjlb_mainmenu_newspace_industry_click()#产业角色
            self.log.info('点击产业角色')
            handle.Kjlb_mainmenu_newspace_industry_tag_click(self.industry)#选择工厂
            self.log.info('产业角色选择：%s'%self.industry)
            handle.Kjlb_mainmenu_newspace_customertype_click()#客户类型
            self.log.info('点击客户类型')
            handle.Kjlb_mainmenu_newspace_customertype_tag_click(self.customertype)#客户类型标签
            self.log.info('点击客户类型标签')
            handle.Kjlb_mainmenu_newspace_customertype_confirm_click()#点击确定
            self.log.info('点击确定按钮')
            handle.Kjlb_mainmenu_newspace_area_click()#所在地区
            self.log.info('点击所在地区')
            driver.find_element_by_name(self.province).click()
            self.log.info('选择%s省'%self.province)
            driver.find_element_by_name(self.city).click()
            self.log.info('选择%s市'%self.city)
            # handle.Kjlb_mainmenu_newspace_area_address_click(self.province)#北京
            # handle.Kjlb_mainmenu_newspace_area_address_click(self.city)#东城
            handle.Kjlb_mainmenu_newspace_affirm_click()#点击提交
            self.log.info('确定提交')

            #------------------------验证对公账号-------------------------------
            handle.Kjlb_mainmenu_newspace_verifynow_click()#点击去验证
            self.log.info('点击去验证对公账号')
            #开户银行:AAA
            #所在地区:北京-东城
            #支行:BBB
            #银行账号:123456
            handle.Kjlb_mainmenu_newspace_verifynow_soverbank_sendkeys(self.soverbank)#开户银行
            self.log.info('填写开户银行：%s'%self.soverbank)
            handle.Kjlb_mainmenu_newspace_verifynow_soveraddress_click()#所在地区
            handle.Kjlb_mainmenu_newspace_verifynow_soveraddress_list_click(self.province)#北京
            handle.Kjlb_mainmenu_newspace_verifynow_soveraddress_list_click(self.city)#东城
            driver.find_element_by_name(self.province).click()#北京
            self.log.info('选择%s省'%self.province)
            driver.find_element_by_name(self.city).click()#东城
            self.log.info('选择%s市'%self.city)
            handle.Kjlb_mainmenu_newspace_verifynow_sovermybank_sendkeys(self.sovermybank)#支行
            self.log.info('填写支行：%s'%self.sovermybank)
            handle.Kjlb_mainmenu_newspace_verifynow_soverbanknub_sendkeys(self.soverbanknub)#银行账户
            self.log.info('填写银行账户：%s'%self.soverbanknub)
            handle.Kjlb_mainmenu_newspace_verifynow_soversave_click()#确定提交
            self.log.info('确定提交')
            sleep(1)
            handle.Kjlb_mainmenu_newspace_verifynow_soversave_back_click()#点击返回
            self.log.info('点击返回')
            sleep(1)

            #bug没改之前这么处理，手动点击取消按钮
            driver.find_element_by_id("com.yunlu6.stone:id/cloundviewbottom_cancle").click()
            self.log.info('点击取消按钮')
            self.log.info('------END:test1_1创建机构空间.CreateSpace.py------')
        except Exception as err:
            self.log.error("CreateSpace Inside : %s"%err)
            raise err