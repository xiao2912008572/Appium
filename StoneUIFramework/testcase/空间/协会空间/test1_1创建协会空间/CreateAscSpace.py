__author__ = 'Administrator'
# -*- coding: utf-8 -*-

from StoneUIFramework.testcase.空间.协会空间.test1_1创建协会空间 import *


# 创建机构空间
class CreateAscSpace:
    # 1.初始化
    def __init__(self):
        # 1.创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')
        # 2.获取截图路径、日志路径、日志名
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名
        # 3.创建日志模块
        self.log = Log(self.logfile)

    # 2.创建协会空间-公用方法
    def createAscSpace(self, driver, fullname, easyname,
                       province, city, soverbank, sovermybank,
                       soverbanknub, customertype, industry):
        # 创建_SPACEHANDLE5公有定位控件对象
        handle = SPACEHANDLE5(driver)
        sleep(1)
        try:
            self.log.info('------START:test1_1创建协会空间.CreateAscSpace.py------')
            # 1.空间首页
            handle.Kjlb_click()
            self.log.info('点击空间首页')
            # 2.右上角主菜单
            handle.Kjlb_mainmenu_click()
            self.log.info('点击右上角主菜单')
            # 3.+机构空间
            handle.Kjlb_mainmenu_newspace_click()
            self.log.info('点击+机构空间')
            # --------------------------新机构空间会空间-------------------------
            # 机构名称:(fullname):appium测试协会
            # 机构简称:(easyname):appium测试协会
            # 机构类型:企业
            # 产业角色:工厂
            # 客户类型:石材
            # 所在地区:北京-东城
            # 详细地址:不填
            handle.Kjlb_mainmenu_newspace_orgname_sendkeys(fullname)  # 全称
            self.log.info('输入协会名称：{0}'.format(fullname))
            handle.Kjlb_mainmenu_newspace_orgintro_sendkeys(easyname)  # 简称
            self.log.info('输入协会简称：{0}'.format(easyname))
            handle.Kjlb_mainmenu_newspace_orgtitle_click()  # 点击标题
            self.log.info('点击标题')
            handle.Kjlb_mainmenu_newspace_orgtype_click()  # 机构类型
            self.log.info('点击机构类型')
            handle.Kjlb_mainmenu_newspace_orgtype_association_click()  # 机构类型：协会
            self.log.info('选择机构类型：协会')
            sleep(1)
            handle.Kjlb_mainmenu_newspace_customertype_click()  # 客户类型
            self.log.info('点击客户类型')
            handle.Kjlb_mainmenu_newspace_customertype_tag_click(customertype)  # 客户类型标签
            self.log.info('点击客户类型标签')
            handle.Kjlb_mainmenu_newspace_customertype_confirm_click()  # 点击确定
            self.log.info('点击确定按钮')
            handle.Kjlb_mainmenu_newspace_area_click()  # 所在地区
            self.log.info('点击所在地区')
            driver.find_element_by_name(province).click()
            self.log.info('选择%s省' % province)
            driver.find_element_by_name(city).click()
            self.log.info('选择%s市' % city)
            handle.Kjlb_mainmenu_newspace_affirm_click()  # 点击提交
            self.log.info('确定提交')

            # ------------------------验证对公账号-------------------------------
            handle.Kjlb_mainmenu_newspace_verifynow_click()  # 点击去验证
            self.log.info('点击去验证对公账号')
            # 开户银行:AAA
            # 所在地区:北京-东城
            # 支行:BBB
            # 银行账号:123456
            handle.Kjlb_mainmenu_newspace_verifynow_soverbank_sendkeys(soverbank)  # 开户银行
            self.log.info('填写开户银行：%s' % soverbank)
            handle.Kjlb_mainmenu_newspace_verifynow_soveraddress_click()  # 所在地区
            self.log.info('点击所在地区')
            driver.find_element_by_name(province).click()  # 北京
            self.log.info('选择%s省' % province)
            driver.find_element_by_name(city).click()  # 东城
            self.log.info('选择%s市' % city)
            handle.Kjlb_mainmenu_newspace_verifynow_sovermybank_sendkeys(sovermybank)  # 支行
            self.log.info('填写支行：%s' % sovermybank)
            handle.Kjlb_mainmenu_newspace_verifynow_soverbanknub_sendkeys(soverbanknub)  # 银行账户
            self.log.info('填写银行账户：%s' % soverbanknub)
            handle.Kjlb_mainmenu_newspace_verifynow_soversave_click()  # 确定提交
            self.log.info('确定提交')
            sleep(1)
            handle.Kjlb_mainmenu_newspace_verifynow_soversave_back_click()  # 点击返回
            self.log.info('点击返回')
            sleep(1)
            self.log.info('------END:test1_1创建协会空间.CreateAscSpace.py------')
        except Exception as err:
            self.log.error("CreateAscSpace Inside : %s" % err)
            raise err
