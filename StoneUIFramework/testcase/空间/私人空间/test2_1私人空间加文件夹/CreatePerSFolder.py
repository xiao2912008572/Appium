__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from time import sleep
import logging
from StoneUIFramework.public.common.publicfunction import Tools
from StoneUIFramework.public.handle.space.SPACEHANDLE5 import _SPACEHANDLE5
from StoneUIFramework.public.common.datainfo import DataInfo

#创建机构空间
class CreatePerSFolder:
    def __init__(self):#初始化测试数据
        d = DataInfo("space.xls")#创建DataInfo()对象
        self.foldername1 = d.cell("test006-私人空间",2,14)#文件夹1:appium文件夹
    def createPerSFolder(self,driver,spacename,foldername1 = None,foldername2 = None,foldername3 = None):#最多三个文件夹
        #创建工具类
        tools = Tools(driver)#tools工具
        #创建_SPACEHANDLE5公有定位控件对象
        handle = _SPACEHANDLE5(driver)
        sleep(2)
        try:
        #1.空间-菜单栏
            driver.find_element_by_name(spacename).click()
            # handle.Kjlb_browseperspaceByName(spacename).click()
            handle.Kjlb_browseperspace_menu_click()
        #2.+文件夹
            handle.Kjlb_browseperspace_menu_addfolder_click()
        #3.输入文件夹名称-确定
            handle.Kjlb_browseperspace_menu_addfolder_foldername_sendkeys(foldername1)
            handle.Kjlb_browseperspace_menu_addfolder_confirm_click()
        #4.检查文件夹是否成功新建
            foldername = handle.Kjlb_browseperspace_foldername()[0].text
            assert self.foldername1 == foldername,"Error : Floder Name Is Wrong"
        #5.+数据:相册-照片列表-完成
            #5.1+数据
            handle.Kjlb_browseperspace_piclist_click(0)
            #5.2相册方式
            handle.Kjlb_browseperspace_addData_ByAlbum_click()
            #5.3点击第一张照片
            handle.Kjlb_browseperspace_addData_ByAlbum_piclist_click(0)
            #5.4完成
            handle.Kjlb_browseperspace_addData_ByAlbum_confirm_click()
            sleep(1)
            #5.5返回控件主页
            handle.Kjlb_browseperspace_addData_ByAlbum_confirm_back_click()
        #6.检查上传是否成功
            picLen = len(handle.Kjlb_browseperspace_piclist())#照片列表长度应该为2
            assert picLen == 2,'Error : Picture Upload Failed'
        #7.返回
            handle.Kjlb_browseperspace_back_click()
        except Exception as err:
            logging.error("Error Information CreatePerSFolder Inside : %s"%err)
            raise err