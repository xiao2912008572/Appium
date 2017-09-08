__author__ = 'Administrator'
#coding=utf-8
from time import sleep
import logging

from StoneUIFramework.public.common.publicfunction import Tools
from StoneUIFramework.config.globalparam import GlobalParam
from StoneUIFramework.public.handle.space.SPACEHANDLE5 import _SPACEHANDLE5

#上架产品
class DeleteProduct:
    def __init__(self):#初始化测试数据
       pass
    def deleteProduct(self,driver):
        try:
            #创建工具类
            self.tools = Tools(driver)#tools工具
            #创建_SPACEHANDLE5公有定位控件对象
            self.handle = _SPACEHANDLE5(driver)
            sleep(1)
            #-----------------删除产品-----------------
        #1.点击菜单栏
            self.handle.Kjlb_browseorgspace_menu_product_unlock_list_menu_click()#点击菜单栏
        #2.点击删除
            self.handle.Kjlb_browseorgspace_menu_product_unlock_list_menu_delete_click()#删除产品
        except Exception as err:
            logging.error("Error Information DeleteProduct Inside : %s"%err)
            raise err