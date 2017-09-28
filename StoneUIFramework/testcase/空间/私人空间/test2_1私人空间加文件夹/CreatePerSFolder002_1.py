__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import unittest
from time import sleep

from StoneUIFramework.public.common.Connect import Connect
from StoneUIFramework.public.common.publicfunction import Tools
from StoneUIFramework.config.globalparam import GlobalParam
from StoneUIFramework.public.handle.space.SPACEHANDLE5 import _SPACEHANDLE5

from StoneUIFramework.testcase.空间.私人空间.test2_1私人空间加文件夹.CreatePersonSpace import CreatePersonSpace
from StoneUIFramework.testcase.空间.私人空间.test2_1私人空间加文件夹.ClosePersonSpace import ClosePersonSpace
from StoneUIFramework.testcase.空间.私人空间.test2_1私人空间加文件夹.CreatePerSFolder import CreatePerSFolder
from StoneUIFramework.testcase.空间.私人空间.test2_1私人空间加文件夹.DeletePerSFolder import DeletePerSFloder
from StoneUIFramework.public.common.datainfo import DataInfo
from StoneUIFramework.public.common.log import Log

#加文件夹
class perspace_NewFloderP(unittest.TestCase):
    @classmethod#装饰器，类方法
    def setUpClass(self):#最开始执行
        #1.建立连接信息
        cnn = Connect()
        self.driver = cnn.connect()
        #2.创建工具类
        self.tools = Tools(self.driver)#tools工具
        #3.创建_SPACEHANDLE5公有定位控件对象
        self.handle = _SPACEHANDLE5(self.driver)
        #4.创建读取配置信息对象
        cf = GlobalParam('config','path_file.conf')
        # 5. 获取截图路径、日志路径、日志名
        self.screen_path = cf.getParam('space', "per_path_001_1")  # 通过配置文件获取截图的路径
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名
        # 创建日志记录模块
        self.log = Log(self.logfile)
        #6.创建Createspace、Closespace、CreatePerSFolder对象
        self.cr = CreatePersonSpace()
        self.cl = ClosePersonSpace()
        self.cpf = CreatePerSFolder()
        self.cpl = DeletePerSFloder()
        sleep(2)
        #7.准备测试数据
        d = DataInfo("space.xls")#创建DataInfo()对象
        self.spacename = d.cell("test006-私人空间",2,13)#空间名:appium私人空间
        self.foldername1 = d.cell("test006-私人空间",2,14)#文件夹1:appium文件夹
        # self.foldername1 = d.cell("test006",2,14)#文件夹1名:appium文件夹
    def test_pernewfolder(self):
        try:
            self.log.info("------------START:test2_1私人空间加文件夹CreatePerFolder002_1.py------------")
            #1.进入空间列表
            self.handle.Kjlb_click()
            self.log.info('点击进入空间列表')
            # #2.点击主菜单
            # self.handle.Kjlb_mainmenu_click()
            # #3.点击+私人空间
            # self.handle.Kjlb_mainmenu_newpersonspace_click()
            #4.创建私人空间
            if self.driver.find_elements_by_name(self.spacename) != []:#检查当前的私人空间是否已经存在,如果存在就关闭
                #4.1进入空间-菜单栏-编辑
                self.handle.Kjlb_browseorgspaceByName_click(self.spacename)
                self.handle.Kjlb_browseperspace_menu_click()
                self.handle.Kjlb_browseperspace_menu_edit_click()
                #4.2检查是否存在文件夹
                if self.driver.find_elements_by_id("com.yunlu6.stone:id/editlayout_folder_dele") != []:
                    #4.2.0返回-返回空间列表
                    self.handle.Kjlb_browseperspace_menu_edit_back_click()
                    self.handle.Kjlb_browseperspace_back_click()
                    # 4.2.1删除文件夹
                    self.cpl.deletePerSFloder(self.driver,self.spacename)
                    #4.2.2先关闭空间
                    self.cl.closePersonSpace(self.driver,self.spacename)
                    #4.2.3再创建空间
                    self.cr.createPersonSpace(self.driver,self.spacename)
                    #4.2.4创建文件夹
                    self.cpf.createPerSFolder(self.driver,self.spacename,self.foldername1)
                    #4.2.5#删除文件夹
                    self.cpl.deletePerSFloder(self.driver,self.spacename)
                    #4.2.6再关闭空间
                    self.cl.closePersonSpace(self.driver,self.spacename)
                else:
                    self.driver.find_element_by_id("com.yunlu6.stone:id/title_back_icon").click()#返回上一层
                    sleep(1)
                    self.driver.find_element_by_id("com.yunlu6.stone:id/title_main_back_more_icon").clear()#返回空间列表
                    sleep(1)
                    #4.2.7先关闭空间
                    self.cl.closePersonSpace(self.driver,self.spacename)
                    #4.2.8再创建空间
                    self.cr.createPersonSpace(self.driver,self.spacename)
                    #4.2.9创建文件夹
                    self.cpf.createPerSFolder(self.driver,self.spacename,self.foldername1)
                    #4.2.10#删除文件夹
                    self.cpl.deletePerSFloder(self.driver,self.spacename)
                    #4.2.11再关闭空间
                    self.cl.closePersonSpace(self.driver,self.spacename)
            else:
                #4.3先创建空间
                self.cr.createPersonSpace(self.driver,self.spacename)#创建
                #4.4创建文件夹
                self.cpf.createPerSFolder(self.driver,self.spacename,self.foldername1)
                #4.5删除文件夹
                self.cpl.deletePerSFloder(self.driver,self.spacename)
                #4.6再关闭空间
                self.cl.closePersonSpace(self.driver,self.spacename)
            self.log.info('------------END:test2_1私人空间加文件夹CreatePerFolder002_1.py------------')
        except Exception as err:
            self.tools.getScreenShot(self.screen_path,"ExceptionShot")
            self.log.error("Outside : %s"%err)
            raise err
        finally:
            self.driver.quit()