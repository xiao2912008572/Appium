__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from time import sleep
import logging
from StoneUIFramework.public.common.publicfunction import Tools
from StoneUIFramework.public.handle.space.SPACEHANDLE5 import _SPACEHANDLE5

#删除资讯
class DeleteArchivies:
    def __init__(self):#初始化测试数据
        pass
    def deletearchivies(self,driver,spacename):
        #创建工具类
        tools = Tools(driver)#tools工具
        #创建_SPACEHANDLE5公有定位控件对象
        handle = _SPACEHANDLE5(driver)
        sleep(1)
        try:
        #1.空间首页
            handle.Kjlb_click()
        #2.选择空间:测试空间123
            handle.Kjlb_browseorgspaceByName_click(spacename)
        #3.右上角:菜单栏选择资讯
            handle.Kjlb_browseorgspace_menu_click()
            handle.Kjlb_browseorgspace_menu_archivies_click()
        #4.判断是否有图片，有就进入删除
            #4.1判断-点击第1张图片-点击第1张图片
            if handle.Kjlb_browseorgspace_menu_archivies_pic != []:
                handle.Kjlb_browseorgspace_menu_archivies_pic_click(0)
                handle.Kjlb_browseorgspace_menu_archivies_pic_click(0)
            #4.2菜单栏
                handle.Kjlb_browseorgspace_menu_archivies_pic_menu_click()
            #4.3下架
                handle.Kjlb_browseorgspace_menu_archivies_pic_menu_offshelf_click()
            #4.4点击第1张图片
                handle.Kjlb_browseorgspace_menu_archivies_pic_click(0)
                handle.Kjlb_browseorgspace_menu_archivies_pic_click(0)
            #4.4菜单栏
                handle.Kjlb_browseorgspace_menu_archivies_pic_menu_click()
            #4.5删除
                handle.Kjlb_browseorgspace_menu_archivies_pic_menu_delete_click()
            #4.6返回-空间主界面
                handle.Kjlb_browseorgspace_menu_archivies_back_click()
        #5.删除检查
                handle.Kjlb_browseorgspaceByName_click(spacename)
            #5.1菜单栏
                handle.Kjlb_browseorgspace_menu_click()
            #5.1资讯
                handle.Kjlb_browseorgspace_menu_archivies_click()
            #5.3判断
                assert [] == handle.Kjlb_browseorgspace_menu_archivies_pic,'Error Pic Delete Failed!'
        except Exception as err:
            logging.error("Error Information DeleteArchivies Inside : %s"%err)
            raise err