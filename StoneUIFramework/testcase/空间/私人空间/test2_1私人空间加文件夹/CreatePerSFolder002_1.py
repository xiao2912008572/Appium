__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from StoneUIFramework.testcase.空间.私人空间.test2_1私人空间加文件夹 import *


# 加文件夹
@ddt.ddt
class perspace_NewFloderP(unittest.TestCase):
    # 1.全局测试数据
    d = DataInfo("space.xls")  # 创建DataInfo()对象
    spacename_1 = d.cell("test006-私人空间", 2, 13)  # 空间名:appium私人空间
    foldername1_1 = d.cell("test006-私人空间", 2, 14)  # 文件夹1:appium文件夹

    # 2.初始化
    def setUp(self):
        # 1.建立连接信息
        cnn = Connect()
        self.driver = cnn.connect()
        # 2.创建工具类
        self.tools = Tools(self.driver)  # tools工具
        # 3.创建_SPACEHANDLE5公有定位控件对象
        self.handle = SPACEHANDLE5(self.driver)
        # 4.创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')
        # 5. 获取截图路径、日志路径、日志名
        self.screen_path = cf.getParam('space', "per_path_001_1")  # 通过配置文件获取截图的路径
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名
        # 6.创建Createspace、Closespace、CreatePerSFolder对象
        self.cr = CreatePersonSpace()
        self.cl = ClosePersonSpace()
        self.cpf = CreatePerSFolder()
        self.cpl = DeletePerSFloder()
        sleep(2)
        # 7.创建日志记录模块
        self.log = Log(self.logfile)
        # 8.打印日志
        self.log.info('****************************************用例开始！****************************************')
        self.log.info("------------START:test2_1私人空间加文件夹CreatePerFolder002_1.py------------")

    # 3.释放资源
    def tearDown(self):
        # 1.打印日志
        self.log.info('------------END:test2_1私人空间加文件夹CreatePerFolder002_1.py------------')
        self.log.info('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~用例结束！~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        # 2.关闭driver
        self.driver.quit()

    # 4.测试用例
    @ddt.data([spacename_1, foldername1_1])
    @ddt.unpack
    def test_pernewfolder(self, spacename, foldername1, foldername2=None, foldername3=None):
        try:
            # 1.进入空间列表
            self.handle.Kjlb_click()
            self.log.info('点击进入空间列表')
            # #2.点击主菜单
            # self.handle.Kjlb_mainmenu_click()
            # #3.点击+私人空间
            # self.handle.Kjlb_mainmenu_newpersonspace_click()
            # 4.创建私人空间
            if self.driver.find_elements_by_name(spacename) != []:  # 检查当前的私人空间是否已经存在,如果存在就关闭
                # 4.1进入空间-菜单栏-编辑
                self.handle.Kjlb_browseorgspaceByName_click(spacename)
                self.handle.Kjlb_browseperspace_menu_click()
                self.handle.Kjlb_browseperspace_menu_edit_click()
                # 4.2检查是否存在文件夹
                if self.driver.find_elements_by_id("com.yunlu6.stone:id/editlayout_folder_dele") != []:
                    # 4.2.0返回-返回空间列表
                    self.handle.Kjlb_browseperspace_menu_edit_back_click()
                    self.handle.Kjlb_browseperspace_back_click()
                    # 4.2.1删除文件夹
                    self.cpl.deletePerSFloder(self.driver, spacename)
                    # 4.2.2先关闭空间
                    self.cl.closePersonSpace(self.driver, spacename)
                    # 4.2.3再创建空间
                    self.cr.createPersonSpace(self.driver, spacename)
                    # 4.2.4创建文件夹
                    self.cpf.createPerSFolder(self.driver, spacename, foldername1)
                    # 4.2.5#删除文件夹
                    self.cpl.deletePerSFloder(self.driver, spacename)
                    # 4.2.6再关闭空间
                    self.cl.closePersonSpace(self.driver, spacename)
                else:
                    self.driver.find_element_by_id("com.yunlu6.stone:id/title_back_icon").click()  # 返回上一层
                    sleep(1)
                    self.driver.find_element_by_id("com.yunlu6.stone:id/title_main_back_more_icon").clear()  # 返回空间列表
                    sleep(1)
                    # 4.2.7先关闭空间
                    self.cl.closePersonSpace(self.driver, spacename)
                    # 4.2.8再创建空间
                    self.cr.createPersonSpace(self.driver, spacename)
                    # 4.2.9创建文件夹
                    self.cpf.createPerSFolder(self.driver, spacename, foldername1)
                    # 4.2.10#删除文件夹
                    self.cpl.deletePerSFloder(self.driver, spacename)
                    # 4.2.11再关闭空间
                    self.cl.closePersonSpace(self.driver, spacename)
            else:
                # 4.3先创建空间
                self.cr.createPersonSpace(self.driver, spacename)  # 创建
                # 4.4创建文件夹
                self.cpf.createPerSFolder(self.driver, spacename, foldername1)
                # 4.5删除文件夹
                self.cpl.deletePerSFloder(self.driver, spacename)
                # 4.6再关闭空间
                self.cl.closePersonSpace(self.driver, spacename)
        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("Outside : %s" % err)
            raise err
