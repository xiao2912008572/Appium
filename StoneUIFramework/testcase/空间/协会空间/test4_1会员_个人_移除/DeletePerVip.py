__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from time import sleep
from StoneUIFramework.public.handle.space.SPACEHANDLE5 import _SPACEHANDLE5
from StoneUIFramework.public.common.datainfo import DataInfo
from StoneUIFramework.public.common.log import Log
from StoneUIFramework.config.globalparam import GlobalParam


# 移除个人会员
class DeletePerVip:
    # 1.初始化
    def __init__(self):
        d = DataInfo("space.xls")  # 创建DataInfo()对象
        self.vipname = d.cell("test007-会员", 2, 2)  # 人脉姓名
        # 1.创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')
        # 2.获取截图路径、日志路径、日志名
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名
        # 3.创建日志模块
        self.log = Log(self.logfile)

    # 2.会员_个人_移除-公用方法
    def deletePerVip(self, driver):
        '''移除个人会员'''
        # 创建_SPACEHANDLE5公有定位控件对象
        self.handleS = _SPACEHANDLE5(driver)
        sleep(1)
        try:
            self.log.info('------START:test4_1会员_个人_移除.DeletePerVip.py------')
            # #1.进入空间
            #     self.handleS.Kjlb_click()
            # #2.选择协会
            #     self.handleS.Kjlb_browseorgspaceByName_click(spacename)
            # 3.菜单栏
            self.handleS.Kjlb_browseascspace_menu_click()
            self.log.info('点击菜单栏')
            # 4.会员
            self.handleS.Kjlb_browseascspace_menu_vip_click()
            self.log.info('点击会员')
            # 5.个人名录
            self.handleS.Kjlb_browseascspace_menu_vip_personlist_click()
            self.log.info('点击个人名录')
            # 6.菜单栏
            self.handleS.Kjlb_browseascspace_menu_vip_menu_click()
            self.log.info('点击菜单栏')
            # 7.管理
            self.handleS.Kjlb_browseascspace_menu_vip_menu_manage_click()
            self.log.info('点击管理')
            # 8.编辑
            self.handleS.Kjlb_browseascspace_menu_vip_menu_manage_edit_click()
            self.log.info('点击编辑')
            # 9.勾选个人
            self.handleS.Kjlb_browseascspace_menu_vip_menu_manage_edit_chooseperson_click(0)
            self.log.info('勾选第1个人')
            # 10.移除
            self.handleS.Kjlb_browseascspace_menu_vip_menu_manage_edit_delete_click()
            self.log.info('点击移除')
            # 11.返回空间主界面
            self.handleS.Kjlb_browseascspace_menu_vip_menu_manage_edit_cancel_click()  # 取消->编辑页
            self.log.info('点击取消，返回至编辑页')
            self.handleS.Kjlb_browseascspace_menu_vip_menu_manage_back_click()  # 编辑界面返回->管理页
            self.log.info('点击编辑界面返回，返回至管理页')
            self.handleS.Kjlb_browseascspace_menu_vip_back_click()  # 管理界面返回->名片页
            self.log.info('点击管理界面返回，返回至名片页')
            self.handleS.Kjlb_browseascspace_back_click()  # 返回到空间列表
            self.log.info('返回到空间列表')
            self.log.info('------END:test4_1会员_个人_移除.DeletePerVip.py------')
        except Exception as err:
            self.log.error("DeletePerVip Inside : %s" % err)
            raise err
