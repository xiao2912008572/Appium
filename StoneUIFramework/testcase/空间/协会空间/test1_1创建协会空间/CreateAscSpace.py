__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from time import sleep
import logging
from StoneUIFramework.public.common.publicfunction import Tools
from StoneUIFramework.public.handle.space.SPACEHANDLE5 import _SPACEHANDLE5
from StoneUIFramework.public.common.datainfo import DataInfo

#创建机构空间
class CreateAscSpace:
    def __init__(self):#初始化测试数据
        d = DataInfo("space.xls")#创建DataInfo()对象
        self.province = (d.cell("test001-创建",2,4))#北京
        self.city = (d.cell("test001-创建",2,5))#东城
        self.soverbank = d.cell("test001-创建",2,7)#开户行
        self.sovermybank = d.cell("test001-创建",2,8)#支行
        self.soverbanknub = int(d.cell("test001-创建",2,9))#银行账号
        self.customertype = int(d.cell("test001-创建",2,3))#客户类型
        self.industry = int(d.cell("test001-创建",2,10))#产业角色
    def createAscSpace(self,driver,fullname,easyname):
        #创建工具类
        tools = Tools(driver)#tools工具
        #创建_SPACEHANDLE5公有定位控件对象
        handle = _SPACEHANDLE5(driver)
        sleep(1)
        try:
        #1.空间首页
            handle.Kjlb_click()
        #2.右上角主菜单
            handle.Kjlb_mainmenu_click()
        #3.+机构空间空间
            handle.Kjlb_mainmenu_newspace_click()
            #--------------------------新机构空间会空间-------------------------
            # 机构名称:(fullname):appium测试协会
            # 机构简称:(easyname):appium测试协会
            # 机构类型:企业
            # 产业角色:工厂
            # 客户类型:石材
            # 所在地区:北京-东城
            # 详细地址:不填
            handle.Kjlb_mainmenu_newspace_orgname_sendkeys(fullname)#全称
            handle.Kjlb_mainmenu_newspace_orgintro_sendkeys(easyname)#简称
            handle.Kjlb_mainmenu_newspace_orgtitle_click()#点击标题
            handle.Kjlb_mainmenu_newspace_orgtype_click()#机构类型
            handle.Kjlb_mainmenu_newspace_orgtype_association_click()#机构类型：企业
            sleep(1)
            # handle.Kjlb_mainmenu_newspace_industry_click()#产业角色
            # handle.Kjlb_mainmenu_newspace_industry_tag_click(self.industry)#选择工厂
            handle.Kjlb_mainmenu_newspace_customertype_click()#客户类型
            handle.Kjlb_mainmenu_newspace_customertype_tag_click(self.customertype)#客户类型标签
            handle.Kjlb_mainmenu_newspace_customertype_confirm_click()#点击确定
            handle.Kjlb_mainmenu_newspace_area_click()#所在地区
            driver.find_element_by_name(self.province).click()
            driver.find_element_by_name(self.city).click()
            # handle.Kjlb_mainmenu_newspace_area_address_click(self.province)#北京
            # handle.Kjlb_mainmenu_newspace_area_address_click(self.city)#东城
            handle.Kjlb_mainmenu_newspace_affirm_click()#点击提交

            #------------------------验证对公账号-------------------------------
            handle.Kjlb_mainmenu_newspace_verifynow_click()#点击去验证
            #开户银行:AAA
            #所在地区:北京-东城
            #支行:BBB
            #银行账号:123456
            handle.Kjlb_mainmenu_newspace_verifynow_soverbank_sendkeys(self.soverbank)#开户银行
            handle.Kjlb_mainmenu_newspace_verifynow_soveraddress_click()#所在地区
            # handle.Kjlb_mainmenu_newspace_verifynow_soveraddress_list_click(self.province)#北京
            # handle.Kjlb_mainmenu_newspace_verifynow_soveraddress_list_click(self.city)#东城
            driver.find_element_by_name(self.province).click()#北京
            driver.find_element_by_name(self.city).click()#东城
            handle.Kjlb_mainmenu_newspace_verifynow_sovermybank_sendkeys(self.sovermybank)#支行
            handle.Kjlb_mainmenu_newspace_verifynow_soverbanknub_sendkeys(self.soverbanknub)#银行账户
            handle.Kjlb_mainmenu_newspace_verifynow_soversave_click()#确定提交
            sleep(1)
            handle.Kjlb_mainmenu_newspace_verifynow_soversave_back_click()#点击返回
            sleep(1)
        except Exception as err:
            logging.error("Error Information CreateSpace Inside : %s"%err)
            raise err