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
class contact_Talk(unittest.TestCase):
    def test_talkContact(self):
        #连接信息
        cnn = Connect()
        driver = cnn.connect()
        tools = Tools(driver)#tools工具

        cf = Config()
        screen_path = cf.get_PATH('contact',"path_005")#通过配置文件获取截图的路径
        log_path = cf.get_PATH('contact','log_005')#通过配置文件获取日志的路径
        try:
            tools.coverUpdate(screen_path)#覆盖更新日志,覆盖更新截图
            tools.getLog(log_path)#打印日志
            #点击人脉列表页面
            driver.find_element_by_id("com.yunlu6.stone:id/navi_item_connection").click()
            sleep(1)
            # 15102761413  12345678

            #搜索新增人脉
            driver.find_element_by_id("com.yunlu6.stone:id/img_btn_search").click()
            driver.find_element_by_id("com.yunlu6.stone:id/et_search").send_keys(u"金天浩")
            driver.find_element_by_id("com.yunlu6.stone:id/iv").click()
            sleep(1)

            #查看该人脉相关信息
            driver.find_element_by_id("com.yunlu6.stone:id/iv_arrow").click()
            sleep(2)
            tools.getScreenShot(screen_path,'查看该人脉名片')#截图

            #点击单人会话按钮，开始会话
            driver.find_element_by_id("com.yunlu6.stone:id/edit_text").click()
            sleep(1)
            driver.find_element_by_id("com.yunlu6.stone:id/message_content_msgcontent").send_keys(u"你好")#发消息
            driver.find_element_by_id("com.yunlu6.stone:id/iv_emoji").click()#点击表情包按钮
            sleep(1)
            driver.find_elements_by_id("com.yunlu6.stone:id/item_iv_face")[0].click()#选择第一个表情
            driver.find_element_by_id("com.yunlu6.stone:id/message_content_send").click()#点击发送
            tools.getScreenShot(screen_path,'发送消息页面')#截图

            #返回人脉列表
            driver.find_element_by_id("com.yunlu6.stone:id/title_main_more_back").click()#点击返回
            driver.find_element_by_id("com.yunlu6.stone:id/iv_back").click()#点击返回
            driver.find_element_by_id("com.yunlu6.stone:id/iv_back").click()#点击返回
            driver.find_element_by_id("com.yunlu6.stone:id/iv_back").click()#点击返回

            #----------------------------------登录另一个账号查看----------------------------------------
            #换完名片之后，要去另一个账号检查是否成功收到消息
            logout = Logout()
            logout.userLogout(driver)
            sleep(1)
            login = Login()
            login.userLogin(driver,15102761413,12345678)
            sleep(1)

            # text = driver.find_element_by_class_name("android.widget.TextView")#获取会话条数
            # self.assertEqual(text.text,'2',msg="条数显示错误")#检查会话条数显示是否正确
            # print("-----------会话消息条数显示有误--------------")

            driver.find_element_by_id("com.yunlu6.stone:id/icon_message").click()#点击会话按钮
            driver.save_screenshot("C地址拼接:\\Users\\xiaoj\Desktop\screenshot\人脉单人会话\收到会话消息.png")#后期要调整的
            driver.find_element_by_id("com.yunlu6.stone:id/msgitem_arrow").click()
            tools.getScreenShot(screen_path,'单人会话详情页')#截图，后期要调整的

            #返回主页面
            driver.find_element_by_id("com.yunlu6.stone:id/title_main_more_back").click()#返回
            driver.find_element_by_id("com.yunlu6.stone:id/buildstione_backe").click()#返回


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


