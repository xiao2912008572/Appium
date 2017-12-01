__author__ = 'Administrator'
# coding=utf-8
from YunluFramework.testcase.空间.机构空间.test2_1上下架产品 import *


# 上架产品
class CreateProduct:
    # 1.初始化
    def __init__(self):  # 初始化测试数据
        # 1.创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')
        # 2.获取截图路径、日志路径、日志名
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名
        # 3.创建日志模块
        self.log = Log(self.logfile)

    # 2.创建产品-公用方法
    def createProduct(self, driver, photo, proname,
                      tag1, tag2, species, type,
                      surface, key, value, price1,
                      stock1, price2, stock2, price3,
                      stock3, price4, stock4):
        """
            菜单栏用坐标定位：68行，实属无奈之举
        """
        try:
            t = Tools(driver)
            self.log.info('------START:test2_1上下架产品.CreateProduct.py------')
            # 创建_SPACEHANDLE5公有定位控件对象
            handle = SPACEHANDLE5(driver)
            sleep(1)
            # -----------------新建产品-----------------
            handle.Kjlb_browseorgspace_menu_product_new_click()  # 点击新建按钮
            self.log.info('点击新建按钮')
            # 1.添加照片
            handle.Kjlb_browseorgspace_menu_product_new_addphoto_click()  # 点击添加照片按钮
            self.log.info('点击添加照片按钮')
            handle.Kjlb_browseorgspace_menu_product_new_addphoto_album_click()  # 选择相册添加
            self.log.info('选择相册添加')
            handle.Kjlb_browseorgspace_menu_product_new_addphoto_album_list_click(photo)  # 选择第一张照片
            self.log.info('选择第%s张照片' % photo)
            handle.Kjlb_browseorgspace_menu_product_new_addphoto_album_confirm_click()  # 点击完成
            self.log.info('点击完成')
            sleep(4)
            # 2.商品名称
            handle.Kjlb_browseorgspace_menu_product_new_proname_click()  # 点击商品名称
            self.log.info('点击商品名称')
            handle.Kjlb_browseorgspace_menu_product_new_proname_name_sendkeys(proname)  # 输入商品名称
            self.log.info('输入商品名称：%s' % proname)
            handle.Kjlb_browseorgspace_menu_product_new_proname_name_title_click()  # 点击顶部标题
            self.log.info('点击顶部标题')

            driver.find_element_by_id("com.yunlu6.yunlu:id/et_classify").send_keys(u"建筑石材")
            self.log.info('商品分类输入：建筑石材')
            sleep(1)
            t.click_element_by_coordinate(528,566)
            self.log.info('点击搜索结果中的建筑石材')
            sleep(1)

            # handle.Kjlb_browseorgspace_menu_product_new_proname_bclassify_click()  # 点击分类
            # self.log.info('点击商品分类')
            # handle.Kjlb_browseorgspace_menu_product_new_proname_bonetag_click(tag1)  # 1级标签
            # self.log.info('选择%s级标签' % tag1)
            # handle.Kjlb_browseorgspace_menu_product_new_proname_btwotag_click(tag2)  # 2级标签
            # self.log.info('选择%s级标签' % tag2)
            # handle.Kjlb_browseorgspace_menu_product_new_proname_confirm_click()  # 点击确定按钮
            # self.log.info('确定按钮')
            handle.Kjlb_browseorgspace_menu_product_new_proname_choose_click()  # 点击勾选按钮
            self.log.info('点击勾选按钮')
            # # 3.石种属性
            # handle.Kjlb_browseorgspace_menu_product_new_attribute_click()  # 点击石种属性
            # self.log.info('点击石种属性')
            # handle.Kjlb_browseorgspace_menu_product_new_attribute_species_sendkeys(species)  # 种类名
            # self.log.info('选择种类名：%s' % species)
            # handle.Kjlb_browseorgspace_menu_product_new_attribute_species_match_click(0)  # 点击匹配出的石种名
            # self.log.info('点击匹配出的石种名')
            # handle.Kjlb_browseorgspace_menu_product_new_attribute_confirm_click()  # 点击勾选
            # self.log.info('点击勾选按钮')
            # # 4.制品和表面
            # handle.Kjlb_browseorgspace_menu_product_new_attrstone_click()  # 点击制品和表面
            # self.log.info('点击制品与表面')
            # handle.Kjlb_browseorgspace_menu_product_new_attrstone_type_click()  # 点击制品
            # self.log.info('点击制品')
            # handle.Kjlb_browseorgspace_menu_product_new_attrstone_type_list_click(type)  # 平板
            # self.log.info('选择%s' % type)
            # handle.Kjlb_browseorgspace_menu_product_new_attrstone_surface_click()  # 点击表面
            # self.log.info('点击表面')
            # handle.Kjlb_browseorgspace_menu_product_new_attrstone_surface_list_click(surface)  # 光面
            # self.log.info('选择%s' % surface)
            # handle.Kjlb_browseorgspace_menu_product_new_attrstone_confirm_click()  # 勾选
            # self.log.info('点击勾选按钮')
            # 5.产品参数
            handle.Kjlb_browseorgspace_menu_product_new_parameter_click()  # 点击产品参数
            self.log.info('点击产品参数')
            handle.Kjlb_browseorgspace_menu_product_new_parameter_key_clear(0)  # 先清空参数名
            self.log.info('清空参数名')
            handle.Kjlb_browseorgspace_menu_product_new_parameter_key_sendkeys(0, key)  # 输入参数名
            self.log.info('输入参数名：%s' % key)
            handle.Kjlb_browseorgspace_menu_product_new_parameter_value_sendkeys(0, value)  # 输入参数值
            self.log.info('输入参数值：%s' % value)
            handle.Kjlb_browseorgspace_menu_product_new_parameter_confirm_click()  # 点击勾选
            self.log.info('点击勾选')
            # 6.价格
            handle.Kjlb_browseorgspace_menu_product_new_price_click()  # 点击价格
            self.log.info('点击价格')
            # 6.1 价格:0 库存:0
            handle.Kjlb_browseorgspace_menu_product_new_price_unitprice_sendkeys(-2, price1)  # 单价0元
            self.log.info('单价：%s' % price1)
            handle.Kjlb_browseorgspace_menu_product_new_price_stock_sendkeys(-1, stock1)  # 库存0
            self.log.info('库存：%s' % stock1)
            t.swipeUp(500)
            self.log.info('向上滑动屏幕0.5秒')
            handle.Kjlb_browseorgspace_menu_product_new_price_save_click()  # 点击保存
            self.log.info('点击保存')
            # 6.2 价格:123 库存:空
            handle.Kjlb_browseorgspace_menu_product_new_price_add_click()  # +新价
            self.log.info('点击+新价')
            handle.Kjlb_browseorgspace_menu_product_new_price_unitprice_sendkeys(-2, price2)  # 单价123元
            self.log.info('单价：%s' % price2)
            handle.Kjlb_browseorgspace_menu_product_new_price_stock_sendkeys(-1, stock2)  # 库存空
            self.log.info('库存：%s' % stock2)
            t.swipeUp(500)
            self.log.info('向上滑动屏幕0.5秒')
            handle.Kjlb_browseorgspace_menu_product_new_price_save_click()  # 点击保存
            self.log.info('点击保存')
            # 6.3 价格:空 库存:123
            handle.Kjlb_browseorgspace_menu_product_new_price_add_click()  # +新价
            self.log.info('点击+新价')
            handle.Kjlb_browseorgspace_menu_product_new_price_stock_sendkeys(-1, stock3)  # 库存123
            self.log.info('库存：%s' % stock3)
            handle.Kjlb_browseorgspace_menu_product_new_price_unitprice_sendkeys(-2, price3)  # 单价空
            self.log.info('单价：%s' % price1)
            t.swipeUp(500)
            self.log.info('向上滑动屏幕0.5秒')
            handle.Kjlb_browseorgspace_menu_product_new_price_save_click()  # 点击保存
            self.log.info('点击保存')
            # 6.4 价格:999 库存:999
            handle.Kjlb_browseorgspace_menu_product_new_price_add_click()  # +新价
            self.log.info('点击+新价')
            handle.Kjlb_browseorgspace_menu_product_new_price_unitprice_sendkeys(-2, price4)  # 单价999元
            self.log.info('单价：%s' % price4)
            handle.Kjlb_browseorgspace_menu_product_new_price_stock_sendkeys(-1, stock4)  # 库存999
            self.log.info('库存：%s' % stock4)
            t.swipeUp(500)
            self.log.info('向上滑动屏幕0.5秒')
            handle.Kjlb_browseorgspace_menu_product_new_price_save_click()  # 点击保存
            self.log.info('点击保存')
            handle.Kjlb_browseorgspace_menu_product_new_price_back_click()  # 点击返回
            self.log.info('点击返回')
            # 7.保存->发布
            handle.Kjlb_browseorgspace_menu_product_new_save_click()  # 点击保存
            self.log.info('点击保存')
            self.log.info('------END:test2_1上下架产品.CreateProduct.py------')
        except Exception as err:
            self.log.error("CreateProduct Inside : %s" % err)
            raise err
