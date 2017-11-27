__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from YunluFramework.testcase.空间.机构空间.test1_1创建机构空间 import *


# 关闭机构空间
class CloseSpace:
    # 1.初始化
    def __init__(self):
        # 1.创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')
        # 2.获取截图路径、日志路径、日志名
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名
        # 3.创建日志模块
        self.log = Log(self.logfile)
        sleep(1)

    # 2.关闭空间-公用方法
    def closeSpace(self, driver, spacename):
        # 1.创建工具类
        t = Tools(driver)
        try:
            self.log.info("------START:test1_1创建机构空间.CloseSpace.py-----")
            # 1.创建_SPACEHANDLE5公有定位控件对象
            self.handle = SPACEHANDLE5(driver)
            # -----------------关闭空间 - ----------------
            # 为了保证不中途退出，需要第一次进入的时候检查是否存在该机构，如果存在，先关闭
            t.swipeUp(500)
            t.swipeUp(500)
            t.swipeUp(500)
            self.log.info('屏幕向上滑动1.5秒')
            self.handle.Kjlb_browseorgspaceByName_click(spacename)
            self.log.info('点击进入空间:{0}'.format(spacename))
            sleep(1)
            self.handle.Kjlb_browseorgspace_menu_click()  # 菜单栏
            self.log.info('点击空间菜单栏')
            self.handle.Kjlb_browseorgspace_menu_close_click()  # 关闭
            self.log.info('点击关闭按钮')
            self.handle.Kjlb_browseorgspace_menu_close_confirm_click()  # 确认关闭
            self.log.info('点击确认关闭')
            self.log.info("------END:test1_1创建机构空间.CloseSpace.pyy-----")
        except Exception as err:
            self.log.error("CloseSpace Inside : %s" % err)
            raise err
