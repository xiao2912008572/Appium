__author__ = 'xiaoj'
# -*- coding: utf-8 -*-
import sys
import os
import unittest
from time import sleep
from appium import webdriver
import logging
from StoneAPP.Connect import Connect
from StoneAPP.UploadPic import UploadPic
from StoneAPP.DeletePic import DeletePic
from StoneAPP.AllTools.Tools import Tools
from StoneAPP.AllTools.Config import Config


#使用已登录的账号进行浏览产品
class yunku_Edit(unittest.TestCase):
    def test_edit(self):
        cnn = Connect()
        driver = cnn.connect()
        tools = Tools(driver)#tools工具

        cf = Config()
        screen_path = cf.get_PATH('yunku',"path_001")#通过配置文件获取截图的路径
        log_path = cf.get_PATH('yunku','log_001')#通过配置文件获取日志的路径

        try:
            tools.coverUpdate(screen_path)#覆盖更新日志,覆盖更新截图
            tools.getLog(log_path)#打印日志
            #上传图片
            pic = UploadPic()
            pic.uploadpic(driver)
            tools.getScreenShot(screen_path,'上传后云库检查')#截图

            #点击云库第一张照片
            driver.find_elements_by_id("com.yunlu6.stone:id/cloudlibrary_image_item")[0].click()
            driver.find_element_by_id("com.yunlu6.stone:id/title_main_tv_more_menu").click()#点击下拉框
            driver.find_element_by_id("com.yunlu6.stone:id/btn_share_space").click()#点击"编辑"
            tools.getScreenShot(screen_path,'编辑页面检查')#截图

            #点击编辑框，改名为"产品图片001"
            driver.find_element_by_id("com.yunlu6.stone:id/image_edit_et_name").send_keys(u"产品名称001")

            #填写备注，"产品备注001"
            driver.find_element_by_id("com.yunlu6.stone:id/image_edit_et_remark").send_keys(u"产品备注001")

            #点击保存
            driver.save_screenshot("C地址拼接:\\Users\\xiaoj\Desktop\screenshot\云库图片编辑\编辑中页面检查.png")
            driver.find_element_by_id("com.yunlu6.stone:id/btn_image_edit_save").click()

            #检查编辑后的输入显示
            proname = driver.find_element_by_id("com.yunlu6.stone:id/title_main_tv_more_title")
            self.assertEqual(proname.text,"产品名称001",msg="名称不OK")
            print("-----编辑后:名称检查OK------")

            proremark = driver.find_element_by_id("com.yunlu6.stone:id/tv_remark")
            self.assertEqual(proremark.text,"产品备注001",msg="备注不OK")
            print("-----编辑后:备注检查OK------")

            sleep(1)
            tools.getScreenShot(screen_path,'编辑后页面检查')#截图

            #返回云库
            driver.find_element_by_id("com.yunlu6.stone:id/title_main_back_more_icon").click()

            #删除图片，还原云库
            deletepic = DeletePic()
            deletepic.deletepic(driver)

            #删除图片后云库检查
            tools.getScreenShot(screen_path,'云库删除后检查')#截图
            logging.info("susscess@@!!!!!!")#宣布成功
            driver.quit()#退出

        except Exception as e:
            tools.getScreenShot(screen_path,'exception')#截图
            logging.info("error@@@@!!!!!!")#打印错误的日志
            driver.quit()



