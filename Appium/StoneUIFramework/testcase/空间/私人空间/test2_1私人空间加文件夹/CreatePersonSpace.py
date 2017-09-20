__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from time import sleep
import logging
from StoneUIFramework.public.handle.space.SPACEHANDLE5 import _SPACEHANDLE5

#创建机构空间
class CreatePersonSpace:
    def __init__(self):#初始化测试数据
        pass
    def createPersonSpace(self,driver,spacename,foldername1 = None,foldername2 = None,foldername3 = None):#最多三个文件夹
        #创建_SPACEHANDLE5公有定位控件对象
        handle = _SPACEHANDLE5(driver)
        sleep(2)
        try:
        # #1.空间首页
        #     handle.Kjlb_click()
        #2.右上角主菜单
            handle.Kjlb_mainmenu_click()
        #3.+私人空间
            handle.Kjlb_mainmenu_newpersonspace_click()
        #4.输入空间名称、文件夹名-保存
            handle.Kjlb_mainmenu_newpersonspace_choosespacetype_click(0)#选择衣服类型空间
            handle.Kjlb_mainmenu_newpersonspace_spacename_sendkeys(spacename)#appium私人空间
            # handle.Kjlb_mainmenu_newpersonspace_foldername_sendkeys(foldername1)#appium文件夹
            handle.Kjlb_mainmenu_newpersonspace_save_click()#保存
        #6.返回到空间列表
            handle.Kjlb_mainmenu_newpersonspace_mainback_click()
        except Exception as err:
            logging.error("Error Information CreatePersonSpace Inside : %s"%err)
            raise err