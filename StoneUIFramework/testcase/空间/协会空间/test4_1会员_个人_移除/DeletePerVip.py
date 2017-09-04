__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from time import sleep
import logging
from StoneUIFramework.public.handle.space.SPACEHANDLE5 import _SPACEHANDLE5
from StoneUIFramework.public.common.datainfo import DataInfo

# 移除个人会员
class DeletePerVip:
    def __init__(self):  
        #初始化测试数据
        d = DataInfo("space.xls")  #创建DataInfo()对象
        self.vipname = d.cell("test007-会员",2,2)             #人脉姓名

    def deletePerVip(self, driver):
        '''移除个人会员'''
        #创建_SPACEHANDLE5公有定位控件对象
        self.handleS = _SPACEHANDLE5(driver)
        sleep(1)
        try:
        # #1.进入空间
        #     self.handleS.Kjlb_click()
        # #2.选择协会
        #     self.handleS.Kjlb_browseorgspaceByName_click(spacename)
        #3.菜单栏
            self.handleS.Kjlb_browseascspace_menu_click()
        #4.会员
            self.handleS.Kjlb_browseascspace_menu_vip_click()
        #5.个人名录
            self.handleS.Kjlb_browseascspace_menu_vip_personlist_click()
        #6.菜单栏
            self.handleS.Kjlb_browseascspace_menu_vip_menu_click()
        #7.管理
            self.handleS.Kjlb_browseascspace_menu_vip_menu_manage_click()
        #8.编辑
            self.handleS.Kjlb_browseascspace_menu_vip_menu_manage_edit_click()
        #9.勾选个人
            self.handleS.Kjlb_browseascspace_menu_vip_menu_manage_edit_chooseperson_click(0)
        #10.移除
            self.handleS.Kjlb_browseascspace_menu_vip_menu_manage_edit_delete_click()
        #11.返回空间主界面
            self.handleS.Kjlb_browseascspace_menu_vip_menu_manage_edit_cancel_click()   #取消->编辑页
            self.handleS.Kjlb_browseascspace_menu_vip_menu_manage_back_click()          #编辑界面返回->管理页
            self.handleS.Kjlb_browseascspace_menu_vip_back_click()                      #管理界面返回->名片页
            self.handleS.Kjlb_browseascspace_back_click()                               #返回到空间列表
        except Exception as err:
            logging.error("Error Information DeletePerVip Inside : %s" % err)
            raise err