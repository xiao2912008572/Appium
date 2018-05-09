__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import sys
sys.path.append("/Users/xiaojingyuan/PycharmProjects/Appium")
from YunluFramework.testcase.空间.机构空间.test5_1编辑 import *


# 编辑
@ddt.ddt
class space_BusinessCardO(unittest.TestCase):
    # 1.创建数据库操作对象
    d = DataMysql()
    sql01 = "select * from test_5_1_orgbusinesscard_01"
    sql03 = "select * from test_5_1_orgbusinesscard_03"
    data01 = d.select(sql01, 0)
    data03 = d.select(sql03, 0)

    # 2.初始化
    @classmethod
    def setUpClass(self):
        # 1.建立连接信息
        cnn = Connect()
        self.driver = cnn.connect()

        # 2.创建工具类
        self.tools = Tools(self.driver)  # tools工具

        # 3.创建_SPACEHANDLE5公有定位控件对象
        self.handle = SPACEHANDLE5(self.driver)

        # 4.创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')

        # 5.获取截图路径、日志路径、日志名
        self.screen_path = cf.getParam('space', "org_path_005_1")  # 通过配置文件获取截图的路径

        self.logfile = cf.getParam('log', "logfile")  # 日志文件名
        # 6.创建日志记录模块
        self.log = Log(self.logfile)

        # 7.创建Space操作对象
        self.common = CommonSpace(self.handle, self.log, self.tools)

        # 8.打印日志
        self.log.info('****************************************用例开始！****************************************')
        self.log.info('------------START:test5_1编辑.BusinessCard005_1.py------------')

    # 3.释放资源
    @classmethod
    def tearDownClass(self):
        # 1.打印日志
        self.log.info("------------END::test5_1编辑.BusinessCard005_1.py------------")  # 宣布成功
        self.log.info('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~用例结束！~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

        # 2.关闭driver
        # self.driver.quit()

    # 4.测试用例
    # 4.1进入空间
    @ddt.data(data01)
    @ddt.unpack
    def test_businesscard01(self, spacename):
        '''进入空间
        :param spacename:空间名
        '''
        try:
            # 1.进入空间
            self.common.enter_space(spacename)

        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_businesscard01 : %s" % err)
            raise err

    # 4.2 进入编辑
    def test_businesscard02(self):
        '''进入编辑
        :return:
        '''
        try:
            # 1.进入编辑
            self.common.click_org_menu('edit')

        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_businesscard02 : %s" % err)
            raise err

    # 4.3 编辑名片
    @ddt.data(data03)
    @ddt.unpack
    def test_businesscard03(self, contact, phone, tel, email, QQ, website):
        '''编辑名片
        :param contact: 联系人
        :param phone: 手机号
        :param tel: 座机号
        :param email: 邮箱
        :param QQ: QQ
        :param website: 网站
        '''
        try:
            # 1.联系人
            if self.handle.Kjlb_browseorgspace_menu_edit_contact_text() is not None:
                self.handle.Kjlb_browseorgspace_menu_edit_contact_clear()
            self.handle.Kjlb_browseorgspace_menu_edit_contact_sendkeys(contact)
            self.log.info('输入联系人：%s' % contact)

            # 2.手机号
            if self.handle.Kjlb_browseorgspace_menu_edit_phone_text() is not None:
                self.handle.Kjlb_browseorgspace_menu_edit_phone_clear()
            self.handle.Kjlb_browseorgspace_menu_edit_phone_sendkeys(phone)
            self.log.info('输入手机号：%s' % phone)

            # 3.座机号
            if self.handle.Kjlb_browseorgspace_menu_edit_landline_text() is not None:
                self.handle.Kjlb_browseorgspace_menu_edit_landline_clear()
            self.handle.Kjlb_browseorgspace_menu_edit_landline_sendkeys(tel)
            self.log.info('输入座机号：%s' % tel)

            # 4.邮箱
            if self.handle.Kjlb_browseorgspace_menu_edit_email_text() is not None:
                self.handle.Kjlb_browseorgspace_menu_edit_email_clear()
            self.handle.Kjlb_browseorgspace_menu_edit_email_sendkeys(email)
            self.log.info('输入邮箱：%s' % email)

            # 5.QQ
            if self.handle.Kjlb_browseorgspace_menu_edit_QQ_text() is not None:
                self.handle.Kjlb_browseorgspace_menu_edit_QQ_clear()
            self.handle.Kjlb_browseorgspace_menu_edit_QQ_sendkeys(QQ)
            self.log.info('输入QQ号：%s' % QQ)

            # 6.网址
            if self.handle.Kjlb_browseorgspace_menu_edit_website_text() is not None:
                self.handle.Kjlb_browseorgspace_menu_edit_website_clear()
            self.handle.Kjlb_browseorgspace_menu_edit_website_sendkeys(website)
            self.log.info('输入网址：%s' % website)

            # 7.勾选
            self.handle.Kjlb_browseorgspace_menu_edit_confirm_click()  # 勾选
            self.log.info('勾选保存')
            sleep(1)

        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_businesscard03 : %s" % err)
            raise err

    # 4.4 检查编辑后图标数量
    def test_businesscard04(self):
        '''检查编辑后图标数量
        :return:
        '''
        try:
            # 1.检查联系方式是否保存
            sleep(1)
            self.log.info('检查联系方式是否保存成功：')
            self.log.info('当前需要保存联系方式数量：5')
            camount_now = len(self.driver.find_elements_by_id('com.yunlu6.yunlu:id/contact_icon'))
            self.log.info('实际写入保存联系方式数量：{0}'.format(camount_now))
            assert camount_now == 5, "部分联系方式未保存成功"
            self.log.info('联系方式保存成功!')

        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_businesscard04 : %s" % err)
            raise err

    # 4.5 检查数据
    @ddt.data(data03)
    @ddt.unpack
    def test_businesscard05(self, contact, phone, tel, email, QQ, website):
        '''检查数据
        :param contact: 联系人
        :param phone: 手机号
        :param tel: 座机号
        :param email: 邮箱
        :param QQ: QQ
        :param website: 网站
        '''
        try:
            # 0.进入编辑
            self.common.click_org_menu('edit')  # 点击编辑

            # 1.联系人
            self.log.info('检查联系人：')
            contact_now = self.handle.Kjlb_browseorgspace_menu_edit_contact_text()
            self.log.info('当前联系人为：{0}'.format(contact_now))
            self.log.info('预期联系人为：{0}'.format(contact))
            assert contact_now == contact, "Contact:Save Failed"
            self.log.info('联系人与预期一致')

            # 2.手机号
            self.log.info('检查手机号:')
            phone_now = self.handle.Kjlb_browseorgspace_menu_edit_phone_text()
            self.log.info('当前手机号为：{0}'.format(phone_now))
            self.log.info('预期手机号为：{0}'.format(phone))
            assert int(phone_now) == phone, "Phone:Save Failed"
            self.log.info('手机号与预期一致')

            # 3.座机号
            self.log.info('检查座机号：')
            tel_now = self.handle.Kjlb_browseorgspace_menu_edit_landline_text()
            self.log.info('当前座机号为：{0}'.format(tel_now))
            self.log.info('预期座机号为：{0}'.format(tel))
            assert int(tel_now) == tel, "Tel:Save Failed"
            self.log.info('座机号与预期一致')

            # 4.邮箱
            self.log.info('检查邮箱：')
            email_now = self.handle.Kjlb_browseorgspace_menu_edit_email_text()
            self.log.info('当前邮箱为：{0}'.format(email_now))
            self.log.info('预期邮箱为：{0}'.format(email))
            assert email_now == email, "Email:Save Failed"
            self.log.info('邮箱与预期一致')

            # 5.QQ
            self.log.info('检查QQ号：')
            QQ_now = self.handle.Kjlb_browseorgspace_menu_edit_QQ_text()
            self.log.info('当前QQ号为：{0}'.format(QQ_now))
            self.log.info('预期QQ号为：{0}'.format(QQ))
            assert int(QQ_now) == QQ, "QQ:Save Failed"
            self.log.info('QQ与预期一致')

            # 6.网址
            self.log.info('检查网址：')
            website_now = self.handle.Kjlb_browseorgspace_menu_edit_website_text()
            self.log.info('当前网址为：{0}'.format(website_now))
            self.log.info('预期网址为：{0}'.format(website))
            assert self.handle.Kjlb_browseorgspace_menu_edit_website_text() == website, "Website:Save Failed"
            self.log.info('网址与预期一致')

        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_businesscard05 : %s" % err)
            raise err

    # 4.6 清空数据
    def test_businesscard06(self):
        '''清空数据
        :return:
        '''
        try:
            # 1.清空联系人
            self.handle.Kjlb_browseorgspace_menu_edit_contact_clear()
            self.log.info('清空联系人')

            # 2.清空手机号
            self.handle.Kjlb_browseorgspace_menu_edit_phone_clear()
            self.log.info('清空手机号')

            # 3.清空座机号
            self.handle.Kjlb_browseorgspace_menu_edit_landline_clear()
            self.log.info('清空座机号')

            # 4.清空邮箱
            self.handle.Kjlb_browseorgspace_menu_edit_email_clear()
            self.log.info('清空邮箱')

            # 5.清空QQ
            self.handle.Kjlb_browseorgspace_menu_edit_QQ_clear()
            self.log.info('清空QQ号')

            # 6.清空网址
            self.handle.Kjlb_browseorgspace_menu_edit_website_clear()
            self.log.info('清空网址')

            # 7.勾选保存
            self.handle.Kjlb_browseorgspace_menu_edit_confirm_click()
            self.log.info('勾选保存')

        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_businesscard06 : %s" % err)
            raise err

if __name__ == '__main__':
    unittest.main()