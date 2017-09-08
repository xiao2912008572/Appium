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
class contact_GroupChat(unittest.TestCase):
    def test_groupchatContact(self):
        cnn = Connect()
        driver = cnn.connect()
        tools = Tools(driver)#tools工具

        cf = Config()
        screen_path = cf.get_PATH('contact',"path_001")#通过配置文件获取截图的路径
        log_path = cf.get_PATH('contact','log_001')#通过配置文件获取日志的路径

        try:
            tools.coverUpdate(screen_path)#覆盖更新日志,覆盖更新截图
            tools.getLog(log_path)#打印日志
            #点击人脉列表页面
            sleep(2)
            driver.find_element_by_id("com.yunlu6.stone:id/navi_item_connection").click()
            sleep(1)
            # 15102761413  12345678

            #搜索人脉
            driver.find_element_by_id("com.yunlu6.stone:id/img_btn_search").click()
            driver.find_element_by_id("com.yunlu6.stone:id/et_search").send_keys(u"金天浩")
            driver.find_element_by_id("com.yunlu6.stone:id/iv").click()
            sleep(1)

            #查看该人脉相关信息
            driver.find_element_by_id("com.yunlu6.stone:id/iv_arrow").click()#点击该人脉
            sleep(2)
            tools.getScreenShot(screen_path,'查看该人脉名片')#截图

            #打标签
            driver.find_element_by_id("com.yunlu6.stone:id/iv_more").click()#点击下拉框
            driver.find_element_by_id("com.yunlu6.stone:id/label").click()#点击标签栏

            #---------------------------先打一个标签测试---------------------------
            driver.find_element_by_name("同事").click()#点击同事标签
            tools.getScreenShot(screen_path,'选中某标签后')#截图
            driver.find_element_by_id("com.yunlu6.stone:id/iv_confirm").click()#确认

            #返回人脉列表
            driver.find_element_by_id("com.yunlu6.stone:id/iv_back").click()#点击返回
            driver.find_element_by_id("com.yunlu6.stone:id/iv_back").click()#点击返回
            driver.find_element_by_id("com.yunlu6.stone:id/iv_back").click()#点击返回

            #-------------------------按标签"同事"进行群聊-------------------------
            #1.点击搜索框
            driver.find_element_by_id("com.yunlu6.stone:id/img_btn_search").click()
            #2.点击"同事标签"
            driver.find_element_by_name("同事").click()
            tools.getScreenShot(screen_path,'标签下人脉')#截图
            #3.点击群聊入口，并发送消息
            driver.find_element_by_name("点击进入群聊").click()
            sleep(1)
            tools.getScreenShot(screen_path,'群聊界面')#截图
            #4.发消息
            driver.find_element_by_id("com.yunlu6.stone:id/message_content_msgcontent").send_keys(u"你好")#发消息
            driver.find_element_by_id("com.yunlu6.stone:id/iv_emoji").click()#点击表情包按钮
            sleep(1)
            driver.find_elements_by_id("com.yunlu6.stone:id/item_iv_face")[0].click()#选择第一个表情
            driver.find_element_by_id("com.yunlu6.stone:id/message_content_send").click()#点击发送
            tools.getScreenShot(screen_path,'发送消息页面')#截图
            #5.查看群成员列表
            driver.find_element_by_id("com.yunlu6.stone:id/iv_to_message").click()#点击群成员图标
            sleep(1)
            tools.getScreenShot(screen_path,'群成员列表')#截图
            #6.返回人脉列表
            driver.find_element_by_id("com.yunlu6.stone:id/title_main_more_back").click()#点击返回
            driver.find_element_by_id("com.yunlu6.stone:id/title_main_more_back").click()#点击返回
            driver.find_element_by_id("com.yunlu6.stone:id/iv_back").click()#点击返回
            driver.find_element_by_id("com.yunlu6.stone:id/iv_back").click()#点击返回

            #----------------------------------登录另一个账号查看----------------------------------------
            #群聊发送消息后，要去另一个账号检查是否成功收到消息
            logout = Logout()
            logout.userLogout(driver)
            sleep(1)
            login = Login()
            login.userLogin(driver,15102761413,12345678)
            sleep(1)

            tools.getScreenShot(screen_path,'main页')#截图，后期调整
            driver.find_element_by_id("com.yunlu6.stone:id/icon_message").click()#点击会话按钮
            tools.getScreenShot(screen_path,'收到会话消息')#截图
            driver.find_element_by_id("com.yunlu6.stone:id/msgitem_arrow").click()
            tools.getScreenShot(screen_path,'单人会话详情页')#截图

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

            #-----------------------取消人脉标签，还原至初始状态-----------------------
            sleep(2)
            driver.find_element_by_id("com.yunlu6.stone:id/navi_item_connection").click()

            #搜索人脉
            driver.find_element_by_id("com.yunlu6.stone:id/img_btn_search").click()
            driver.find_element_by_id("com.yunlu6.stone:id/et_search").send_keys(u"金天浩")
            driver.find_element_by_id("com.yunlu6.stone:id/iv").click()
            sleep(1)

            #查看该人脉相关信息
            driver.find_element_by_id("com.yunlu6.stone:id/iv_arrow").click()#点击该人脉
            sleep(2)
            tools.getScreenShot(screen_path,'查看该人脉名片')#截图

            #取消标签
            driver.find_element_by_id("com.yunlu6.stone:id/iv_more").click()#点击下拉框
            driver.find_element_by_id("com.yunlu6.stone:id/label").click()#点击标签栏
            driver.find_elements_by_id("com.yunlu6.stone:id/tag_id")[0].click()#取消标签
            driver.find_element_by_id("com.yunlu6.stone:id/iv_confirm").click()#勾选

            #检查一下取消标签后的效果
            driver.find_element_by_id("com.yunlu6.stone:id/iv_more").click()#下拉框
            driver.find_element_by_id("com.yunlu6.stone:id/label").click()#标签
            sleep(1)
            tools.getScreenShot(screen_path,'取消标签检查')#截图
            logging.info("susscess@@!!!!!!")#宣布成功
            driver.quit()#退出

        except Exception as e:
            tools.getScreenShot(screen_path,'exception')#截图
            logging.info("error@@@@!!!!!!")#打印错误的日志
            driver.quit()



