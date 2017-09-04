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
class contact_Add(unittest.TestCase):
    def test_addContact(self):
        cnn = Connect()
        driver = cnn.connect()
        tools = Tools(driver)#tools工具

        cf = Config()
        screen_path = cf.get_PATH('contact',"path_001")#通过配置文件获取截图的路径
        log_path = cf.get_PATH('contact','log_001')#通过配置文件获取日志的路径
        try:
            tools.coverUpdate(screen_path)#覆盖更新日志,覆盖更新截图
            tools.getLog(log_path)#打印日志
            sleep(1)

            #添加人脉
            contact = AddContact()
            contact.addContact(driver)
            logging.info("susscess@@!!!!!!")#宣布成功
            driver.quit()

        except Exception as e:
            tools.getScreenShot(screen_path,'exception')#截图
            logging.info("error@@@@!!!!!!")#打印错误的日志
            driver.quit()






