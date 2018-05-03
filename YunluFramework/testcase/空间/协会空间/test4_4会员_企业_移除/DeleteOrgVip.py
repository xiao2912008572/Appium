__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from YunluFramework.testcase.空间.协会空间.test4_4会员_企业_移除 import *


# 移除企业会员
class DeleteOrgVip:
    #1.初始化
    def __init__(self):
        # 1.创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')
        # 2.获取截图路径、日志路径、日志名
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名
        # 3.创建日志模块
        self.log = Log(self.logfile)

    #2.会员_企业_移除-公用方法
    def deletOrgVip(self, driver, orgNo):
        '''移除企业会员'''
        # 创建_SPACEHANDLE5公有定位控件对象
        self.handleS = SPACEHANDLE5(driver)
        sleep(1)
        try:
            self.log.info('------START:test4_4会员_企业_移除.DeleteOrgVip.py------')
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
            # 5.企业名录
            self.handleS.Kjlb_browseascspace_menu_vip_companylist_click()
            self.log.info('点击企业名录')
            # 6.菜单栏
            self.handleS.Kjlb_browseascspace_menu_vip_menu_click()
            self.log.info('点击菜单栏')
            # 7.管理
            self.handleS.Kjlb_browseascspace_menu_vip_menu_manage_click()
            self.log.info('点击管理')
            # 8.编辑
            self.handleS.Kjlb_browseascspace_menu_vip_menu_manage_edit_click()
            self.log.info('点击编辑')
            # 9.勾选企业
            self.handleS.Kjlb_browseascspace_menu_vip_menu_manage_edit_choosecompany_click(orgNo)
            self.log.info('勾选第{0}家企业'.format(orgNo))
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
            try:
                self.handleS.Kjlb_search_back_click()
                self.log.info('点击搜索返回按钮，返回空间列表页面')  # 返回空间列表
            except Exception as e:
                self.log.info('未找到该控件，不执行返回空间列表页面操作')
            self.log.info('------END:test4_4会员_企业_移除.DeleteOrgVip.py------')
        except Exception as err:
            self.log.error("Error Information DeletePerVip Inside : %s" % err)
            raise err
