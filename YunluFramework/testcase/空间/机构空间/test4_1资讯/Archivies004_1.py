__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from YunluFramework.testcase.空间.机构空间.test4_1资讯 import *


# 资讯发布
@ddt.ddt
class space_ArchiviesO(unittest.TestCase):
    # 1.创建数据库操作对象
    d = DataMysql()
    sql01 = "select * from test4_1_orgarchivies_01"
    sql04 = "select * from test4_1_orgarchivies_04"
    sql05 = "select * from test4_1_orgarchivies_05"
    data01 = d.select(sql01, 0)
    data04 = d.select(sql04, 0)
    data05 = d.select(sql05, 0)

    # 2.初始化
    @classmethod
    def setUpClass(self):
        # 1.建立连接信息
        cnn = Connect()
        self.driver = cnn.connect()

        # 2.创建工具类
        self.tools = Tools(self.driver)  # tools工具

        # 3.创建 _SPACEHANDLE5公有定位控件对象
        self.handle = SPACEHANDLE5(self.driver)

        # 4.创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')

        # 5.获取截图路径、日志路径、日志名
        self.screen_path = cf.getParam('space', "org_path_004_1")  # 通过配置文件获取截图的路径
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名

        # 6.创建日志记录模块
        self.log = Log(self.logfile)

        # 7.创建Space操作对象
        self.common = CommonSpace(self.handle, self.log, self.tools)

        # 8.打印日志
        self.log.info('****************************************用例开始！****************************************')
        self.log.info('------------START:test4_1资讯.Archivies004_1.py------------')

    # 3.释放资源
    @classmethod
    def tearDownClass(self):
        # 1.打印日志
        self.log.info("------------END:test4_1资讯.Archivies004_1.py------------")  # 宣布成功
        self.log.info('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~用例结束！~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

        # 2.关闭driver
        # self.driver.quit()

    # 4.测试用例
    # 4.1 进入空间
    @ddt.data(data01)
    @ddt.unpack
    def test_archivies01(self, spacename):
        '''进入空间
        :param spacename:空间名
        '''
        try:
            # 1.进入空间
            self.common.enter_space(spacename)

        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_archivies01 : %s" % err)
            raise err

    # 4.2 进入资讯
    def test_archivies02(self):
        '''进入资讯
        :return:
        '''
        try:
            # 1.进入资讯
            self.common.click_org_menu('archivies')

        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_archivies02 : %s" % err)
            raise err

    # 4.3 各入口跳转检查
    def test_archivies03(self):
        '''各入口跳转检查
        :return:
        '''
        try:
            '''
                20180320资讯功能更新，此处需更改，start
            '''
            # 4.1 入口一:图片新增按钮
            # self.log.info('入口一：图片新增按钮检查')
            # self.handle.Kjlb_browseorgspace_menu_archivies_picadd_click()
            # self.log.info('点击新增图片按钮')
            # self.handle.Kjlb_browseorgspace_menu_archivies_new_back_click()  # 返回
            # self.log.info('点击返回')
            '''
                20180320，end
            '''

            # 1.新增资讯

            # 4.2 入口二:右上角新增
            self.log.info('入口二：右上角新增检查')
            self.handle.Kjlb_browseorgspace_menu_archivies_new_click()
            self.log.info('点击右上角新增按钮')

        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_archivies03 : %s" % err)
            raise err

    # 4.4 添加资讯
    @ddt.data(data04)
    @ddt.unpack
    def test_archivies04(self, title, typelist):
        try:
            # 1.添加照片
            self.handle.Kjlb_browseorgspace_menu_archivies_new_addphoto_click()
            self.log.info('点击+照片')
            self.handle.Kjlb_browseorgspace_menu_archivies_new_addphoto_album_click()  # 点击相册
            self.log.info('点击相册')
            self.handle.Kjlb_browseorgspace_menu_archivies_new_addphoto_album_list_click(0)  # 点击第一张照片
            self.log.info('点击第一张照片')
            self.handle.Kjlb_browseorgspace_menu_archivies_new_addphoto_album_confirm_click()  # 点击完成
            self.log.info('点击完成')
            sleep(1)

            # 2.标题
            self.handle.Kjlb_browseorgspace_menu_archivies_new_title_sendkeys(title)  # 标题
            self.log.info('标题：%s' % title)

            # 3.类型
            self.handle.Kjlb_browseorgspace_menu_archivies_new_type_click()  # 类型
            self.log.info('点击类型')
            self.handle.Kjlb_browseorgspace_menu_archivies_new_type_typelist_click(typelist)  # 经典作品
            self.log.info('选择经典作品')

            # 4.勾选
            self.handle.Kjlb_browseorgspace_menu_archivies_new_confirm_click()  # 勾选
            self.log.info('勾选')
            self.handle.Kjlb_browseorgspace_menu_archivies_new_confirm_late_click()  # 保存
            self.log.info('保存')

            # 5.点击资讯发布
            self.handle.Kjlb_browseorgspace_menu_archivies_pic_click(0)  # 点击第一张资讯
            self.log.info('点击第一张资讯')
            self.handle.Kjlb_browseorgspace_menu_archivies_pic_click(0)  # 点击第一张资讯
            self.log.info('点击第一张资讯')
            self.handle.Kjlb_browseorgspace_menu_archivies_pic_menu_click()  # 菜单栏
            self.log.info('点击菜单栏')
            self.handle.Kjlb_browseorgspace_menu_archivies_pic_menu_new_click()  # 发布
            self.log.info('点击发布')
            type = self.handle.Kjlb_browseorgspace_menu_archivies_pic_menu_new_type_text()  # 获取资讯类型
            assert type == "经典作品(1)", "资讯类型保存错误"
            self.log.info('资讯类型检查')
            self.driver.implicitly_wait(1)  # 只能等待1秒
            self.handle.Kjlb_browseorgspace_menu_archivies_pic_click(0)  # 点击第一张资讯
            self.log.info('点击第一张资讯')
            self.handle.Kjlb_browseorgspace_menu_archivies_pic_click(0)  # 点击第一张资讯
            self.log.info('点击第一张资讯')
            titlee = self.handle.Kjlb_browseorgspace_menu_archivies_pic_title_text()  # 获取资讯标题
            assert titlee == title, "资讯标题未保存成功"
            self.log.info('资讯标题检查')

            # 6.返回到空间列表
            self.handle.Kjlb_browseorgspace_menu_archivies_pic_back_click()
            self.handle.Kjlb_browseorgspace_menu_archivies_back_click()
            self.handle.Kjlb_browseorgspace_menu_archivies_back_click()
            self.handle.Kjlb_browseorgspace_back_click()  # 返回空间
            self.log.info('返回空间')

        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_archivies04 : %s" % err)
            raise err

    # 4.5 删除资讯
    @ddt.data(data05)
    @ddt.unpack
    def test_archivies05(self, spacename):
        try:
            # 1.进入空间
            self.common.enter_space(spacename)

            # 2.右上角:菜单栏选择资讯
            self.handle.Kjlb_browseorgspace_menu_click()
            self.log.info('菜单栏选择资讯')
            self.handle.Kjlb_browseorgspace_menu_archivies_click()
            self.log.info('点击资讯')

            # 3.判断是否有图片，有就进入删除
            # 3.1判断-点击第1张图片-点击第1张图片
            if self.handle.Kjlb_browseorgspace_menu_archivies_pic_element() != []:
                self.log.info('判断是否有图片，有就进入删除')
                self.handle.Kjlb_browseorgspace_menu_archivies_pic_click(0)
                self.log.info('点击第一张图片')
                self.handle.Kjlb_browseorgspace_menu_archivies_pic_click(0)
                self.log.info('点击第一张图片')

                # 3.2菜单栏
                self.handle.Kjlb_browseorgspace_menu_archivies_pic_menu_click()
                self.log.info('点击菜单栏')

                # 3.3下架
                self.handle.Kjlb_browseorgspace_menu_archivies_pic_menu_offshelf_click()
                self.log.info('下架')

                # 3.4点击第1张图片
                sleep(1)
                self.handle.Kjlb_browseorgspace_menu_archivies_pic_click(0)
                self.log.info('点击第一张图片')
                sleep(2)
                self.handle.Kjlb_browseorgspace_menu_archivies_pic_click(0)
                self.log.info('点击第一张图片')

                # 3.4菜单栏
                self.handle.Kjlb_browseorgspace_menu_archivies_pic_menu_click()
                self.log.info('菜单栏')

                # 3.5删除
                self.handle.Kjlb_browseorgspace_menu_archivies_pic_menu_delete_click()
                self.log.info('删除')

                # 3.6返回-空间主界面
                self.handle.Kjlb_browseorgspace_menu_archivies_back_click()
                self.log.info('返回')

                # 3.7删除检查
                self.handle.Kjlb_browseorgspaceByName_click(spacename)
                self.log.info('进入空间：%s' % spacename)

                # 3.8菜单栏
                self.handle.Kjlb_browseorgspace_menu_click()
                self.log.info('点击菜单栏')

                # 3.9资讯
                self.handle.Kjlb_browseorgspace_menu_archivies_click()
                self.log.info('点击资讯')

                # 3.10判断
                self.log.info('判断是否为空，为空即是已删除')
                assert [] == self.handle.Kjlb_browseorgspace_menu_archivies_pic_element(), 'Error Pic Delete Failed!'

        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_archivies05 : %s" % err)
            raise err
