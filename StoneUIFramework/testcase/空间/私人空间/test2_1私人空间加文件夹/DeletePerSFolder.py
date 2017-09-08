__author__ = 'Administrator'
# -*- coding: utf-8 -*-

from time import sleep
import logging
from StoneUIFramework.public.handle.space.SPACEHANDLE5 import _SPACEHANDLE5
from StoneUIFramework.public.common.datainfo import DataInfo

#关闭私人空间
class DeletePerSFloder:
    def deletePerSFloder(self,driver,spacename):
        #创建 _SPACEHANDLE5公有定位控件对象
        handle = _SPACEHANDLE5(driver)
        #测试数据
        d = DataInfo("space.xls")
        self.spacename = d.cell("test006-私人空间",2,13,)#私人空间名
        sleep(2)
        try:
        #1.点击该空间
            handle.Kjlb_browseorgspaceByName_click(spacename)
            if driver.find_element_by_id("com.yunlu6.stone:id/personzone_item_foldernum").text != "(0)":#判断文件夹是否为空
            #2.菜单栏
                handle.Kjlb_browseperspace_menu_click()
            #3.编辑
                handle.Kjlb_browseperspace_menu_edit_click()
            #4.删除文件夹
                #4.1删除文件夹(此时不为空)
                handle.Kjlb_browseperspace_more_menu_edit_deletefolder_click(0)
                #4.2照片列表
                handle.Kjlb_browseperspace_more_menu_edit_deletefolder_piclist_click(0)
                #4.3删除
                handle.Kjlb_browseperspace_more_menu_edit_deletefolder_dbtn_click()
                #4.4是
                handle.Kjlb_browseperspace_more_menu_edit_deletefolder_dbtn_y_click()
                #4.5删除文件夹(为空)
                handle.Kjlb_browseperspace_more_menu_edit_deletefolder_click(0)
                driver.find_element_by_id("com.yunlu6.stone:id/edit_folder_ok").click()
            else:
                #4.5.菜单栏
                handle.Kjlb_browseperspace_menu_click()
                #4.6.编辑
                handle.Kjlb_browseperspace_menu_edit_click()
                #4.7删除文件夹(为空)
                handle.Kjlb_browseperspace_more_menu_edit_deletefolder_click(0)
                driver.find_element_by_id("com.yunlu6.stone:id/edit_folder_ok").click()
        #5.返回空间列表
            handle.Kjlb_browseperspace_more_menu_edit_back_click()
        except Exception as err:
            logging.error("Error Information CloseSpace Inside : %s"%err)
            raise err