__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import unittest
from time import sleep
import logging
from StoneAPP.Connect import Connect
from StoneAPP.AllTools.Tools import Tools
from StoneAPP.AllTools.Config import Config
from StoneAPP.云库._Yunku_ import Yunku
import random

#云库上传图片
class yunku_ShangChuan(unittest.TestCase):
    @classmethod
    def setUpClass(self):#修饰器，最开始执行
        #建立连接信息
        cnn = Connect()
        self.driver = cnn.connect()
        #创建工具类
        self.tools = Tools(self.driver)#tools工具
        #创建_Yunku_公有定位控件对象
        self.yunku = Yunku(self.driver)
        #创建读取配置信息对象
        cf = Config()
        #获取截图路径、日志路径、日志名
        self.screen_path = cf.get_PATH('yunku',"path_001")#通过配置文件获取截图的路径
        self.log_path = cf.get_PATH('yunku','log_001')#通过配置文件获取日志的路径
        self.filename = cf.get_PATH('yunku','filename_001')#日志文件名
        sleep(2)
    def test_shangchuan(self):
        try:
            self.tools.coverUpdate(self.log_path,self.screen_path)#覆盖更新日志,覆盖更新截图
            self.tools.getLog(self.filename)#打印日志
            #点击进入云库界面
            self.yunku.Jryk().click()
            sleep(1)
            self.tools.getScreenShot(self.screen_path,'main')#截图

            #右上角下拉框
            self.yunku.Yunku_Sgd().click()
            sleep(1)

             #点击"+文件"
            self.yunku.Jwj().click()

            #选择相册方式添加1张照片
            self.yunku.Xc().click()#点击相册
            sleep(1)
            self.tools.getScreenShot(self.screen_path,'本地相册图片')#截图
            r = random.randint(0,11)
            self.yunku.Xc_Zp()[r].click()#点击第1张照片
            self.yunku.Complete().click()#点击完成
            # driver.implicitly_wait(10)#智能等待10秒
            sleep(10)

            #判断等待
            # if self.driver.find_element_by_id("com.yunlu6.stone:id/gridview").is_displayed():
            #     sleep(20)

            #通过查看该照片详情删除刚上传的照片
            self.tools.getScreenShot(self.screen_path,'上传后云库检查')
            self.yunku.Yk_Zp()[0].click()#点击第一张照片
            self.yunku.Main_menu().click()#点击右上角主菜单
            sleep(1)
            self.yunku.Main_menu_edit().click()#点击右上角主菜单下的编辑
            self.yunku.Main_menu_edit_delete().click()#点击删除按钮
            sleep(1)

            self.tools.getScreenShot(self.screen_path,'删除待确认图片')
            self.yunku.Confirm().click()#点击删除确认按钮
            sleep(1)
            self.tools.getScreenShot(self.screen_path,'删除后云库检查')
            logging.info("success@@!!!!!!!")#宣布成功
        finally:
            self.tools.getScreenShot(self.screen_path,'finally')#截图
            logging.info("finally@@!!!!!!!")#打印错误的日志
            self.driver.quit()


