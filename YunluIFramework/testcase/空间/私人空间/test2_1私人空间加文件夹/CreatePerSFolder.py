__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from YunluIFramework.testcase.空间.私人空间.test2_1私人空间加文件夹 import *


# 创建机构空间
class CreatePerSFolder:
    # 1.初始化
    def __init__(self):
        # 创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')
        # 获取截图路径、日志路径、日志名
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名
        # 创建日志模块
        self.log = Log(self.logfile)

    # 2.创建私人空间文件夹-公用方法
    def createPerSFolder(self, driver, spacename, foldername1=None, foldername2=None, foldername3=None):  # 最多三个文件夹
        # 1.创建工具类
        tools = Tools(driver)  # tools工具
        # 2.创建_SPACEHANDLE5公有定位控件对象
        handle = SPACEHANDLE5(driver)
        sleep(2)
        try:
            self.log.info('------START:test2_1私人空间加文件夹.CreatePerSFolder.py------')
            # 1.空间-菜单栏
            driver.find_element_by_name(spacename).click()
            self.log.info('点击{0}空间'.format(spacename))
            # handle.Kjlb_browseperspaceByName(spacename).click()
            handle.Kjlb_browseperspace_menu_click()
            self.log.info('点击菜单栏')
            # 2.+文件夹
            handle.Kjlb_browseperspace_menu_addfolder_click()
            self.log.info('点击+文件夹')
            # 3.输入文件夹名称-确定
            handle.Kjlb_browseperspace_menu_addfolder_foldername_sendkeys(foldername1)
            self.log.info('输入文件夹名称：{0}'.format(foldername1))
            handle.Kjlb_browseperspace_menu_addfolder_confirm_click()
            self.log.info('点击确定')
            # 4.检查文件夹是否成功新建
            foldername = handle.Kjlb_browseperspace_foldername_get()[0].text
            self.log.info('检查文件夹是否创建成功')
            assert foldername1 == foldername, "Error : Floder Name Is Wrong"
            # 5.+数据:相册-照片列表-完成
            # 5.1+数据
            handle.Kjlb_browseperspace_piclist_click(0)
            self.log.info('+数据')
            # 5.2相册方式
            handle.Kjlb_browseperspace_addData_ByAlbum_click()
            self.log.info('选择相册方式')
            # 5.3点击第一张照片
            handle.Kjlb_browseperspace_addData_ByAlbum_piclist_click(0)
            self.log.info('点击第一张照片')
            # 5.4完成
            handle.Kjlb_browseperspace_addData_ByAlbum_confirm_click()
            self.log.info('点击完成')
            sleep(1)
            # 5.5返回空间主页
            handle.Kjlb_browseperspace_addData_ByAlbum_confirm_back_click()
            self.log.info('点击返回空间主页')
            # 6.检查上传是否成功
            picLen = len(handle.Kjlb_browseperspace_piclist_get())  # 照片列表长度应该为2
            self.log.info('检查上传是否成功')
            assert picLen == 2, 'Error : Picture Upload Failed'
            # 7.返回
            handle.Kjlb_browseperspace_back_click()
            self.log.info('点击返回')
            self.log.info('------END:test2_1私人空间加文件夹.CreatePerSFolder.py------')
        except Exception as err:
            self.log.error("Error Information CreatePerSFolder Inside : %s" % err)
            raise err
