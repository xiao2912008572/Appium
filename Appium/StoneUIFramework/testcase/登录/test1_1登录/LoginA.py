__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from time import sleep
import logging
from StoneUIFramework.public.common.publicfunction import Tools
from StoneUIFramework.public.handle.login.LOGINHANDLE2 import _LOGINHANDLE2


# 登录
class LoginA:
    def __init__(self):
       pass

    def login(self, driver,phone,password):
        #创建工具类
        tools = Tools(driver)  #tools工具
        #创建_OrgSpaceTeamHandle公有定位控件对象
        handle = _LOGINHANDLE2(driver)
        sleep(1)
        try:
            #登录首页
            if driver.find_elements_by_id("com.yunlu6.stone:id/main_login") != []:
            #1.点击登录
                handle.Login_click()
            #2.输入手机号+密码
                handle.Login_phone_sendkeys(phone)
                handle.Login_password_sendkeys(password)
            #3.点击登录
                handle.Login_loginbtn_click()
                sleep(1)
            #输入框页
            else:
                #2.输入手机号+密码
                handle.Login_phone_sendkeys(phone)
                handle.Login_password_sendkeys(password)
            #3.点击登录
                handle.Login_loginbtn_click()
                sleep(1)
        except Exception as err:
            logging.error("Error Information TeamAssignJob Inside : %s" % err)
            raise err