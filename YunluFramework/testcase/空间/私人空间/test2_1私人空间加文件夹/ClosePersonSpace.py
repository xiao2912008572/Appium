__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from YunluFramework.testcase.空间.私人空间.test2_1私人空间加文件夹 import *


# 关闭私人空间
class ClosePersonSpace:
    # 1.初始化
    def __init__(self):
        # 1.创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')
        # 2.获取截图路径、日志路径、日志名
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名
        # 3.创建日志模块
        self.log = Log(self.logfile)

    # 2.关闭私人空间-公用方法
    def closePersonSpace(self, driver, spacename):
        # 1.创建_SPACEHANDLE5公有定位控件对象
        handle = SPACEHANDLE5(driver)
        sleep(1)
        # 2.创建工具类
        self.tools = Tools(driver)  # tools工具
        try:
            self.log.info("------START:test2_1私人空间加文件夹ClosePersonSpace.py------")
            """
            # 1.点击该空间
            self.tools.find_space_by_name(spacename)
            self.log.info('搜索栏搜索结果:{0}'.format(spacename))
            handle.Kjlb_browseorgspaceByID_click(0)
            handle.Kjlb_browseorgspaceByName_click(spacename)
            self.log.info('点击{0}空间'.format(spacename))
            """
            # 2.菜单栏
            handle.Kjlb_browseperspace_menu_click()
            self.log.info('点击菜单栏')
            # 3.编辑
            handle.Kjlb_browseperspace_menu_edit_click()
            self.log.info('点击编辑')
            # 4.删除空间
            handle.Kjlb_browseperspace_menu_edit_deletespace_click()
            self.log.info('删除空间')
            handle.Kjlb_browseperspace_menu_edit_deletespace_OK_click()
            self.log.info('点击确定删除')
            self.log.info("------END:test2_1私人空间加文件夹ClosePersonSpace.py------")
        except Exception as err:
            self.log.error("Error Information CloseSpace Inside : %s" % err)
            raise err
