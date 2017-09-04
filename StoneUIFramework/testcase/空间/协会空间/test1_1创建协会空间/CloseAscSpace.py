__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from time import sleep
import logging
from StoneUIFramework.public.common.publicfunction import Tools
from StoneUIFramework.public.handle.space.SPACEHANDLE5 import _SPACEHANDLE5
from StoneUIFramework.public.common.datainfo import DataInfo

#关闭机构空间
class CloseAscSpace:
    def closeAsscSpace(self,driver,name):
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
            #1.进入协会空间
            handle.Kjlb_browseorgspaceByName_click(name)
            sleep(1)
            #2.点击菜单栏
            handle.Kjlb_browseascspace_menu_click()
            #3.点击关闭
            handle.Kjlb_browseascspace_menu_close_click()
            #4.关闭确认
            handle.Kjlb_browseascspace_menu_close_yes_click()
        except Exception as err:
            logging.error("Error Information CloseSpace Inside : %s"%err)
            raise err