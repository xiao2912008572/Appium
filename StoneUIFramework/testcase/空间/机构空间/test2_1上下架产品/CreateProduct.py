__author__ = 'Administrator'
#coding=utf-8
from time import sleep
import logging

from StoneUIFramework.config.globalparam import GlobalParam
from StoneUIFramework.public.common.datainfo import DataInfo
from StoneUIFramework.public.handle.space.SPACEHANDLE5 import _SPACEHANDLE5
from StoneUIFramework.public.common.log import Log

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
        #创建读取配置信息对象
        cf = GlobalParam('config','path_file.conf')
        #获取截图路径、日志路径、日志名
        self.logfile = cf.getParam('log',"logfile")#日志文件名
        #创建日志模块
        self.log = Log(self.logfile)
    def createProduct(self,driver):
        """
            菜单栏用坐标定位：68行，实属无奈之举
        """
        try:
            self.log.info('------START:test2_1上下架产品.CreateProduct.py------')
            #创建_SPACEHANDLE5公有定位控件对象
            handle = _SPACEHANDLE5(driver)
            sleep(1)
            #-----------------新建产品-----------------
            handle.Kjlb_browseorgspace_menu_product_new_click()#点击新建按钮
            self.log.info('点击新建按钮')
        #1.添加照片
            handle.Kjlb_browseorgspace_menu_product_new_addphoto_click()#点击添加照片按钮
            self.log.info('点击添加照片按钮')
            handle.Kjlb_browseorgspace_menu_product_new_addphoto_album_click()#选择相册添加
            self.log.info('选择相册添加')
            handle.Kjlb_browseorgspace_menu_product_new_addphoto_album_list_click(self.photo)#选择第一张照片
            self.log.info('选择第%s张照片'%self.photo)
            handle.Kjlb_browseorgspace_menu_product_new_addphoto_album_confirm_click()#点击完成
            self.log.info('点击完成')
            sleep(4)
        #2.商品名称
            handle.Kjlb_browseorgspace_menu_product_new_proname_click()#点击商品名称
            self.log.info('点击商品名称')
            handle.Kjlb_browseorgspace_menu_product_new_proname_name_sendkeys(self.proname)#输入商品名称
            self.log.info('输入商品名称：%s'%self.proname)
            handle.Kjlb_browseorgspace_menu_product_new_proname_name_title_click()#点击顶部标题
            self.log.info('点击顶部标题')
            handle.Kjlb_browseorgspace_menu_product_new_proname_bclassify_click()#点击分类
            self.log.info('点击商品分类')
            handle.Kjlb_browseorgspace_menu_product_new_proname_bonetag_click(self.tag1)#1级标签
            self.log.info('选择%s级标签'%self.tag1)
            handle.Kjlb_browseorgspace_menu_product_new_proname_btwotag_click(self.tag2)#2级标签
            self.log.info('选择%s级标签'%self.tag2)
            handle.Kjlb_browseorgspace_menu_product_new_proname_confirm_click()#点击确定按钮
            self.log.info('确定按钮')
            handle.Kjlb_browseorgspace_menu_product_new_proname_choose_click()#点击勾选按钮
            self.log.info('点击勾选按钮')
        #3.石种属性
            handle.Kjlb_browseorgspace_menu_product_new_attribute_click()#点击石种属性
            self.log.info('点击石种属性')
            handle.Kjlb_browseorgspace_menu_product_new_attribute_species_sendkeys(self.species)#种类名
            self.log.info('选择种类名：%s'%self.species)
            handle.Kjlb_browseorgspace_menu_product_new_attribute_species_match_click(0)#点击匹配出的石种名
            self.log.info('点击匹配出的石种名')
            handle.Kjlb_browseorgspace_menu_product_new_attribute_confirm_click()#点击勾选
            self.log.info('点击勾选按钮')
        #4.制品和表面
            handle.Kjlb_browseorgspace_menu_product_new_attrstone_click()#点击制品和表面
            self.log.info('点击制品与表面')
            handle.Kjlb_browseorgspace_menu_product_new_attrstone_type_click()#点击制品
            self.log.info('点击制品')
            handle.Kjlb_browseorgspace_menu_product_new_attrstone_type_list_click(self.type)#平板
            self.log.info('选择%s'%self.type)
            handle.Kjlb_browseorgspace_menu_product_new_attrstone_surface_click()#点击表面
            self.log.info('点击表面')
            handle.Kjlb_browseorgspace_menu_product_new_attrstone_surface_list_click(self.surface)#光面
            self.log.info('选择%s'%self.surface)
            handle.Kjlb_browseorgspace_menu_product_new_attrstone_confirm_click()#勾选
            self.log.info('点击勾选按钮')
        #5.产品参数
            handle.Kjlb_browseorgspace_menu_product_new_parameter_click()#点击产品参数
            self.log.info('点击产品参数')
            handle.Kjlb_browseorgspace_menu_product_new_parameter_key_clear(0)#先清空参数名
            self.log.info('清空参数名')
            handle.Kjlb_browseorgspace_menu_product_new_parameter_key_sendkeys(0,self.key)#输入参数名
            self.log.info('输入参数名：%s'%self.key)
            handle.Kjlb_browseorgspace_menu_product_new_parameter_value_sendkeys(0,self.value)#输入参数值
            self.log.info('输入参数值：%s'%self.value)
            handle.Kjlb_browseorgspace_menu_product_new_parameter_confirm_click()#点击勾选
            self.log.info('点击勾选')
        #6.价格
            handle.Kjlb_browseorgspace_menu_product_new_price_click()#点击价格
            self.log.info('点击价格')
         #6.1 价格:0 库存:0
            handle.Kjlb_browseorgspace_menu_product_new_price_unitprice_sendkeys(-2,self.price1)#单价0元
            self.log.info('单价：%s'%self.price1)
            handle.Kjlb_browseorgspace_menu_product_new_price_stock_sendkeys(-1,self.stock1)#库存0
            self.log.info('库存：%s'%self.stock1)
            handle.Kjlb_browseorgspace_menu_product_new_price_save_click()  # 点击保存
            self.log.info('点击保存')
         #6.2 价格:123 库存:空
            handle.Kjlb_browseorgspace_menu_product_new_price_add_click()#+新价
            self.log.info('点击+新价')
            handle.Kjlb_browseorgspace_menu_product_new_price_unitprice_sendkeys(-2,self.price2)#单价123元
            self.log.info('单价：%s'%self.price2)
            handle.Kjlb_browseorgspace_menu_product_new_price_stock_sendkeys(-1,self.stock2)#库存空
            self.log.info('库存：%s'%self.stock2)
            handle.Kjlb_browseorgspace_menu_product_new_price_save_click()#点击保存
            self.log.info('点击保存')
         #6.3 价格:空 库存:123
            handle.Kjlb_browseorgspace_menu_product_new_price_add_click()#+新价
            self.log.info('点击+新价')
            handle.Kjlb_browseorgspace_menu_product_new_price_stock_sendkeys(-1,self.stock3)#库存123
            self.log.info('库存：%s'%self.stock3)
            handle.Kjlb_browseorgspace_menu_product_new_price_unitprice_sendkeys(-2,self.price3)#单价空
            self.log.info('单价：%s'%self.price1)
            handle.Kjlb_browseorgspace_menu_product_new_price_save_click()#点击保存
            self.log.info('点击保存')
         #6.4 价格:999 库存:999
            handle.Kjlb_browseorgspace_menu_product_new_price_add_click()#+新价
            self.log.info('点击+新价')
            handle.Kjlb_browseorgspace_menu_product_new_price_unitprice_sendkeys(-2,self.price4)#单价999元
            self.log.info('单价：%s'%self.price4)
            handle.Kjlb_browseorgspace_menu_product_new_price_stock_sendkeys(-1,self.stock4)#库存999
            self.log.info('库存：%s'%self.stock4)
            handle.Kjlb_browseorgspace_menu_product_new_price_save_click()#点击保存
            self.log.info('点击保存')
            handle.Kjlb_browseorgspace_menu_product_new_price_back_click()#点击返回
            self.log.info('点击返回')
        #7.保存->发布
            handle.Kjlb_browseorgspace_menu_product_new_save_click()#点击保存
            self.log.info('点击保存')
            self.log.info('------END:test2_1上下架产品.CreateProduct.py------')
        except Exception as err:
            self.log.error("CreateProduct Inside : %s"%err)
            raise err