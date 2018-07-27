__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from YunluFramework.testcase.空间.私人空间.test2_1私人空间加文件夹 import *


# 创建机构空间
class CreatePersonSpace:
    # 1.初始化
    def __init__(self):
        # 1.创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')
        # 2.获取截图路径、日志路径、日志名
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名
        # 3.创建日志模块
        self.log = Log(self.logfile)

    # 2.创建私人空间-公用方法
    def createPersonSpace(self, driver, spacename, foldername1=None, foldername2=None, foldername3=None):  # 最多三个文件夹
        # 创建_SPACEHANDLE5公有定位控件对象
        handle = SPACEHANDLE5(driver)
        sleep(2)
        try:
            self.log.info("------START:test2_1私人空间加文件夹CreatePersonSpace.py------")
            # #1.空间首页
            #     handle.Kjlb_click()
            # 2.右上角主菜单
            handle.Kjlb_mainmenu_click()
            self.log.info('点击右上角主菜单')
            # 3.+私人空间
            handle.Kjlb_mainmenu_newpersonspace_click()
            self.log.info('点击+私人空间')
            # 4.输入空间名称、文件夹名-保存
            handle.Kjlb_mainmenu_newpersonspace_choosespacetype_click(0)  # 选择衣服类型空间
            self.log.info('选择衣服类型空间')
            handle.Kjlb_mainmenu_newpersonspace_spacename_sendkeys(spacename)  # appium私人空间
            self.log.info('空间名为{0}'.format(spacename))
            # handle.Kjlb_mainmenu_newpersonspace_foldername_sendkeys(foldername1)#appium文件夹
            handle.Kjlb_mainmenu_newpersonspace_save_click()  # 保存
            self.log.info('点击保存')
            # 6.返回到空间列表
            handle.Kjlb_mainmenu_newpersonspace_mainback_click()
            self.log.info('返回到空间列表')
            self.log.info('------END:test2_1私人空间加文件夹.CreatePersonSpace.py------')
        except Exception as err:
            self.log.error("CreatePersonSpace Inside : %s" % err)
            raise err
