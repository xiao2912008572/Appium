__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import unittest
from time import sleep
import logging
from StoneAPP.Connect import Connect
from StoneAPP.AllTools.Tools import Tools
from StoneAPP.AllTools.Config import Config
from StoneAPP.云库._Yunku_ import Yunku
from StoneAPP.空间._Space_ import Space
import random

#云库如偏分类产品库

class yunku_FenLei(unittest.TestCase):
    @classmethod
    def setUpClass(self):#修饰器，最开始执行
        #建立连接信息
        cnn = Connect()
        self.driver = cnn.connect()
        #创建工具类
        self.tools = Tools(self.driver)#tools工具
        #创建_Yunku_公有定位控件对象
        #创建_Space_公有定位控件对象
        self.yunku = Yunku(self.driver)
        self.space = Space(self.driver)
        #创建读取配置信息对象
        cf = Config()
        #获取截图路径、日志路径、日志名
        self.screen_path = cf.get_PATH('yunku',"path_002")#通过配置文件获取截图的路径
        self.log_path = cf.get_PATH('yunku','log_002')#通过配置文件获取日志的路径
        self.filename = cf.get_PATH('yunku','filename_002')#日志文件名
        sleep(2)
    def test_fenlei(self):
        try:
            self.tools.coverUpdate(self.log_path,self.screen_path)#覆盖更新日志,覆盖更新截图
            self.tools.getLog(self.filename)#打印日志
            #点击进入云库界面
            self.yunku.Jryk().click()
            sleep(1)
            self.tools.getScreenShot(self.screen_path,'main')#截main图

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
            self.yunku.Xc_Zp()[r].click()#随机添加照片
            self.yunku.Complete().click()#点击完成
            # driver.implicitly_wait(10)#智能等待10秒
            sleep(10)

            #点击上传的图片
            #通过查看该照片详情删除刚上传的照片
            self.tools.getScreenShot(self.screen_path,'上传后云库检查')
            self.yunku.Yk_Zp()[0].click()#点击第一张照片
            self.yunku.Main_menu().click()#点击右上角主菜单
            sleep(1)

            #点击分类
            self.yunku.Main_menu_classify().click()
            sleep(1)
            self.tools.getScreenShot(self.screen_path,'分类到页面检查')

            #选择分类到"xjy机构"
            self.yunku.Main_menu_classify_xjy_Org().click()
            #选择分类到产品库
            self.yunku.Main_menu_classify_product().click()
            #点击"√"按钮
            self.yunku.Title_tv_menu().click()
            sleep(1)
            self.tools.getScreenShot(self.screen_path,'分类后云库检查')#截图

            #检查xjy机构的产品库是否有刚才传过来的图片
             #1.选择空间列表
            self.space.Jrkj().click()
             #2.选择"xjy机构"
            self.space.Jrkj_xjy_company_org().click()
             #3.点击产品列表
            self.space.Main_menu().click()#主菜单
            self.space.Main_menu_company_product().click()#产品栏
             #4.点击添加产品
            self.space.Main_menu_company_product_new().click()#新增
             #5.点击添加照片，选择产品库
            self.space.Main_menu_company_product_new_addphoto().click()#点击添加照片
            self.space.Main_menu_company_product_new_addphoto_Bywifisync().click()#选择产品库
            sleep(1)
            self.tools.getScreenShot(self.screen_path,'产品库检查')#截图





            logging.info("susscess@@!!!!!!")#宣布成功
        finally:
            self.tools.getScreenShot(self.screen_path,'finally')#截图
            logging.info("finally@@!!!!!!!")#打印错误的日志
            self.driver.quit()


