__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import sys
import os
import unittest
from time import sleep
from appium import webdriver
import logging
from StoneAPP.Connect import Connect
from StoneAPP.DelContact import DelContact
from StoneAPP.AllTools.Tools import Tools
from StoneAPP.AllTools.Config import Config




#使用已登录的账号进行浏览产品
class contact_Del(unittest.TestCase):
    def test_delContact(self):
        cnn = Connect()
        driver = cnn.connect()
        tools = Tools(driver)#tools工具

        cf = Config()
        screen_path = cf.get_PATH('contact',"path_003")#通过配置文件获取截图的路径
        log_path = cf.get_PATH('contact','log_003')#通过配置文件获取日志的路径
        try:
            tools.coverUpdate(screen_path)#覆盖更新日志,覆盖更新截图
            tools.getLog(log_path)#打印日志
            #删除人脉
            contact = DelContact()
            contact.delContact(driver)

            #还原人脉
            driver.find_element_by_id("com.yunlu6.stone:id/title_main_back_more_icon").click()#点击返回
            driver.find_element_by_name("黑名单").click()#点击黑名单
            sleep(1)
            driver.find_element_by_name("肖静远").click()#点击联系人
            sleep(3)
            driver.find_element_by_id("com.yunlu6.stone:id/iv_more").click()#右上角下拉框
            driver.find_element_by_id("com.yunlu6.stone:id/ll_recover").click()#点击还原按钮
            driver.find_element_by_id("com.yunlu6.stone:id/title_main_back_more_icon").click()#点击返回
            driver.find_element_by_id("com.yunlu6.stone:id/iv_back").click()#点击返回人脉
            logging.info("susscess@@!!!!!!")#宣布成功
            driver.quit()

        except Exception as e:
            tools.getScreenShot(screen_path,'exception')#截图
            logging.info("error@@@@!!!!!!")#打印错误的日志
            driver.quit()





