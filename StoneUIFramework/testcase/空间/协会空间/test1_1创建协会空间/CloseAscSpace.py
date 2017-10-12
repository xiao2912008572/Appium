__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from time import sleep
from StoneUIFramework.config.globalparam import GlobalParam
from StoneUIFramework.public.handle.space.SPACEHANDLE5 import _SPACEHANDLE5
from StoneUIFramework.public.common.log import Log


# 关闭机构空间
class CloseAscSpace:
    # 1.初始化
    def __init__(self):
        # 1.创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')
        # 2.获取截图路径、日志路径、日志名
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名
        # 3.创建日志模块
        self.log = Log(self.logfile)
        sleep(1)

    # 2.关闭协会空间-公用方法
    def closeAsscSpace(self, driver, name):
        # 创建_SPACEHANDLE5公有定位控件对象
        handle = _SPACEHANDLE5(driver)

        try:
            self.log.info('------START:test1_1创建协会空间.CloseAscSpace.py------')
            # 为了保证不中途退出，需要第一次进入的时候检查是否存在该机构，如果存在，先关闭
            # 1.进入协会空间
            handle.Kjlb_browseorgspaceByName_click(name)
            self.log.info('进入协会空间：{0}'.format(name))
            sleep(1)
            # 2.点击菜单栏
            handle.Kjlb_browseascspace_menu_click()
            self.log.info('点击菜单栏')
            # 3.点击关闭
            handle.Kjlb_browseascspace_menu_close_click()
            self.log.info('点击关闭')
            # 4.关闭确认
            handle.Kjlb_browseascspace_menu_close_yes_click()
            self.log.info('确认关闭')
            self.log.info('------END:test1_1创建协会空间.CloseAscSpace.py------')
        except Exception as err:
            self.log.error("CloseAscSpace Inside : %s" % err)
            raise err
