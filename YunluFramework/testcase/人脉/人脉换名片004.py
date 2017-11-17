__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import sys
import os
import unittest
from time import sleep
from appium import webdriver
import logging
from StoneAPP.Connect import Connect
from StoneAPP.AddContact import AddContact
from StoneAPP.Login import Login
from StoneAPP.Logout import Logout
from StoneAPP.AllTools.Tools import Tools
from StoneAPP.AllTools.Config import Config


#使用已登录的账号进行浏览产品
class contact_Exc(unittest.TestCase):
    def test_excContact(self):
        cnn = Connect()
        driver = cnn.connect()
        tools = Tools(driver)#tools工具

        cf = Config()
        screen_path = cf.get_PATH('contact',"path_004")#通过配置文件获取截图的路径
        log_path = cf.get_PATH('contact','log_004')#通过配置文件获取日志的路径
        try:
            tools.coverUpdate(screen_path)#覆盖更新日志,覆盖更新截图
            tools.getLog(log_path)#打印日志
            #点击搜索框，搜索"肖静远"
            sleep(2)
            driver.find_element_by_id("com.yunlu6.stone:id/navi_item_connection").click()#点击人脉列表
            driver.find_element_by_id("com.yunlu6.stone:id/img_btn_search").click()#搜索框
            driver.find_element_by_id("com.yunlu6.stone:id/et_search").send_keys(u"肖静远")
            driver.find_element_by_id("com.yunlu6.stone:id/iv").click()
            sleep(1)
            tools.getScreenShot(screen_path,'搜索结果')#截图

            #点击搜索出来的联系人
            sleep(2)
            driver.find_element_by_id("com.yunlu6.stone:id/iv_arrow").click()#点击联系人
            sleep(2)
            driver.find_element_by_id("com.yunlu6.stone:id/iv_more").click()#下拉框
            driver.find_element_by_id("com.yunlu6.stone:id/card_exchange").click()#名片设置
            sleep(1)
            tools.getScreenShot(screen_path,'名片设置界面')#截图

            #点击预览，发送
            driver.find_element_by_name("预览").click()
            driver.find_element_by_name("发送名片").click()
            sleep(1)
            tools.getScreenShot(screen_path,'发送名片成功')#截图

            #返回到人脉首页
            driver.find_element_by_id("com.yunlu6.stone:id/iv_back").click()#点击返回
            driver.find_element_by_id("com.yunlu6.stone:id/iv_back").click()#点击返回
            driver.find_element_by_id("com.yunlu6.stone:id/iv_back").click()#点击返回

            #----------------------------------登录另一个账号查看----------------------------------------
            #换完名片之后，要去另一个账号检查是否成功收到消息
            logout = Logout()
            logout.userLogout(driver)
            sleep(1)
            login = Login()
            login.userLogin(driver,17607136211,12345678)
            sleep(1)
            tools.getScreenShot(screen_path,'申请截图')#截图，后期要调整的

            #------------------------------------退出当前账号，登录原始账号-------------------------------
            logout = Logout()
            logout.userLogout(driver)
            sleep(1)
            login = Login()
            login.userLogin(driver,13027104206,12345678)
            sleep(1)
            logging.info("susscess@@!!!!!!")#宣布成功
            driver.quit()#退出

        except Exception as e:
            tools.getScreenShot(screen_path,'exception')#截图
            logging.info("error@@@@!!!!!!")#打印错误的日志
            driver.quit()




