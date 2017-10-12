__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from time import sleep
from StoneUIFramework.public.common.publicfunction import Tools
from StoneUIFramework.public.handle.space.SPACEHANDLE5 import _SPACEHANDLE5
from StoneUIFramework.public.common.datainfo import DataInfo
from StoneUIFramework.public.common.log import Log
from StoneUIFramework.config.globalparam import GlobalParam


# 企业名片编辑
class Edit:
    # 1.初始化
    def __init__(self):
        # 1.创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')
        # 2.获取截图路径、日志路径、日志名
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名
        # 3.创建日志模块
        self.log = Log(self.logfile)

    # 2.编辑协会名片-公用方法
    def edit(self, driver, contact, phone, tel, email, QQ, website):
        # 创建工具类
        tools = Tools(driver)  # tools工具
        # 创建 _SPACEHANDLE5公有定位控件对象
        handle = _SPACEHANDLE5(driver)
        sleep(2)
        try:
            self.log.info('------START:test1_1创建协会空间.CreateAscSpace.py------')
            # 1.空间首页
            # handle.Kjlb_click()
            # tools.getScreenShot(screen_path,"空间首页")
            # 2.选择空间:协会测试123
            # handle.Kjlb_browseorgspaceByName_click("测试空间123")
            # 3.右上角:菜单栏
            handle.Kjlb_browseascspace_menu_click()  # 点击菜单栏
            self.log.info('点击菜单栏')
            # 4.右上角菜单栏-编辑
            handle.Kjlb_browseascspace_menu_edit_click()
            self.log.info('点击右上角菜单栏-编辑')
            # 5.编辑企业名片详情
            # 5.1 联系人
            if handle.Kjlb_browseascspace_menu_edit_contact_text() is not None:
                handle.Kjlb_browseascspace_menu_edit_contact_clear()
            handle.Kjlb_browseascspace_menu_edit_contact_sendkeys(contact)
            self.log.info('输入联系人：%s' % contact)
            # 5.2 手机号
            if handle.Kjlb_browseascspace_menu_edit_phone_text() is not None:
                handle.Kjlb_browseascspace_menu_edit_phone_clear()
            handle.Kjlb_browseascspace_menu_edit_phone_sendkeys(phone)
            self.log.info('输入手机号：%s' % phone)
            # 5.3 座机号
            if handle.Kjlb_browseascspace_menu_edit_landline_text() is not None:
                handle.Kjlb_browseascspace_menu_edit_landline_clear()
            handle.Kjlb_browseascspace_menu_edit_landline_sendkeys(tel)
            self.log.info('输入座机号：%s' % tel)
            # 5.4 邮箱
            if handle.Kjlb_browseascspace_menu_edit_email_text() is not None:
                handle.Kjlb_browseascspace_menu_edit_email_clear()
            handle.Kjlb_browseascspace_menu_edit_email_sendkeys(email)
            self.log.info('输入邮箱：%s' % email)
            # 5.5 QQ
            if handle.Kjlb_browseascspace_menu_edit_QQ_text() is not None:
                handle.Kjlb_browseascspace_menu_edit_QQ_clear()
            handle.Kjlb_browseascspace_menu_edit_QQ_sendkeys(QQ)
            self.log.info('输入QQ号：%s' % QQ)
            # 5.6 网址
            if handle.Kjlb_browseascspace_menu_edit_website_text() is not None:
                handle.Kjlb_browseascspace_menu_edit_website_clear()
            handle.Kjlb_browseascspace_menu_edit_website_sendkeys(website)
            self.log.info('输入网址：%s' % website)
            # 6.勾选+点击检查
            handle.Kjlb_browseorgspace_menu_bcard_menu_edit_confirm_click()  # 勾选
            self.log.info('勾选保存')
            sleep(1)
            assert len(handle.Kjlb_browseorgspace_menu_bcard_contactlist_element()) == 5, "部分联系方式未保存成功"
            self.log.info('联系方式是否保存成功检查')
            '''
            #6.1 手机号
            handle.Kjlb_browseorgspace_menu_bcard_contactlist_click(0)
            sleep(1)
            driver.keyevent('4')
            sleep(3)
            #6.2 座机号
            handle.Kjlb_browseorgspace_menu_bcard_contactlist_click(1)
            sleep(1)
            driver.keyevent('4')
            sleep(2)
            #6.3 QQ
            handle.Kjlb_browseorgspace_menu_bcard_contactlist_click(2)
            sleep(2)
            driver.keyevent('4')
            sleep(2)
            #6.4 邮箱
            handle.Kjlb_browseorgspace_menu_bcard_contactlist_click(3)
            sleep(1)
            driver.keyevent('4')
            sleep(2)
            driver.find_element_by_id("android:id/button2").click()#点击放弃,三星手机自带邮箱
            #6.5 网址
            handle.Kjlb_browseorgspace_menu_bcard_contactlist_click(4)
            driver.keyevent('4')
            sleep(2)
            driver.keyevent('4')
            sleep(2)
            '''
            # 7.检查数据
            handle.Kjlb_browseascspace_menu_click()  # 菜单栏
            self.log.info('点击菜单栏')
            handle.Kjlb_browseascspace_menu_edit_click()  # 编辑
            self.log.info('点击编辑')
            # 7.1 联系人
            assert handle.Kjlb_browseascspace_menu_edit_contact_text() == contact, "Contact:Save Failed"
            self.log.info('检查联系人')
            # 7.2 手机号
            assert int(handle.Kjlb_browseascspace_menu_edit_phone_text()) == phone, "Phone:Save Failed"
            self.log.info('检查手机号')
            # 7.3 座机号
            assert int(handle.Kjlb_browseascspace_menu_edit_landline_text()) == tel, "Tel:Save Failed"
            self.log.info('检查座机号')
            # 7.4 邮箱
            assert handle.Kjlb_browseascspace_menu_edit_email_text() == email, "Email:Save Failed"
            self.log.info('检查邮箱')
            # 7.5 QQ
            assert int(handle.Kjlb_browseascspace_menu_edit_QQ_text()) == QQ, "QQ:Save Failed"
            self.log.info('检查QQ号')
            # 7.6 网址
            assert handle.Kjlb_browseascspace_menu_edit_website_text() == website, "Website:Save Failed"
            self.log.info('检查网址')
            # 8.清空名片数据
            # 8.1 清空联系人
            handle.Kjlb_browseascspace_menu_edit_contact_clear()
            self.log.info('清空联系人')
            # 8.2 清空手机号
            handle.Kjlb_browseascspace_menu_edit_phone_clear()
            self.log.info('清空手机号')
            # 8.3 清空座机号
            handle.Kjlb_browseascspace_menu_edit_landline_clear()
            self.log.info('清空座机号')
            # 8.4 清空邮箱
            handle.Kjlb_browseascspace_menu_edit_email_clear()
            self.log.info('清空邮箱')
            # 8.5 清空QQ
            handle.Kjlb_browseascspace_menu_edit_QQ_clear()
            self.log.info('清空QQ号')
            # 8.6 清空网址
            handle.Kjlb_browseascspace_menu_edit_website_clear()
            self.log.info('清空网址')
            # 8.7 勾选保存
            handle.Kjlb_browseascspace_menu_edit_confirm_click()
            self.log.info('勾选保存')
            self.log.info('------END:test2_1协会编辑.Edit.py------')
        except Exception as err:
            self.log.error("Edit Inside : %s" % err)
            raise err
