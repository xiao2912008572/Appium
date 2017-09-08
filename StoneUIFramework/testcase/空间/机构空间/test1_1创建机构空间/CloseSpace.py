__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from time import sleep
import logging
from StoneUIFramework.config.globalparam import GlobalParam
from StoneUIFramework.public.common.publicfunction import Tools
from StoneUIFramework.public.handle.space.SPACEHANDLE5 import _SPACEHANDLE5
from StoneUIFramework.public.common.datainfo import DataInfo

#关闭机构空间
class CloseSpace:
    def closeSpace(self,driver):
        """
            菜单栏用坐标定位：34行，实属无奈之举
        """
        #创建工具类
        tools = Tools(driver)#tools工具
        #创建_SPACEHANDLE5公有定位控件对象
        handle = _SPACEHANDLE5(driver)
        #测试数据
        d = DataInfo("space.xls")#创建DataInfo()对象
        # self.easyname = d.cell("test001",2,2,)
        self.menu_x = int(d.cell("test001-创建",2,11))#fullname
        self.menu_y = int(d.cell("test001-创建",2,12,))#easyname
        sleep(1)
        try:
            #为了保证不中途退出，需要第一次进入的时候检查是否存在该机构，如果存在，先关闭
            handle.Kjlb_browseorgspaceByID_click(0)#点击进入
            sleep(1)
            handle.Kjlb_browseorgspace_menu_click()#菜单栏
            handle.Kjlb_browseorgspace_menu_bcard_click()#企业名片
            handle.Kjlb_browseorgspace_menu_bcard_menu_click()#菜单栏
            handle.Kjlb_browseorgspace_menu_bcard_menu_close_click()#关闭
            handle.Kjlb_browseorgspace_menu_bcard_menu_close_confirm_click()#确认关闭
        except Exception as err:
            logging.error("Error Information CloseSpace Inside : %s"%err)
            raise err