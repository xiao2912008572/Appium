__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from time import sleep
import logging
from StoneUIFramework.public.common.publicfunction import Tools
from StoneUIFramework.public.handle.space.SPACEHANDLE5 import _SPACEHANDLE5
from StoneUIFramework.public.common.log import Log
from StoneUIFramework.config.globalparam import GlobalParam

#删除资讯
class DeleteArchivies:
    def __init__(self):#初始化测试数据
        #创建读取配置信息对象
        cf = GlobalParam('config','path_file.conf')
        #获取截图路径、日志路径、日志名
        self.logfile = cf.getParam('log',"logfile")#日志文件名
        #创建日志模块
        self.log = Log(self.logfile)
    def deletearchivies(self,driver,spacename):
        #创建工具类
        tools = Tools(driver)#tools工具
        #创建_SPACEHANDLE5公有定位控件对象
        handle = _SPACEHANDLE5(driver)
        sleep(1)
        try:
            self.log.info('------START:test4_1资讯.DeleteArchivies.py------')
        #1.空间首页
            handle.Kjlb_click()
            self.log.info('进入空间首页')
        #2.选择空间:测试空间123
            handle.Kjlb_browseorgspaceByName_click(spacename)
            self.log.info('进入空间：%s'%spacename)
        #3.右上角:菜单栏选择资讯
            handle.Kjlb_browseorgspace_menu_click()
            self.log.info('菜单栏选择资讯')
            handle.Kjlb_browseorgspace_menu_archivies_click()
            self.log.info('点击资讯')
        #4.判断是否有图片，有就进入删除
            #4.1判断-点击第1张图片-点击第1张图片
            if handle.Kjlb_browseorgspace_menu_archivies_pic_element() != []:
                self.log.info('判断是否有图片，有就进入删除')
                handle.Kjlb_browseorgspace_menu_archivies_pic_click(0)
                self.log.info('点击第一张图片')
                handle.Kjlb_browseorgspace_menu_archivies_pic_click(0)
                self.log.info('点击第一张图片')
            #4.2菜单栏
                handle.Kjlb_browseorgspace_menu_archivies_pic_menu_click()
                self.log.info('点击菜单栏')
            #4.3下架
                handle.Kjlb_browseorgspace_menu_archivies_pic_menu_offshelf_click()
                self.log.info('下架')
            #4.4点击第1张图片
                sleep(1)
                handle.Kjlb_browseorgspace_menu_archivies_pic_click(0)
                self.log.info('点击第一张图片')
                sleep(2)
                handle.Kjlb_browseorgspace_menu_archivies_pic_click(0)
                self.log.info('点击第一张图片')
            #4.4菜单栏
                handle.Kjlb_browseorgspace_menu_archivies_pic_menu_click()
                self.log.info('菜单栏')
            #4.5删除
                handle.Kjlb_browseorgspace_menu_archivies_pic_menu_delete_click()
                self.log.info('删除')
            #4.6返回-空间主界面
                handle.Kjlb_browseorgspace_menu_archivies_back_click()
                self.log.info('返回')
        #5.删除检查
                handle.Kjlb_browseorgspaceByName_click(spacename)
                self.log.info('进入空间：%s'%spacename)
            #5.1菜单栏
                handle.Kjlb_browseorgspace_menu_click()
                self.log.info('点击菜单栏')
            #5.1资讯
                handle.Kjlb_browseorgspace_menu_archivies_click()
                self.log.info('点击资讯')
            #5.3判断
                self.log.info('判断是否为空，为空即是已删除')
                assert [] == handle.Kjlb_browseorgspace_menu_archivies_pic_element(),'Error Pic Delete Failed!'
                self.log.info('------END:test4_1资讯.DeleteArchivies.py------')
        except Exception as err:
            self.log.error("DeleteArchivies Inside : %s"%err)
            raise err