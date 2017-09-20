__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from time import sleep
from StoneUIFramework.public.common.publicfunction import Tools
from StoneUIFramework.public.handle.space.SPACEHANDLE5 import _SPACEHANDLE5
from StoneUIFramework.public.common.datainfo import DataInfo
from StoneUIFramework.public.common.log import Log
from StoneUIFramework.config.globalparam import GlobalParam

#团队人事任免
class NewArchivies:
    def __init__(self):
        #初始化测试数据
        d = DataInfo("space.xls")#创建DataInfo()对象
        self.title = d.cell("test004-资讯",2,1)#测试空间123
        self.typelist = int(d.cell("test004-资讯",2,2))#类型列表:经典作品
        #创建读取配置信息对象
        cf = GlobalParam('config','path_file.conf')
        #获取截图路径、日志路径、日志名
        self.logfile = cf.getParam('log',"logfile")#日志文件名
        #创建日志模块
        self.log = Log(self.logfile)
    def newarchivies(self,driver):
        #创建工具类
        tools = Tools(driver)#tools工具
        #创建_SPACEHANDLE5公有定位控件对象
        handle = _SPACEHANDLE5(driver)
        sleep(1)
        try:
            self.log.info('------START:test4_1资讯.NewArchivies.py------')
        #1.空间首页
            # handle.Kjlb_click()
            # tools.getScreenShot(screen_path,"空间首页")
        #2.选择空间:测试空间123
            # handle.Kjlb_browseorgspaceByName_click("测试空间123")
        #3.右上角:菜单栏选择资讯
            handle.Kjlb_browseorgspace_menu_click()
            self.log.info('点击菜单栏')
            handle.Kjlb_browseorgspace_menu_archivies_click()
            self.log.info('点击资讯')
        #4.各入口跳转检查
            #4.1 入口一:图片新增按钮
            self.log.info('入口一：图片新增按钮检查')
            handle.Kjlb_browseorgspace_menu_archivies_picadd_click()
            self.log.info('点击新增图片按钮')
            handle.Kjlb_browseorgspace_menu_archivies_new_back_click()#返回
            self.log.info('点击返回')
            #4.2 入口二:右上角新增
            self.log.info('入口二：右上角新增检查')
            handle.Kjlb_browseorgspace_menu_archivies_new_click()
            self.log.info('点击右上角新增按钮')
        #5.添加资讯
            #5.1 添加照片
            handle.Kjlb_browseorgspace_menu_archivies_new_addphoto_click()
            self.log.info('点击+照片')
            handle.Kjlb_browseorgspace_menu_archivies_new_addphoto_album_click()#点击相册
            self.log.info('点击相册')
            handle.Kjlb_browseorgspace_menu_archivies_new_addphoto_album_list_click(0)#点击第一张照片
            self.log.info('点击第一张照片')
            handle.Kjlb_browseorgspace_menu_archivies_new_addphoto_album_confirm_click()#点击完成
            self.log.info('点击完成')
            sleep(1)
            #5.2 标题
            handle.Kjlb_browseorgspace_menu_archivies_new_title_sendkeys(self.title)#标题
            self.log.info('标题：%s'%self.title)
            #5.3 类型
            handle.Kjlb_browseorgspace_menu_archivies_new_type_click()#类型
            self.log.info('点击类型')
            handle.Kjlb_browseorgspace_menu_archivies_new_type_typelist_click(self.typelist)#经典作品
            self.log.info('选择经典作品')
            #5.4 勾选
            handle.Kjlb_browseorgspace_menu_archivies_new_confirm_click()#勾选
            self.log.info('勾选')
            handle.Kjlb_browseorgspace_menu_archivies_new_confirm_late_click()#保存
            self.log.info('保存')
            #5.5 点击资讯发布
            handle.Kjlb_browseorgspace_menu_archivies_pic_click(0)#点击第一张资讯
            self.log.info('点击第一张资讯')
            handle.Kjlb_browseorgspace_menu_archivies_pic_click(0)#点击第一张资讯
            self.log.info('点击第一张资讯')
            handle.Kjlb_browseorgspace_menu_archivies_pic_menu_click()#菜单栏
            self.log.info('点击菜单栏')
            handle.Kjlb_browseorgspace_menu_archivies_pic_menu_new_click()#发布
            self.log.info('点击发布')
            type = handle.Kjlb_browseorgspace_menu_archivies_pic_menu_new_type_text()#获取资讯类型
            assert type == "经典作品(1)","资讯类型保存错误"
            self.log.info('资讯类型检查')
            driver.implicitly_wait(1)#只能等待2秒
            # sleep(2)
            handle.Kjlb_browseorgspace_menu_archivies_pic_click(0)#点击第一张资讯
            driver.implicitly_wait(1)
            self.log.info('点击第一张资讯')
            handle.Kjlb_browseorgspace_menu_archivies_pic_click(0)#点击第一张资讯
            driver.implicitly_wait(1)
            self.log.info('点击第一张资讯')
            title = handle.Kjlb_browseorgspace_menu_archivies_pic_title_text()#获取资讯标题
            assert title == self.title,"资讯标题未保存成功"
            self.log.info('资讯标题检查')
            #5.6 返回到空间列表
            handle.Kjlb_browseorgspace_menu_archivies_pic_back_click()
            handle.Kjlb_browseorgspace_menu_archivies_back_click()
            handle.Kjlb_browseorgspace_menu_archivies_back_click()
            handle.Kjlb_browseorgspace_back_click()#返回空间
            self.log.info('返回空间')
        except Exception as err:
            self.log.error("NewArchivies Inside : %s"%err)
            raise err