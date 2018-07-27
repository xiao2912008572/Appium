__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from StoneUIFramework.testcase.空间.协会空间.test5_8加会员_个人_企业_同意 import *


# +企业会员
class AddOrgVip:
    # 1.初始化
    def __init__(self):
        # 创建Loginout和Login对象
        self.login = LoginA()
        # 1.创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')
        # 2.获取截图路径、日志路径、日志名
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名
        # 3.创建日志模块
        self.log = Log(self.logfile)

    # 2.协会加企业会员-公用方法
    def addOrgVip(self, driver, orgname):
        '''+企业会员'''
        # 创建_OrgSpaceTeamHandle公有定位控件对象
        handle = SPACEHANDLE5(driver)
        sleep(1)
        try:
            self.log.info('------START:test5_8加会员_个人_企业_同意.AddOrgVip.py------')
            # 1.空间首页
            # handle.Kjlb_click()
            # tools.getScreenShot(screen_path,"空间首页")
            # 2.选择空间:测试空间123
            # handle.Kjlb_browseascspaceByName_click(self.spacename)
            # 3.右上角:菜单栏选择+会员
            handle.Kjlb_browseascspace_menu_click()  # 右上角菜单
            self.log.info('点击右上角菜单')
            handle.Kjlb_browseascspace_menu_addvip_click()  # 点击+会员
            self.log.info('点击：+会员')
            # 4.企业会员
            handle.Kjlb_browseascspace_menu_addvip_addcompany_click()
            self.log.info('点击企业会员')
            # 5.搜索栏搜索姓名添加
            handle.Kjlb_browseascspace_menu_addvip_addcompany_search_click()  # 点击搜索栏
            self.log.info('点击搜索栏')
            handle.Kjlb_browseascspace_menu_addvip_addcompany_search_search_sendkeys(orgname)  # 搜索企业名称
            self.log.info('搜索栏搜索企业：{0}'.format(orgname))
            handle.Kjlb_browseascspace_menu_addvip_addcompany_searchbtn_click()  # 点击搜索
            self.log.info('点击搜索')
            # 6.选择搜索结果，添加
            handle.Kjlb_browseascspace_menu_addvip_addcompany_choose_click(0)
            self.log.info('点击搜索')
            handle.Kjlb_browseascspace_menu_addvip_addcompany_confirm_click()
            self.log.info('点击添加')
            # 7.返回到空间主界面
            handle.Kjlb_browseascspace_back_click()
            self.log.info('点击返回，返回至空间主界面')
            self.log.info('------END:test5_8加会员_个人_企业_同意.AddOrgVip.py------')
        except Exception as err:
            self.log.error("AddOrgVip Inside : %s" % err)
            raise err
