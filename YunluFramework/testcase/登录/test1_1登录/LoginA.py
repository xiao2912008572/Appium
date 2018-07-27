__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from YunluFramework.testcase.登录.test1_1登录 import *


# 登录
class LoginA:
    # 1.初始化
    def __init__(self):
        # 1.创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')
        # 2.获取截图路径、日志路径、日志名
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名
        # 3.创建日志模块
        self.log = Log(self.logfile)

    # 2.登录-公用方法
    def login(self, driver, phone, password):
        # 创建_OrgSpaceTeamHandle公有定位控件对象
        handle = LOGINHANDLE2(driver)
        sleep(1)
        try:

            # 登录首页
            if driver.find_elements_by_id("com.yunlu6.stone:id/main_login") != []:
                # 1.点击账号密码登录
                handle.Login_byAccount_click()
                self.log.info('点击账号密码登录')

                # 2.输入手机号+密码
                handle.Login_phone_sendkeys(phone)
                self.log.info('输入手机号：{0}'.format(phone))
                handle.Login_password_sendkeys(password)
                self.log.info('输入密码：{0}'.format(password))

                # 3.点击登录
                handle.Login_loginbtn_click()
                self.log.info('点击登录')
                sleep(1)

            # 输入框页
            else:
                #1.点击账号密码登录
                handle.Login_byAccount_click()
                self.log.info('点击账号密码登录')

                # 2.输入手机号+密码
                handle.Login_phone_sendkeys(phone)
                self.log.info('输入手机号：{0}'.format(phone))
                handle.Login_password_sendkeys(password)
                self.log.info('输入密码：{0}'.format(password))

                # 3.点击登录
                handle.Login_loginbtn_click()
                self.log.info('点击登录')
                sleep(1)

        except Exception as err:
            self.log.error("LoginA Inside : %s" % err)
            raise err
