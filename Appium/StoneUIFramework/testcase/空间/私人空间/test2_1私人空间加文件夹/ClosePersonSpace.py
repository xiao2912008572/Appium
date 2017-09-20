__author__ = 'Administrator'
# -*- coding: utf-8 -*-

from time import sleep
import logging
from StoneUIFramework.public.handle.space.SPACEHANDLE5 import _SPACEHANDLE5

#关闭私人空间
class ClosePersonSpace:
    def closePersonSpace(self,driver,spacename):
        #创建_SPACEHANDLE5公有定位控件对象
        handle = _SPACEHANDLE5(driver)
        sleep(1)
        try:
            #1.点击该空间
            handle.Kjlb_browseorgspaceByName_click(spacename)
            #2.菜单栏
            handle.Kjlb_browseperspace_menu_click()
            #3.编辑
            handle.Kjlb_browseperspace_menu_edit_click()
            #4.删除空间
            handle.Kjlb_browseperspace_menu_edit_deletespace_click()
            handle.Kjlb_browseperspace_menu_edit_deletespace_OK_click()
        except Exception as err:
            logging.error("Error Information CloseSpace Inside : %s"%err)
            raise err