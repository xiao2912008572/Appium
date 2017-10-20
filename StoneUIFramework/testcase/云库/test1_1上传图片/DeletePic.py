__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from StoneUIFramework.testcase.云库.test1_1上传图片 import *


# 删除图片
class DeletePic:
    # 1.初始化
    def __init__(self):
        # 1.创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')
        # 2.获取截图路径、日志路径、日志名
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名
        # 3.创建日志模块
        self.log = Log(self.logfile)
        sleep(1)

    # 2.删除图片-公用方法
    def deletePic(self, driver, picno):
        # 创建_YUNKUHANDLE3公有定位控件对象
        handle = YUNKUHANDLE3(driver)
        try:
            self.log.info('------START:test1_1删除图片.DeletePic.py------')
            # 1.点击云库首页
            handle.Yk_click()
            self.log.info('点击云库首页')
            # 2.点击第1张照片
            handle.Yk_piclist_click(picno)
            self.log.info('选择第{0}张照片'.format(picno + 1))
            # 3.菜单栏
            handle.Yk_piclist_menu_click()
            self.log.info('点击菜单栏')
            # 4.点击编辑
            handle.Yk_piclist_menu_edit_click()
            self.log.info('点击编辑')
            # 5.删除-是
            handle.Yk_piclist_menu_edit_delete_click()
            self.log.info('点击删除')
            handle.Yk_piclist_menu_edit_delete_yes_click()
            self.log.info('确定删除')
            self.log.info('------END:test1_1删除图片.DeletePic.py------')
        except Exception as err:
            self.log.error("DeletePic Inside : %s" % err)
            raise err
