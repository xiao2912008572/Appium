__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from StoneUIFramework.testcase.订单.test1_1购买主流程 import *


# 订单购买主流程
@ddt.ddt
class order_OrderBuy(unittest.TestCase):
    # 1.全局测试数据
    d = DataInfo("order.xls")  # 创建DataInfo()对象
    pro_no_1 = random.randint(0, 3)
    spacename_1 = (d.cell("test001", 2, 1))  # 空间名
    title_address1 = d.cell('test001', 2, 3)  # 标题：添加收货地址
    addressee_1 = d.cell('test001', 2, 4)  # 收货人：肖静远
    contact_1 = int(d.cell('test001', 2, 5))  # 联系电话：13027104206
    province_1 = int(d.cell('test001', 2, 6))  # 省：北京 0
    city_1 = int(d.cell('test001', 2, 7))  # 市：东城 0
    detail_1 = d.cell('test001', 2, 9)  # 详细地址：ABCDEFGHIJKLMNOPQRSTUVWXYZ
    title_order1 = d.cell('test001', 2, 10)  # 标题：确认订单

    # 2.初始化
    @classmethod
    def setUpClass(self):
        # 1.建立连接信息
        cnn = Connect()
        self.driver = cnn.connect()
        # 2.创建工具类
        self.tools = Tools(self.driver)  # tools工具
        # 3.创建SPACEHANDLE6公有定位控件对象
        self.handle = SPACEHANDLE6(self.driver)
        # 4.创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')
        # 5.获取截图路径、日志路径、日志名
        self.screen_path = cf.getParam('order', "order_path_001_1")  # 通过配置文件获取截图的路径
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名
        # 6.创建日志记录模块
        self.log = Log(self.logfile)
        # 7.创建UploadPic和DeletePic对象

        sleep(1)
        # 8.打印日志
        self.log.info('****************************************用例开始！****************************************')
        self.log.info("----------------------------START:test1_1购买主流程.Buy001_1.py---------------------------")

    # 3.释放资源
    @classmethod
    def tearDownClass(self):
        # 1.打印日志
        self.log.info("-----------------------------END:test1_1购买主流程.Buy001_1.py----------------------------")
        self.log.info('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~用例结束！~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        # 2.关闭driver
        self.driver.quit()

    # 4.测试用例
    # 4.1找到商品
    @ddt.data([spacename_1, pro_no_1])
    @ddt.unpack
    def test_buy001(self, spacename, pro_no):
        '''进入空间：找到商品流程'''
        try:
            self.log.info("------------START:Function_Buy001-找到商品------------")
            # 1.空间列表
            self.handle.Kjlb_click()
            self.log.info('点击空间列表')
            # 2.选择进入测试机构空间
            self.handle.Kjlb_browseorgspaceByName_click(spacename)
            self.log.info('进入空间：{0}'.format(spacename))
            # 3.选择第一件商品
            global proname_start
            proname_start = self.handle.Kjlb_prolist_pronameT(pro_no)
            self.log.info('选择的商品名称为：{0}'.format(proname_start))
            self.handle.Kjlb_prolist_click(pro_no)
            self.log.info('点击第{0}件商品'.format(pro_no + 1))
            self.log.info("------------END:Function_Buy001-找到商品------------")
        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("Buy Outside : %s" % err)
            raise err

    @ddt.data([title_address1, addressee_1, contact_1, province_1, city_1, detail_1])
    @ddt.unpack
    def test_buy002(self, title, addressee, contact, province, city, detail):
        '''购买商品：填写地址流程'''
        try:
            self.log.info("------------START:Function_Buy002-购买商品填写地址------------")
            # 1.点击立即购买
            self.handle.Kjlb_browseorgspace_menu_product_lock_list_buynow_click()
            self.log.info('点击立即购买')
            # 2.检查是否跳转至添加收货地址页面
            self.log.info('检查是否跳转至添加收货地址页面')
            assert self.handle.Kjlb_browseorgspace_menu_product_lock_list_buynow_recaddress_page_element() != None, '页面跳转失败'
            self.log.info('跳转成功')
            # 3.页面标题检查
            title_now_address = self.handle.Kjlb_browseorgspace_menu_product_lock_list_buynow_recaddress_gettitle()
            self.log.info('当前页面标题：{0}'.format(title_now_address))
            self.log.info('预期页面标题：{0}'.format(title))
            assert title_now_address == title, '实际标题与预期标题不符'
            # 4.填写收货地址相关信息
            self.handle.Kjlb_browseorgspace_menu_product_lock_list_buynow_recaddress_addressee_sendkeys(addressee)
            self.log.info('收货人：{0}'.format(addressee))
            self.handle.Kjlb_browseorgspace_menu_product_lock_list_buynow_recaddress_cnumber_sendkeys(contact)
            self.log.info('联系电话：{0}'.format(contact))
            self.handle.Kjlb_browseorgspace_menu_product_lock_list_buynow_recaddress_district_click()
            self.log.info('点击所在地区')
            self.handle.Kjlb_browseorgspace_menu_product_lock_list_buynow_recaddress_districtlist_click(province)
            self.log.info('选择第{0}个省'.format(province + 1))
            self.handle.Kjlb_browseorgspace_menu_product_lock_list_buynow_recaddress_districtlist_click(city)
            self.log.info('选择第{0}个市'.format(city + 1))
            self.handle.Kjlb_browseorgspace_menu_product_lock_list_buynow_recaddress_detail_sendkeys(detail)
            self.log.info('填写详细地址：{0}'.format(detail))
            # 5.点击保存
            self.handle.Kjlb_browseorgspace_menu_product_lock_list_buynow_recaddress_save_click()
            self.log.info('点击保存')
            self.log.info("------------SEND:Function_Buy002-购买商品填写地址------------")
        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("Buy Outside : %s" % err)
            raise err

    @ddt.data([title_order1])
    @ddt.unpack
    def test_buy003(self, title):
        '''确认订单：支付流程'''
        self.log.info("------------START:Function_Buy003-确认订单支付流程------------")
        # 1.页面跳转检查
        self.log.info('检查是否跳转至确认订单页面')
        assert self.handle.Kjlb_browseorgspace_menu_product_lock_list_buynow_corder_pagee() != None, '页面跳转失败'
        self.log.info('跳转成功')
        # 2.页面标题检查
        title_now_order = self.handle.Kjlb_browseorgspace_menu_product_lock_list_buynow_corder_titlee()
        self.log.info('当前页面标题：{0}'.format(title_now_order))
        self.log.info('预期页面标题：{0}'.format(title))
        assert title_now_order == title, '实际标题与预期标题不符'
        # 3.点击支付
        self.handle.Kjlb_browseorgspace_menu_product_lock_list_buynow_corder_pay_click()
        self.log.info('点击支付')
        # 4.选择微信支付
        self.handle.Kjlb_browseorgspace_menu_product_lock_list_buynow_corder_pay_weixin_click()
        self.log.info('支付方式选择：微信支付')
        # 5.立即支付
        self.handle.Kjlb_browseorgspace_menu_product_lock_list_buynow_corder_pay_weixin_now_click()
        self.log.info('点击立即支付')
        # 6.输入密码
        self.handle.Kjlb_browseorgspace_menu_product_lock_list_buynow_corder_pay_weixin_now_password_sendkeys('199288')
        self.log.info('输入密码')
        self.log.info("------------END:Function_Buy003-确认订单支付流程------------")
        # 7.支付成功检查
        self.log.info('支付结果检查')
        assert self.handle.Kjlb_browseorgspace_menu_product_lock_list_buynow_corder_pay_weixin_success_text() == '支付成功', '支付失败！'
        self.log.info('支付成功！')
        # 8.点击完成
        self.handle.Kjlb_browseorgspace_menu_product_lock_list_buynow_corder_pay_weixin_finish_click()
        self.log.info('点击完成')

    def test_buy004(self):
        try:
            '''云庐收银台：查看订单，获取订单编号'''
            self.log.info("------------START:Function_Buy004-云庐收银台检查------------")
            # 1.检查页面是否跳转至云庐收银台
            self.log.info('检查是否跳转至云庐收银台')
            assert self.handle.Kjlb_browseorgspace_menu_product_lock_list_buynow_corder_pay_cashier_page() != None, '页面跳转失败'
            self.log.info('跳转成功')
            # 2.查看订单
            self.handle.Kjlb_browseorgspace_menu_product_lock_list_buynow_corder_pay_cashier_lorder_click()
            self.log.info('查看订单')
            # 3.跳转至待发货列表
            self.log.info('检查页面是否跳转至待发货栏')
            assert self.handle.Kjlb_browseorgspace_menu_order_waitforsend_element() != None, '跳转页面失败'
            self.log.info('跳转成功')
            # 4.点击商品，查看订单
            proname_now = self.handle.Kjlb_browseorgspace_menu_order_prolist_pronameT()
            self.log.info('当前商品名称为：{0}'.format(proname_now))
            self.log.info('预期商品名称为：{0}'.format(proname_start))
            assert proname_now == proname_start, '购买商品名称显示无误'

            self.handle.Kjlb_browseorgspace_menu_order_prolist_click(0)

            self.log.info('点击待发货列表第1件商品')
        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("Buy Outside : %s" % err)
            raise err


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(order_OrderBuy)
    unittest.TextTestRunner(verbosity=2).run(suite)
