__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from YunluFramework.testcase.登录.test2_1退出登录 import *


# 登出
class LoginoutA:
    # 1.初始化
    def __init__(self):
        # 创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')
        # 获取截图路径、日志路径、日志名
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名
        # 创建日志模块
        self.log = Log(self.logfile)

    # 2.登出-公用方法
    def loginout(self, driver, settingN):
        # 创建工具类
        tools = Tools(driver)  # tools工具
        # 创建_OrgSpaceTeamHandle公有定位控件对象
        handle = SETTINGHANDLE4(driver)
        sleep(1)
        try:
            # 1.点击设置按钮
            handle.Setting_click1(settingN)
            self.log.info('点击设置按钮')
            # 2.点击关于我们
            handle.Setting_aboutus_click()
            self.log.info('点击关于我们')
            # 3.点击退出
            handle.Setting_about_loginout_click()
            self.log.info('点击退出')
            # 4.点击确定
            handle.Setting_aboutus_loginout_confirm_click()
            self.log.info('点击确定')
        except Exception as err:
            self.log.error("LoginoutA Inside : %s" % err)
            raise err
