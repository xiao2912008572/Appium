__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from YunluFramework.testcase.空间.common import *


# +个人会员
class AddPerVip:

    # 1.初始化
    def __init__(self):

        # 创建Login对象
        self.login = LoginA()

        # 1.创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')

        # 2.获取截图路径、日志路径、日志名
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名

        # 3.创建日志模块
        self.log = Log(self.logfile)

    # 2.协会加个人会员-公用方法
    def addPerVip(self, driver, vipname):
        '''+个人会员'''
        # 创建_OrgSpaceTeamHandle公有定位控件对象
        handle = SPACEHANDLE5(driver)
        sleep(1)
        try:
            self.log.info('------START:test5_1加会员_管理员_个人_拒绝.AddPerVip.py------')

            # 1.空间首页
            # handle.Kjlb_click()
            # tools.getScreenShot(screen_path,"空间首页")
            # 2.选择空间:测试空间123
            # handle.Kjlb_browseascspaceByName_click(self.spacename)

            # 3.点击+按钮
            handle.Kjlb_browseascspace_addbtn_click()  # 点击+按钮
            self.log.info('点击：+按钮')

            # 4.个人会员
            handle.Kjlb_browseascspace_addbtn_pVip_click()  # 点击个人会员
            self.log.info('点击：个人会员')

            # 5.搜索栏搜索姓名添加
            handle.Kjlb_browseascspace_menu_addvip_addperson_search_sendkeys(vipname)
            self.log.info('搜索栏搜索姓名：{0}'.format(vipname))
            handle.Kjlb_browseascspace_menu_addvip_addperson_searchbtn_click()
            self.log.info('点击搜索')

            # 6.选择搜索结果，添加
            handle.Kjlb_browseascspace_menu_addvip_addperson_choose_click(0)
            self.log.info('选择搜索结果：第1个')
            handle.Kjlb_browseascspace_menu_addvip_addperson_confirm_click()
            self.log.info('点击添加')

            # 7.返回到空间主界面
            handle.Kjlb_browseascspace_back_click()
            self.log.info('点击返回，返回至空间主界面')

            # 8.返回空间列表
            try:
                handle.Kjlb_search_back_click()
                self.log.info('点击搜索返回按钮，返回空间列表页面')  # 返回空间列表
            except Exception as e:
                self.log.info('未找到该控件，不执行返回空间列表页面操作')

            self.log.info('------END:test5_1加会员_管理员_个人_拒绝.AddPerVip.py------')

        except Exception as err:
            self.log.error("AddPerVip Inside : %s" % err)
            raise err
