__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from StoneUIFramework.testcase.云库.test2_1编辑图片 import *


# 云库图片编辑
@ddt.ddt
class yunku_EditPic(unittest.TestCase):
    # 1.全局测试数据
    d = DataInfo("yunku.xls")  # 创建DataInfo()对象
    picNo_1 = int(d.cell("test002", 2, 1))  # 第1张图片
    title_end_1 = random.choice(['apple', 'pear', 'peach', 'orange', 'lemon'])  # 目标标题-随机取值
    remark_end_1 = random.choice(['apple', 'pear', 'peach', 'orange', 'lemon'])  # 目标备注-随机取值
    title_start_1 = d.cell("test002", 2, 4)  # 初始化标题
    remark_start_1 = d.cell("test002", 2, 5)  # 初始化备注

    # 2.初始化
    def setUp(self):
        # 1.建立连接信息
        cnn = Connect()
        self.driver = cnn.connect()
        # 2.创建工具类
        self.tools = Tools(self.driver)  # tools工具
        # 3.创建_YUNKUHANDLE3公有定位控件对象
        self.handle = YUNKUHANDLE3(self.driver)
        # 4.创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')
        # 5.获取截图路径、日志路径、日志名
        self.screen_path = cf.getParam('yunku', "yun_path_001_2")  # 通过配置文件获取截图的路径
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名
        # 6.创建日志记录模块
        self.log = Log(self.logfile)
        # 7.创建EditPic和RecoveryPic对象
        self.ed = EditPic()
        self.re = RecoveryPic()
        sleep(1)
        # 8.打印日志
        self.log.info('****************************************用例开始！****************************************')
        self.log.info("------------START:test2_1编辑图片.EditPic002_1.py------------")

    # 3.释放资源
    def tearDown(self):
        # 1.打印日志
        self.log.info("------------END:test2_1编辑图片.EditPic002_1.py------------")
        self.log.info('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~用例结束！~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        # 2.关闭driver
        self.driver.quit()

    # 4.测试用例
    @ddt.data([picNo_1, title_end_1, remark_end_1, title_start_1, remark_start_1])
    @ddt.unpack
    def test_editpic(self, picno, pictitle_end, remark_end, pictitle_start, remark_start):
        '''编辑图片'''
        try:
            # -------------编辑图片------------
            # 1.点击云库首页
            self.handle.Yk_click()
            self.log.info('点击云库首页')
            # 2.点击第1张照片
            self.handle.Yk_piclist_click(picno)
            self.log.info('选择第{0}张照片'.format(picno))
            # 2.1检查图片是否存在备注名
            if self.handle.Yk_piclist_picself_reamark_pageisvisible():
                # if self.driver.find_elements_by_id("com.yunlu6.stone:id/tv_remark"):
                self.log.info('图片备注名可见')
                # 3.查看当前图片的标题和备注
                pic_title_begin = self.handle.Yk_piclist_picanme_text()
                pic_remark_begin = self.handle.Yk_piclist_picself_reamark_text()
                self.log.info('检查编辑前图片名称为：{0}'.format(pic_title_begin))
                self.log.info('检查编辑前图片备注为：{0}'.format(pic_remark_begin))
                # 4.编辑图片
                self.ed.editPic(self.driver, picno, pictitle_end, remark_end)
                # 5.查看编辑后图片的标题和备注
                pic_title_end = self.handle.Yk_piclist_picanme_text()
                pic_remark_end = self.handle.Yk_piclist_picself_reamark_text()
                self.log.info('检查编辑后图片名称为：{0}'.format(pic_title_end))
                self.log.info('检查编辑后图片备注为：{0}'.format(pic_remark_end))
                assert pictitle_end == pic_title_end, '图片名称编辑失败'
                assert remark_end == pic_remark_end, '图片备注编辑失败'
                self.log.info('图片名称和备注保存成功')
                # 6.返回云库
                self.handle.Yk_piclist_menu_edit_back_click()
                self.log.info('点击返回云库')
                # 7.还原标题和备注名
                self.re.recoveryPic(self.driver, picno, pictitle_start, remark_start)
                # 8.还原后标题和备注名检查
                pic_title_re = self.handle.Yk_piclist_picanme_text()
                pic_remark_re = self.handle.Yk_piclist_picself_reamark_text()
                self.log.info('检查还原后图片名称为：{0}'.format(pic_title_re))
                self.log.info('检查还原后图片备注为：{0}'.format(pic_remark_re))
                assert pictitle_start == pic_title_re, '图片名称还原成功'
                assert remark_start == pic_remark_re, '图片备注还原成功'
                self.log.info('图片名称和备注还原成功')
            else:
                self.log.info('图片备注名不可见!')
                # 3.查看当前图片的标题和备注
                pic_title_begin = self.handle.Yk_piclist_picanme_text()
                self.log.info('检查编辑前图片名称为：{0}'.format(pic_title_begin))
                self.log.info('检查编辑前图片备注为：{0}'.format('空'))
                # 4.编辑图片
                self.ed.editPic(self.driver, picno, pictitle_end, remark_end)
                # 5.查看编辑后图片的标题和备注
                pic_title_end = self.handle.Yk_piclist_picanme_text()
                pic_remark_end = self.handle.Yk_piclist_picself_reamark_text()
                self.log.info('检查编辑后图片名称为：{0}'.format(pic_title_end))
                self.log.info('检查编辑后图片名称为：{0}'.format(pic_remark_end))
                assert pictitle_end == pic_title_end, '图片名称编辑失败'
                assert remark_end == pic_remark_end, '图片备注编辑失败'
                self.log.info('图片名称和备注保存成功')
                # 6.返回云库
                self.handle.Yk_piclist_menu_edit_back_click()
                self.log.info('点击返回云库')
                # 7.还原标题和备注名
                self.re.recoveryPic(self.driver, picno, pictitle_start, remark_start)
                # 8.还原后标题和备注名检查
                pic_title_re = self.handle.Yk_piclist_picanme_text()
                pic_remark_re = self.handle.Yk_piclist_picself_reamark_text()
                self.log.info('检查还原后图片名称为：{0}'.format(pic_title_re))
                self.log.info('检查还原后图片备注为：{0}'.format(pic_remark_re))
                assert pictitle_start == pic_title_re, '图片名称还原成功'
                assert remark_start == pic_remark_re, '图片备注还原成功'
                self.log.info('图片名称和备注还原成功')
        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("EditPic Outside : %s" % err)
            raise err
