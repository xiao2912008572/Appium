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
from StoneAPP.AllTools.Tools import Tools
from StoneAPP.AllTools.Config import Config


#使用已登录的账号进行浏览产品
class contact_Browse(unittest.TestCase):
    def test_browseContact(self):
        cnn = Connect()
        driver = cnn.connect()
        tools = Tools(driver)#tools工具

        cf = Config()
        screen_path = cf.get_PATH('contact',"path_002")#通过配置文件获取截图的路径
        log_path = cf.get_PATH('contact','log_002')#通过配置文件获取日志的路径
        try:
            tools.coverUpdate(screen_path)#覆盖更新日志,覆盖更新截图
            tools.getLog(log_path)#打印日志
            #添加人脉
            contact = AddContact()
            contact.addContact(driver)

            #点击返回人脉列表页面
            driver.find_element_by_id("com.yunlu6.stone:id/title_main_back_more_icon").click()
            sleep(1)

            #添加人脉后，刷新人脉列表
            driver.swipe(497,634,497,1103)
            sleep(1)

            #搜索新增人脉
            driver.find_element_by_id("com.yunlu6.stone:id/img_btn_search").click()
            driver.find_element_by_id("com.yunlu6.stone:id/et_search").send_keys(u"肖静远")
            driver.find_element_by_id("com.yunlu6.stone:id/iv").click()
            sleep(1)
            tools.getScreenShot(screen_path,'搜索新增人脉结果')#截图

            #查看该人脉相关信息
            driver.find_element_by_id("com.yunlu6.stone:id/iv_arrow").click()
            sleep(2)
            tools.getScreenShot(screen_path,'查看该人脉名片')#截图

            #查看该人脉下的空间
             #楚正和珠宝
            driver.find_element_by_id("com.yunlu6.stone:id/tv_name").click()
            sleep(2)
            tools.getScreenShot(screen_path,'通道设置空间浏览')#截图
            logging.info("susscess@@!!!!!!")#宣布成功
            driver.quit()#退出

        except Exception as e:
            tools.getScreenShot(screen_path,'exception')#截图
            logging.info("error@@@@!!!!!!")#打印错误的日志
            driver.quit()





