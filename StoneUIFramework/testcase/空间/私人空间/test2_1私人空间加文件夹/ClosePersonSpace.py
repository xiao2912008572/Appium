__author__ = 'Administrator'
# -*- coding: utf-8 -*-

from time import sleep
from StoneUIFramework.public.handle.space.SPACEHANDLE5 import _SPACEHANDLE5
from StoneUIFramework.public.common.log import Log
from StoneUIFramework.config.globalparam import GlobalParam


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
        # 创建_SPACEHANDLE5公有定位控件对象
        handle = _SPACEHANDLE5(driver)
        sleep(1)
        try:
            self.log.info("------START:test2_1私人空间加文件夹ClosePersonSpace.py------")
            # 1.点击该空间
            handle.Kjlb_browseorgspaceByName_click(spacename)
            self.log.info('点击{0}空间'.format(spacename))
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
