__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from StoneUIFramework.testcase.空间.私人空间.test2_1私人空间加文件夹 import *


# 关闭私人空间
class DeletePerSFloder:
    # 1.初始化
    def __init__(self):
        # 1.创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')
        # 2.获取截图路径、日志路径、日志名
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名
        # 3.创建日志模块
        self.log = Log(self.logfile)
        sleep(1)

    # 2.删除私人空间文件夹-公用方法
    def deletePerSFloder(self, driver, spacename):
        # 创建 _SPACEHANDLE5公有定位控件对象
        handle = SPACEHANDLE5(driver)
        try:
            self.log.info('------START:test2_1私人空间加文件夹.DeletePerSFolder.py------')
            # 1.点击该空间
            handle.Kjlb_browseorgspaceByName_click(spacename)
            self.log.info('点击{0}空间'.format(spacename))
            self.log.info('判断文件夹是否为空')
            if driver.find_element_by_id("com.yunlu6.stone:id/personzone_item_foldernum").text != "(0)":  # 判断文件夹是否为空
                # 2.菜单栏
                handle.Kjlb_browseperspace_menu_click()
                self.log.info('点击菜单栏')
                # 3.编辑
                handle.Kjlb_browseperspace_menu_edit_click()
                self.log.info('点击编辑')
                # 4.删除文件夹
                # 4.1删除文件夹(此时不为空)
                handle.Kjlb_browseperspace_more_menu_edit_deletefolder_click(0)
                self.log.info('点击删除文件夹')
                # 4.2照片列表
                handle.Kjlb_browseperspace_more_menu_edit_deletefolder_piclist_click(0)
                self.log.info('点击第一张照片')
                # 4.3删除
                handle.Kjlb_browseperspace_more_menu_edit_deletefolder_dbtn_click()
                self.log.info('点击删除')
                # 4.4是
                handle.Kjlb_browseperspace_more_menu_edit_deletefolder_dbtn_y_click()
                self.log.info('确认删除')
                # 4.5删除文件夹(为空)
                handle.Kjlb_browseperspace_more_menu_edit_deletefolder_click(0)
                self.log.info('删除文件夹-为空时')
                driver.find_element_by_id("com.yunlu6.stone:id/edit_folder_ok").click()
                self.log.info('确认删除文件夹')
            else:
                # 4.5.菜单栏
                handle.Kjlb_browseperspace_menu_click()
                self.log.info('点击菜单栏')
                # 4.6.编辑
                handle.Kjlb_browseperspace_menu_edit_click()
                self.log.info('点击编辑')
                # 4.7删除文件夹(为空)
                handle.Kjlb_browseperspace_more_menu_edit_deletefolder_click(0)
                self.log.info('删除文件夹-为空时')
                driver.find_element_by_id("com.yunlu6.stone:id/edit_folder_ok").click()
                self.log.info('确认删除文件将爱')
                # 5.返回空间列表
            handle.Kjlb_browseperspace_more_menu_edit_back_click()
            self.log.info('返回空间列表')
        except Exception as err:
            self.log.error("Error Information CloseSpace Inside : %s" % err)
            raise err
