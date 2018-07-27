__author__ = 'Administrator'
# coding=utf-8
from StoneUIFramework.testcase.空间.机构空间.test2_1上下架产品 import *


# 上架产品
class DeleteProduct:
    # 1.初始化
    def __init__(self):  # 初始化测试数据
        # 1.创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')
        # 2.获取截图路径、日志路径、日志名
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名
        # 3.创建日志模块
        self.log = Log(self.logfile)

    # 2. 下架产品-公用方法
    def deleteProduct(self, driver):
        try:
            self.log.info('------START:test2_1上下架产品.DeleteProduct.py------')
            # 创建_SPACEHANDLE5公有定位控件对象
            self.handle = SPACEHANDLE5(driver)
            sleep(1)
            # -----------------删除产品-----------------
            # 1.点击菜单栏
            self.handle.Kjlb_browseorgspace_menu_product_unlock_list_menu_click()  # 点击菜单栏
            self.log.info('点击菜单栏')
            # 2.点击删除
            self.handle.Kjlb_browseorgspace_menu_product_unlock_list_menu_delete_click()  # 删除产品
            self.log.info('点击删除')
            self.log.info('------End:test2_1上下架产品.DeleteProduct.py------')
        except Exception as err:
            self.log.error("DeleteProduct Inside : %s" % err)
            raise err
