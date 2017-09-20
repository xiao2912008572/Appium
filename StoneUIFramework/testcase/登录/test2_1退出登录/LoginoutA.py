__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from time import sleep
import logging
from StoneUIFramework.public.common.publicfunction import Tools
from StoneUIFramework.public.handle.setting.SETTINGHANDLE4 import _SETTINGHANDLE4


# 团队人事任免
class LoginoutA:
    def __init__(self):
       pass

    def loginout(self, driver,settingN):
        #创建工具类
        tools = Tools(driver)  #tools工具
        #创建_OrgSpaceTeamHandle公有定位控件对象
        handle = _SETTINGHANDLE4(driver)
        sleep(1)
        try:
        #1.点击设置按钮
            handle.Setting_click1(settingN)
        #2.点击系统设置
            handle.Setting_system_click()
        #3.点击退出
            handle.Setting_system_loginout_click()
        #4.点击确定
            handle.Setting_system_loginout_confirm_click()
        except Exception as err:
            logging.error("Error Information Loginout Inside : %s" % err)
            raise err