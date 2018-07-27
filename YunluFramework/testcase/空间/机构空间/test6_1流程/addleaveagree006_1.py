__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from YunluFramework.testcase.空间.机构空间.test6_1流程 import *
import time


# 编辑
@ddt.ddt
class Add_leave_Agree(unittest.TestCase):
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
        # self.screen_path = cf.getParam('space', "org_path_006_1")  # 通过配置文件获取截图的路径

        self.logfile = cf.getParam('log', "logfile")  # 日志文件名
        # 6.创建日志记录模块
        self.log = Log(self.logfile)

        # 7.创建Space操作对象
        self.common = CommonSpace(self.handle, self.log, self.tools)

        # 8.打印日志
        self.log.info('****************************************用例开始！****************************************')
        self.log.info('------------START:test6_1流程.Addleaveprocess006_1.py------------')

    # 3.释放资源
    @classmethod
    def tearDownClass(self):
        # 1.打印日志
        self.log.info("------------END::test6_1流程.Addleaveprocess006_1.py------------")  # 宣布成功
        self.log.info('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~用例结束！~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

        # 2.关闭driver
        # self.driver.quit()

    # 4.测试用例
    # 4.1进入空间
    @ddt.data(data01)
    @ddt.unpack
    def test_process01(self, spacename):
        '''进入空间
        :param spacename:空间名
        '''
        try:
            # 1.进入空间
            self.common.enter_space(spacename)

        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_process01 : %s" % err)
            raise err

    # 4.2进入流程
    def test_process02(self):
        '''进入流程
        :return:
        '''
        try:
            # 1.进入流程
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='流程']").click()  # 后面需要封装一个通用类，将所有的菜单项集合
            # self.handle.Kjlb_browseorgspace_menu_flow_click("[@text='流程']")  # 点击流程
            self.log.info('点击流程')

        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_process02 : %s" % err)
            raise err

    # 4.3新建请假审批
    def test_process03(self):
        '''新建请假审批
        :return:
        '''
        try:
            # 1.点击菜单栏
            self.handle.Kjlb_browseorgspace_menu_flow_menu_click()
            self.log.info("点击菜单栏")

            # 2.点击新申请
            self.handle.Kjlb_browseorgspace_menu_flow_menu_new_click()
            self.log.info("点击新申请")

            # 3.点击请假
            self.handle.Kjlb_browseorgspace_menu_flow_menu_new_leave_click()
            self.log.info("点击请假")

            # 4.选择开始时间
            self.handle.Kjlb_browseorgspace_menu_flow_menu_new_leave_start_click()
            self.log.info("点击开始时间")

            # 5.点击确定
            self.handle.Kjlb_browseorgspace_menu_flow_menu_new_leave_start_sure_click()
            self.log.info("点击确定")

            # 5.选择结束时间
            self.handle.Kjlb_browseorgspace_menu_flow_menu_new_leave_end_click()
            self.log.info("选择结束时间")

            # 6.滑动年份
            time.sleep(1)
            self.tools.swipeUps(170, 1512, 500)
            self.log.info("添加一年")

            # 7.点击确定
            self.handle.Kjlb_browseorgspace_menu_flow_menu_new_leave_start_sure_click()
            self.log.info("点击确定")

            # 8.检查天数，增加1年，应为365
            year = int(self.handle.Kjlb_browseorgspace_menu_flow_menu_new_leave_day_text())
            years = 365
            assert years == year, "年份统计有误"
            self.log.info('年份统计无误')

            # 9.输入请假内容
            self.handle.Kjlb_browseorgspace_menu_flow_menu_new_leave_et_sendkey('请假')
            self.log.info("输入请假内容")  # 后面以数据库形式，存入文本

            # 10.点击附件
            self.handle.Kjlb_browseorgspace_menu_flow_menu_new_leave_photo_click()
            self.log.info("点击附件")

            # 11.选择照片
            self.handle.Kjlb_browseorgspace_menu_flow_menu_new_leave_start_alumm_click()
            self.log.info("选择相册添加")
            self.handle.Kjlb_browseorgspace_menu_product_new_addphoto_album_list_click(0)  # 选择第一张照片
            self.log.info('选择第%s张照片' % 1)  # 后面新建了数据库，以数据库数值代替
            self.handle.Kjlb_browseorgspace_menu_product_new_addphoto_album_confirm_click()  # 点击完成
            self.log.info('点击完成')
            sleep(4)

            # 12.选择审批人
            self.handle.Kjlb_browseorgspace_menu_flow_menu_new_leave_approver_click()
            self.log.info("点击审批人")
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='管理员']").click()
            self.log.info("选择管理员")  # 后面利用xpath，用数据库给一个职位身份来选择具体的人
            time.sleep(1)
            self.tools.swipeUp(1000)
            self.log.info("向上滑动0.5秒")
            self.handle.Kjlb_browseorgspace_menu_flow_menu_new_leave_ccpeople_click()
            self.log.info("点击抄送人")
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='管理员']").click()
            self.log.info("选择管理员")
            self.handle.Kjlb_browseorgspace_menu_flow_menu_new_leave_approver_submit_click()
            self.log.info("点击确定按钮")
            time.sleep(1)
            self.tools.swipeUp(1000)
            self.handle.Kjlb_browseorgspace_menu_flow_menu_new_leave_submit_click()
            self.log.info("点击提交按钮")
            time.sleep(1)
            self.tools.swipeUp(1000)
            self.handle.Kjlb_browseorgspace_menu_flow_menu_new_leave_revoke_click()
            self.log.info("点击撤销")
            self.handle.Kjlb_browseorgspace_menu_flow_menu_new_leave_revoke_confirm_click()
            self.log.info("点击确认")
            self.handle.Kjlb_browseorgspace_menu_flow_back_click()
            self.log.info("点击返回")

        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_process03 : %s" % err)
            raise err

    # 4.4新建加班审批
    def test_process04(self):
        '''新建加班审批
        :return:
        '''

        try:
            # 1.点击菜单栏
            self.handle.Kjlb_browseorgspace_menu_flow_menu_click()
            self.log.info("点击菜单栏")

            # 2.点击新申请
            self.handle.Kjlb_browseorgspace_menu_flow_menu_new_click()
            self.log.info("点击新申请")

            # 3.点击请假
            self.handle.Kjlb_browseorgspace_menu_flow_menu_new_overtime_click()
            self.log.info("点击加班")

            # 4.选择开始时间
            self.handle.Kjlb_browseorgspace_menu_flow_menu_new_leave_start_click()
            self.log.info("点击开始时间")

            # 5.点击确定
            self.handle.Kjlb_browseorgspace_menu_flow_menu_new_leave_start_sure_click()
            self.log.info("点击确定")

            # 5.选择结束时间
            self.handle.Kjlb_browseorgspace_menu_flow_menu_new_leave_end_click()
            self.log.info("选择结束时间")

            # 6.滑动年份
            time.sleep(1)
            self.tools.swipeUps(170, 1512, 500)
            self.log.info("添加一年")

            # 7.点击确定
            self.handle.Kjlb_browseorgspace_menu_flow_menu_new_leave_start_sure_click()
            self.log.info("点击确定")

            # 8.检查天数，增加1年，应为365
            year = int(self.handle.Kjlb_browseorgspace_menu_flow_menu_new_leave_day_text())
            years = 365
            assert years == year, "年份统计有误"
            self.log.info('年份统计无误')

            # 9.输入请假内容
            self.handle.Kjlb_browseorgspace_menu_flow_menu_new_leave_et_sendkey('加班')
            self.log.info("输入内容:加班")  # 后面以数据库形式，存入文本

            # 10.点击附件
            self.handle.Kjlb_browseorgspace_menu_flow_menu_new_leave_photo_click()
            self.log.info("点击附件")

            # 11.选择照片
            self.handle.Kjlb_browseorgspace_menu_flow_menu_new_leave_start_alumm_click()
            self.log.info("选择相册添加")
            self.handle.Kjlb_browseorgspace_menu_product_new_addphoto_album_list_click(0)  # 选择第一张照片
            self.log.info('选择第%s张照片' % 0)  # 后面新建了数据库，以数据库数值代替
            self.handle.Kjlb_browseorgspace_menu_product_new_addphoto_album_confirm_click()  # 点击完成
            self.log.info('点击完成')
            sleep(4)

            # 12.选择审批人
            self.handle.Kjlb_browseorgspace_menu_flow_menu_new_leave_approver_click()
            self.log.info("点击审批人")
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='管理员']").click()
            self.log.info("选择管理员")  # 后面利用xpath，用数据库给一个职位身份来选择具体的人
            time.sleep(1)
            self.tools.swipeUp(1000)
            self.log.info("向上滑动0.5秒")
            self.handle.Kjlb_browseorgspace_menu_flow_menu_new_leave_ccpeople_click()
            self.log.info("点击抄送人")
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='管理员']").click()
            self.log.info("选择管理员")
            self.handle.Kjlb_browseorgspace_menu_flow_menu_new_leave_approver_submit_click()
            self.log.info("点击确定按钮")
            time.sleep(1)
            self.tools.swipeUp(1000)
            self.handle.Kjlb_browseorgspace_menu_flow_menu_new_leave_submit_click()
            self.log.info("点击提交按钮")
            self.handle.Kjlb_browseorgspace_menu_flow_menu_new_leave_revoke_click()
            self.log.info("点击撤销")
            self.handle.Kjlb_browseorgspace_menu_flow_menu_new_leave_revoke_confirm_click()
            self.log.info("点击确认")
            self.handle.Kjlb_browseorgspace_menu_flow_back_click()
            self.log.info("点击返回")

        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_process04 : %s" % err)
            raise err

    # 4.5新建方案审批
    def test_process05(self):
        '''新建加班审批
        :return:
        '''

        try:
            # 1.点击菜单栏
            self.handle.Kjlb_browseorgspace_menu_flow_menu_click()
            self.log.info("点击菜单栏")

            # 2.点击新申请
            self.handle.Kjlb_browseorgspace_menu_flow_menu_new_click()
            self.log.info("点击新申请")

            # 3.点击请假
            self.handle.Kjlb_browseorgspace_menu_flow_menu_new_scheme_click()
            self.log.info("点击方案审批")

            # 4.选择开始时间
            self.handle.Kjlb_browseorgspace_menu_flow_menu_new_leave_start_click()
            self.log.info("点击开始时间")

            # 5.点击确定
            self.handle.Kjlb_browseorgspace_menu_flow_menu_new_leave_start_sure_click()
            self.log.info("点击确定")

            # 5.选择结束时间
            self.handle.Kjlb_browseorgspace_menu_flow_menu_new_leave_end_click()
            self.log.info("选择结束时间")

            # 6.滑动年份
            time.sleep(1)
            self.tools.swipeUps(170, 1512, 500)
            self.log.info("添加一年")

            # 7.点击确定
            self.handle.Kjlb_browseorgspace_menu_flow_menu_new_leave_start_sure_click()
            self.log.info("点击确定")

            # 8.检查天数，增加1年，应为365
            year = int(self.handle.Kjlb_browseorgspace_menu_flow_menu_new_leave_day_text())
            years = 365
            assert years == year, "年份统计有误"
            self.log.info('年份统计无误')

            # 9.输入请假内容
            self.handle.Kjlb_browseorgspace_menu_flow_menu_new_leave_et_sendkey('加班')
            self.log.info("输入内容:方案审批")  # 后面以数据库形式，存入文本

            # 10.点击附件
            self.handle.Kjlb_browseorgspace_menu_flow_menu_new_leave_photo_click()
            self.log.info("点击附件")

            # 11.选择照片
            self.handle.Kjlb_browseorgspace_menu_flow_menu_new_leave_start_alumm_click()
            self.log.info("选择相册添加")
            self.handle.Kjlb_browseorgspace_menu_product_new_addphoto_album_list_click(0)  # 选择第一张照片
            self.log.info('选择第%s张照片' % 0)  # 后面新建了数据库，以数据库数值代替
            self.handle.Kjlb_browseorgspace_menu_product_new_addphoto_album_confirm_click()  # 点击完成
            self.log.info('点击完成')
            sleep(4)

            # 12.选择审批人
            self.handle.Kjlb_browseorgspace_menu_flow_menu_new_leave_approver_click()
            self.log.info("点击审批人")
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='管理员']").click()
            self.log.info("选择管理员")  # 后面利用xpath，用数据库给一个职位身份来选择具体的人
            time.sleep(1)
            self.tools.swipeUp(1000)
            self.log.info("向上滑动0.5秒")
            self.handle.Kjlb_browseorgspace_menu_flow_menu_new_leave_ccpeople_click()
            self.log.info("点击抄送人")
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='管理员']").click()
            self.log.info("选择管理员")
            self.handle.Kjlb_browseorgspace_menu_flow_menu_new_leave_approver_submit_click()
            self.log.info("点击确定按钮")
            time.sleep(1)
            self.tools.swipeUp(1000)
            self.handle.Kjlb_browseorgspace_menu_flow_menu_new_leave_submit_click()
            self.log.info("点击提交按钮")
            self.handle.Kjlb_browseorgspace_menu_flow_menu_new_leave_revoke_click()
            self.log.info("点击撤销")
            self.handle.Kjlb_browseorgspace_menu_flow_menu_new_leave_revoke_confirm_click()
            self.log.info("点击确认")
            self.handle.Kjlb_browseorgspace_menu_flow_back_click()
            self.log.info("点击返回")

        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_process05 : %s" % err)
            raise err
