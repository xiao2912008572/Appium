__author__ = 'Administrator'
#coding=utf-8
from time import sleep
import logging

from StoneUIFramework.public.common.publicfunction import Tools
from StoneUIFramework.config.globalparam import GlobalParam
from StoneUIFramework.public.common.datainfo import DataInfo
from StoneUIFramework.public.handle.space.SPACEHANDLE5 import _SPACEHANDLE5

#上架产品
class CreateProduct:
    def __init__(self):#初始化测试数据
        #测试数据
        d = DataInfo("space.xls")#创建DataInfo()对象
        self.spacename = d.cell("test002-上架产品",2,1)#空间名
        self.photo = int(d.cell("test002-上架产品",2,2))#photo列表
        self.proname = d.cell("test002-上架产品",2,3)#商品名
        self.tag1 = int(d.cell("test002-上架产品",2,4))#tag1
        self.tag2 = int(d.cell("test002-上架产品",2,5))#tag2
        self.species = d.cell("test002-上架产品",2,6)#种类名
        self.type = int(d.cell("test002-上架产品",2,7))#制品
        self.surface = int(d.cell("test002-上架产品",2,8))#表面
        self.key = d.cell("test002-上架产品",2,9)#参数名
        self.value = d.cell("test002-上架产品",2,10)#参数值
        self.price1 = int(d.cell("test002-上架产品",2,11))#price1
        self.stock1 = int(d.cell("test002-上架产品",2,12))#stock1
        self.price2 = int(d.cell("test002-上架产品",2,13))#price2
        self.stock2 = d.cell("test002-上架产品",2,14)#stock2
        self.price3 = d.cell("test002-上架产品",2,15)#price3
        self.stock3 = int(d.cell("test002-上架产品",2,16))#stock3
        self.price4 = int(d.cell("test002-上架产品",2,17))#price4
        self.stock4 = int(d.cell("test002-上架产品",2,18))#stock4
        self.menu_x = int(d.cell("test002-上架产品",2,19))#menu_x
        self.menu_y = int(d.cell("test002-上架产品",2,20))#menu_y
    def createProduct(self,driver):
        """
            菜单栏用坐标定位：68行，实属无奈之举
        """
        try:
            #创建_SPACEHANDLE5公有定位控件对象
            handle = _SPACEHANDLE5(driver)
            sleep(1)
            #-----------------新建产品-----------------
            handle.Kjlb_browseorgspace_menu_product_new_click()#点击新建按钮
        #1.添加照片
            handle.Kjlb_browseorgspace_menu_product_new_addphoto_click()#点击添加照片按钮
            handle.Kjlb_browseorgspace_menu_product_new_addphoto_album_click()#选择相册添加
            handle.Kjlb_browseorgspace_menu_product_new_addphoto_album_list_click(self.photo)#选择第一张照片
            handle.Kjlb_browseorgspace_menu_product_new_addphoto_album_confirm_click()#点击完成
            sleep(4)
        #2.商品名称
            handle.Kjlb_browseorgspace_menu_product_new_proname_click()#点击商品名称
            handle.Kjlb_browseorgspace_menu_product_new_proname_name_sendkeys(self.proname)#输入商品名称
            handle.Kjlb_browseorgspace_menu_product_new_proname_name_title_click()#点击顶部标题
            handle.Kjlb_browseorgspace_menu_product_new_proname_bclassify_click()#点击分类
            handle.Kjlb_browseorgspace_menu_product_new_proname_bonetag_click(self.tag1)#1级标签
            handle.Kjlb_browseorgspace_menu_product_new_proname_btwotag_click(self.tag2)#2级标签
            handle.Kjlb_browseorgspace_menu_product_new_proname_confirm_click()#点击确定按钮
            handle.Kjlb_browseorgspace_menu_product_new_proname_choose_click()#点击勾选按钮
        #3.石种属性
            handle.Kjlb_browseorgspace_menu_product_new_attribute_click()#点击石种属性
            handle.Kjlb_browseorgspace_menu_product_new_attribute_species_sendkeys(self.species)#种类名
            handle.Kjlb_browseorgspace_menu_product_new_attribute_species_match_click(0)#点击匹配出的石种名
            handle.Kjlb_browseorgspace_menu_product_new_attribute_confirm_click()#点击勾选
        #4.制品和表面
            handle.Kjlb_browseorgspace_menu_product_new_attrstone_click()#点击制品和表面
            handle.Kjlb_browseorgspace_menu_product_new_attrstone_type_click()#点击制品
            handle.Kjlb_browseorgspace_menu_product_new_attrstone_type_list_click(self.type)#平板
            handle.Kjlb_browseorgspace_menu_product_new_attrstone_surface_click()#点击表面
            handle.Kjlb_browseorgspace_menu_product_new_attrstone_surface_list_click(self.surface)#光面
            handle.Kjlb_browseorgspace_menu_product_new_attrstone_confirm_click()#勾选
        #5.产品参数
            handle.Kjlb_browseorgspace_menu_product_new_parameter_click()#点击产品参数
            handle.Kjlb_browseorgspace_menu_product_new_parameter_key_clear(0)#先清空参数名
            handle.Kjlb_browseorgspace_menu_product_new_parameter_key_sendkeys(0,self.key)#输入参数名
            handle.Kjlb_browseorgspace_menu_product_new_parameter_value_sendkeys(0,self.value)#输入参数值
            handle.Kjlb_browseorgspace_menu_product_new_parameter_confirm_click()#点击勾选
        #6.价格
            handle.Kjlb_browseorgspace_menu_product_new_price_click()#点击价格
         #6.1 价格:0 库存:0
            handle.Kjlb_browseorgspace_menu_product_new_price_unitprice_sendkeys(-2,self.price1)#单价0元
            handle.Kjlb_browseorgspace_menu_product_new_price_stock_sendkeys(-1,self.stock1)#库存0
            handle.Kjlb_browseorgspace_menu_product_new_price_save().click()#点击保存
         #6.2 价格:123 库存:空
            handle.Kjlb_browseorgspace_menu_product_new_price_add_click()#+新价
            handle.Kjlb_browseorgspace_menu_product_new_price_unitprice_sendkeys(-2,self.price2)#单价123元
            handle.Kjlb_browseorgspace_menu_product_new_price_stock_sendkeys(-1,self.stock2)#库存空
            handle.Kjlb_browseorgspace_menu_product_new_price_save_click()#点击保存
         #6.3 价格:空 库存:123
            handle.Kjlb_browseorgspace_menu_product_new_price_add_click()#+新价
            handle.Kjlb_browseorgspace_menu_product_new_price_stock_sendkeys(-1,self.stock3)#库存123
            handle.Kjlb_browseorgspace_menu_product_new_price_unitprice_sendkeys(-2,self.price3)#单价空
            handle.Kjlb_browseorgspace_menu_product_new_price_save_click()#点击保存
         #6.4 价格:999 库存:999
            handle.Kjlb_browseorgspace_menu_product_new_price_add_click()#+新价
            handle.Kjlb_browseorgspace_menu_product_new_price_unitprice_sendkeys(-2,self.price4)#单价999元
            handle.Kjlb_browseorgspace_menu_product_new_price_stock_sendkeys(-1,self.stock4)#库存999
            handle.Kjlb_browseorgspace_menu_product_new_price_save_click()#点击保存
            handle.Kjlb_browseorgspace_menu_product_new_price_back_click()#点击返回
        #7.保存->发布
            handle.Kjlb_browseorgspace_menu_product_new_save_click()#点击保存
        except Exception as err:
            logging.error("Error Information CreateProduct Inside : %s"%err)
            raise err