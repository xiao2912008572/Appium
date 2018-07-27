__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from YunluFramework.testcase.空间.协会空间.test1_1创建协会空间 import *


# 创建机构空间
@ddt.ddt
class ascspace_CreateA(unittest.TestCase):
    # 1.创建数据库操作对象
    d = DataMysql()
    sql02 = "select * from test1_1_asccreatespace_02"
    sql03 = "select * from test1_1_asccreatespace_03"
    sql04 = "select * from test1_1_asccreatespace_04"
    data02 = d.select(sql02, 0)
    data03 = d.select(sql03, 0)
    data04 = d.select(sql04, 0)

    # 2.初始化
    @classmethod
    def setUpClass(self):
        # 1.建立连接信息
        cnn = Connect()
        self.driver = cnn.connect()

        # 2.创建工具类
        self.tools = Tools(self.driver)  # tools工具

        # 3.创建_BrowseOrgSpace公有定位控件对象
        self.handle = SPACEHANDLE5(self.driver)

        # 4.创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')

        # 5.获取截图路径、日志路径、日志名
        self.screen_path = cf.getParam('space', "ass_path_001_1")  # 通过配置文件获取截图的路径
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名

        # 6.创建日志记录模块
        self.log = Log(self.logfile)

        # 7.创建CommonSpace对象
        self.common = CommonSpace(self.handle, self.log, self.tools)
        sleep(1)

        # 8.打印日志
        self.log.info('****************************************用例开始！****************************************')
        self.log.info("------------START:test1_1创建协会空间.CreateASCSpace001_1.py------------")

    # 3.释放资源
    @classmethod
    def tearDownClass(self):
        # 1.打印日志
        self.log.info("------------END:test1_1创建机构空间.CreateASCSpace001_1.py------------")
        self.log.info('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~用例结束！~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

        # 2.关闭driver
        # self.driver.quit()

    # 4.测试用例
    # 4.0判断企业是否重复
    @ddt.data(data04)
    @ddt.unpack
    def test_asccreateSpace00(self, spacename):
        '''判断企业是否重复
        :param spacename: 空间名
        :return:
        '''
        try:
            self.common.enter_space(spacename) #进入空间
            self.common.click_asc_menu('close')  # 点击关闭
            self.handle.Kjlb_browseorgspace_menu_close_confirm_click()  # 确认关闭
            self.log.info('点击确认关闭')

        except:
            pass

    # 4.1进入空间列表
    def test_asccreateSpace01(self):
        '''进入空间首页
        :return:
        '''
        try:
            sleep(1)
            # 1.空间首页
            self.handle.Kjlb_click()
            self.log.info('点击空间首页')

            # 2.右上角主菜单
            self.handle.Kjlb_mainmenu_click()
            self.log.info('点击右上角主菜单')

            # 3.+机构空间
            self.handle.Kjlb_mainmenu_newspace_click()
            self.log.info('点击+机构空间')

        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_asccreateSpace01 : %s" % err)
            raise err

    # 4.2新建协会空间
    @ddt.data(data02)
    @ddt.unpack
    def test_asccreateSpace02(self, fullname, easyname, province, city, customertype):
        '''新建协会空间
        :param fullname: 机构名称
        :param easyname: 机构简称
        :param province: 省
        :param city: 市
        :param customertype: 客户类型
        :return:
        '''
        try:
            self.handle.Kjlb_mainmenu_newspace_orgname_sendkeys(fullname)  # 全称
            self.log.info('输入协会名称：{0}'.format(fullname))
            self.handle.Kjlb_mainmenu_newspace_orgintro_sendkeys(easyname)  # 简称
            self.log.info('输入协会简称：{0}'.format(easyname))
            self.handle.Kjlb_mainmenu_newspace_orgtitle_click()  # 点击标题
            self.log.info('点击标题')


            '''
            self.handle.Kjlb_mainmenu_newspace_orgtype_click()  # 机构类型
            self.log.info('点击机构类型')
            self.handle.Kjlb_mainmenu_newspace_orgtype_association_click()  # 机构类型：协会
            self.log.info('选择机构类型：协会')
            '''

            sleep(1)
            self.handle.Kjlb_mainmenu_newspace_customertype_click()  # 客户类型
            self.log.info('点击客户类型')
            self.handle.Kjlb_mainmenu_newspace_customertype_tag_click(customertype)  # 客户类型标签
            self.log.info('点击客户类型标签')
            self.handle.Kjlb_mainmenu_newspace_customertype_confirm_click()  # 点击确定
            self.log.info('点击确定按钮')
            self.handle.Kjlb_mainmenu_newspace_area_click()  # 所在地区
            self.log.info('点击所在地区')
            self.driver.find_element_by_name(province).click()
            self.log.info('选择%s省' % province)
            self.driver.find_element_by_name(city).click()
            self.log.info('选择%s市' % city)
            self.handle.Kjlb_mainmenu_newspace_affirm_click()  # 点击提交
            self.log.info('确定提交')

        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_asccreateSpace02 : %s" % err)
            raise err

    # 4.3 验证对公账号信息
    @ddt.data(data03)
    @ddt.unpack
    def test_asccreateSpace03(self, province, city, soverbanknub):
        '''验证对公账号信息
        :param province: 省
        :param city: 市
        :param soverbanknub:银行账号
        :return:
        '''
        try:
            self.handle.Kjlb_mainmenu_newspace_verifynow_click()  # 点击去验证
            self.log.info('点击去验证对公账号')
            # 开户银行:AAA
            # 所在地区:北京-东城
            # 支行:BBB
            # 银行账号:123456
            self.handle.Kjlb_mainmenu_newspace_verifynow_soverbank_click()  # 开户银行
            self.log.info('点击开户银行')
            self.handle.Kjlb_mainmenu_newspace_verifynow_soverbank_list1_click(0)
            self.log.info('点击开户银行列表1中第1家银行')
            self.handle.Kjlb_mainmenu_newspace_verifynow_soverbank_list1_click(0)
            self.log.info('点击开户银行列表2中第1家银行')
            self.handle.Kjlb_mainmenu_newspace_verifynow_soveraddress_click()  # 所在地区
            self.log.info('点击所在地区')
            self.driver.find_element_by_name(province).click()  # 北京
            self.log.info('选择%s省' % province)
            self.driver.find_element_by_name(city).click()  # 东城
            self.log.info('选择%s市' % city)
            # handle.Kjlb_mainmenu_newspace_verifynow_sovermybank_sendkeys(sovermybank)  # 支行
            # self.log.info('填写支行：%s' % sovermybank)
            self.handle.Kjlb_mainmenu_newspace_verifynow_soverbanknub_sendkeys(soverbanknub)  # 银行账户
            self.log.info('填写银行账户：%s' % soverbanknub)
            self.handle.Kjlb_mainmenu_newspace_verifynow_soversave_click()  # 确定提交
            self.log.info('确定提交')
            sleep(1)
            self.handle.Kjlb_mainmenu_newspace_verifynow_soversave_back_click()  # 点击返回
            self.log.info('点击返回')
            sleep(1)

        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_asccreateSpace03 : %s" % err)
            raise err

    # 4.4 关闭空间
    @ddt.data(data04)
    @ddt.unpack
    def test_asccreateSpace04(self, spacename):
        '''关闭空间
        :param driver:
        :param spacename: 简称名
        :return:
        '''
        try:
            self.log.info("------START:test1_1创建机构空间.CloseSpace.py-----")
            # -----------------关闭空间 - ----------------
            # 为了保证不中途退出，需要第一次进入的时候检查是否存在该机构，如果存在，先关闭
            self.common.enter_space(spacename)  # 进入空间
            sleep(1)
            self.common.click_asc_menu('close')  # 点击关闭
            self.handle.Kjlb_browseorgspace_menu_close_confirm_click()  # 确认关闭
            self.log.info('点击确认关闭')

        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_createSpace04 : %s" % err)
            raise err
