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
class contact_Label(unittest.TestCase):
    def test_labelContact(self):
        cnn = Connect()
        driver = cnn.connect()
        tools = Tools(driver)#tools工具

        cf = Config()
        screen_path = cf.get_PATH('contact',"path_006")#通过配置文件获取截图的路径
        log_path = cf.get_PATH('contact','log_006')#通过配置文件获取日志的路径

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

            #先做标签检查，如果该联系人有标签，先置为空
            try:
                label = driver.find_element_by_id("com.yunlu6.stone:id/tag_view_label")
                label1 = label.find_elements_by_id("com.yunlu6.stone:id/tag_id")
                for l in label1[::-1]:#倒序检查
                    if l.is_enabled():
                        l.click()
            except Exception as e:
                print(e)

            #---------------------------A连接信息.先打一个标签测试---------------------------
            driver.find_element_by_name("同事").click()#点击同事标签
            tools.getScreenShot(screen_path,'选中某标签后')#截图
            driver.find_element_by_id("com.yunlu6.stone:id/iv_confirm").click()#确认

            #测试点:
            # 1.重新查看标签中，标签是否打上
            # 2.人脉列表搜索，标签筛选功能，是否有该用户(多个标签时再测试)
            #---1.---
            driver.find_element_by_id("com.yunlu6.stone:id/iv_more").click()#点击下拉框
            driver.find_element_by_id("com.yunlu6.stone:id/label").click()#点击标签栏
            sleep(1)
            tools.getScreenShot(screen_path,'标签检查是否打上')#截图

                #此时可以做取消勾选检查，如果打上了的话
            driver.find_element_by_id("com.yunlu6.stone:id/tag_view_label").find_element_by_name("同事").click()#取消勾选标签
            tools.getScreenShot(screen_path,'取消选中某标签后')#截图
            driver.find_element_by_id("com.yunlu6.stone:id/iv_confirm").click()#点击确认

                #再次检查取消标签勾选是否生效
            driver.find_element_by_id("com.yunlu6.stone:id/iv_more").click()#点击下拉框
            driver.find_element_by_id("com.yunlu6.stone:id/label").click()#点击标签栏
            sleep(1)
            tools.getScreenShot(screen_path,'标签检查是否取消')#截图

            #---------------------------B系统地址.打多个标签测试---------------------------
            #测试点:
            # 1.重新查看标签中，标签是否打上
            # 2.人脉列表搜索，标签筛选功能，是否有该用户(多个标签时再测试)
            driver.find_element_by_name("同事").click()#同事标签
            driver.find_element_by_name("朋友").click()#朋友标签
            driver.find_element_by_name("职业").click()#职业栏
            driver.find_element_by_name("IT互联网").click()#IT互联网标签
            driver.find_element_by_name("性格").click()#性格栏
            driver.find_element_by_name("不拘小节").click()#不拘小节标签
            sleep(1)
            tools.getScreenShot(screen_path,'打多个标签')#截图
            driver.find_element_by_id("com.yunlu6.stone:id/iv_confirm").click()#点击确认
            sleep(2)

            #---1.---再次确认多标签是否打上
            driver.find_element_by_id("com.yunlu6.stone:id/iv_more").click()#点击下拉框
            driver.find_element_by_id("com.yunlu6.stone:id/label").click()#点击标签栏

            #断言检查
            id1 = driver.find_element_by_id("com.yunlu6.stone:id/tag_view_label")#先看标签元素框
            label = id1.find_elements_by_id("com.yunlu6.stone:id/tag_id")#再标签元素框下查找元素
            try:
                self.assertEqual(label[0].text,'IT互联网',msg="error\n")
                # print("IT互联网:标签已打上")
            except Exception as e:
                print("错误信息:%s"%e)

            try:
                self.assertEqual(label[1].text,'不拘小节',msg="error\n")
                # print("不拘小节:标签已打上")
            except Exception as e:
                print("错误信息:%s"%e)

            try:
                self.assertEqual(label[2].text,'同事',msg="error\n")
                # print("同事:标签已打上")
            except Exception as e:
                print("错误信息:%s"%e)

            try:
                self.assertEqual(label[3].text,'朋友',msg="error\n")
                # print("朋友:标签已打上")
            except Exception as e:
                print("错误信息:%s"%e)

            sleep(1)
            tools.getScreenShot(screen_path,'多标签确认')#截图

            #---2.---标签筛选分别查看上述几个标签中是否有该人脉
            driver.find_element_by_id("com.yunlu6.stone:id/iv_back").click()#返回
            driver.find_element_by_id("com.yunlu6.stone:id/iv_back").click()#返回
            driver.find_element_by_id("com.yunlu6.stone:id/iv_back").click()#返回

              #同事、朋友、不拘小节、IT互联网
            #检查同事标签
            Label = driver.find_elements_by_id("com.yunlu6.stone:id/item_name")
            driver.find_element_by_name("同事").click()
            try:
                for label in Label:
                    if label.text == '金天浩':
                        # print("同事标签:OK")
                        break
            except Exception as e :
                print("错误信息:%s"%e)
            driver.find_element_by_id("com.yunlu6.stone:id/iv_back").click()#返回上一页

            #检查朋友标签
            driver.find_element_by_name("朋友").click()
            try:
                for label in Label:
                    if label.text == '金天浩':
                        # print("朋友标签:OK")
                        break
            except Exception as e :
                print("错误信息:%s"%e)
            driver.find_element_by_id("com.yunlu6.stone:id/iv_back").click()#返回上一页

            #不拒小节标签检查
            driver.find_element_by_id("com.yunlu6.stone:id/et_search").send_keys(u"不拘小节")
            driver.find_element_by_id("com.yunlu6.stone:id/iv").click()
            try:
                for label in Label:
                    if label.text == '金天浩':
                        # print("不拘小节标签:OK")
                        break
            except Exception as e :
                print("错误信息:%s"%e)
            driver.find_element_by_id("com.yunlu6.stone:id/iv_back").click()#返回上一页

             #IT互联网标签检查
            driver.find_element_by_id("com.yunlu6.stone:id/et_search").send_keys(u"IT互联网")
            driver.find_element_by_id("com.yunlu6.stone:id/iv").click()
            try:
                for label in Label:
                    if label.text == '金天浩':
                        # print("IT互联网标签:OK")
                        break
            except Exception as e :
                print("错误信息:%s"%e)
            driver.find_element_by_id("com.yunlu6.stone:id/iv_back").click()#返回上一页

            #------------------搜索金天浩，取消所有标签，还原状态-----------------------
            driver.find_element_by_id("com.yunlu6.stone:id/img_btn_search").click()
            driver.find_element_by_id("com.yunlu6.stone:id/et_search").send_keys(u"金天浩")
            driver.find_element_by_id("com.yunlu6.stone:id/iv").click()
            sleep(1)

                #查看该人脉相关信息
            driver.find_element_by_id("com.yunlu6.stone:id/iv_arrow").click()#点击该人脉
            sleep(2)

                #打标签
            driver.find_element_by_id("com.yunlu6.stone:id/iv_more").click()#点击下拉框
            driver.find_element_by_id("com.yunlu6.stone:id/label").click()#点击标签栏

                #取消多个标签
            label = driver.find_elements_by_id("com.yunlu6.stone:id/tag_id")
            label[0].click()
            label[0].click()
            label[0].click()
            label[0].click()

            driver.find_element_by_id("com.yunlu6.stone:id/iv_confirm").click()#点击确认
            sleep(1)
            tools.getScreenShot(screen_path,'多标签取消确认')#截图

            #返回人脉列表
            driver.find_element_by_id("com.yunlu6.stone:id/iv_back").click()#点击返回
            driver.find_element_by_id("com.yunlu6.stone:id/iv_back").click()#点击返回
            driver.find_element_by_id("com.yunlu6.stone:id/iv_back").click()#点击返回
            driver.find_element_by_id("com.yunlu6.stone:id/iv_back").click()#点击返回
            logging.info("susscess@@!!!!!!")#宣布成功
            driver.quit()#退出

        except Exception as e:
            tools.getScreenShot(screen_path,'exception')#截图
            logging.info("error@@@@!!!!!!")#打印错误的日志
            driver.quit()