__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from StoneUIFramework.testcase.空间.私人空间.test1_1创建私人空间 import *


# 创建私人空间
@ddt.ddt
class perspace_CreateP(unittest.TestCase):
    # 1.全局测试数据
    d = DataInfo("space.xls")  # 创建DataInfo()对象
    spacename_1 = d.cell("test006-私人空间", 2, 13)  # 空间名:appium私人空间
    # 2.各空间类型下热门空间名第1个标签
    clothesT_1 = (d.cell("test006-私人空间", 3, 1))  # 我的衣柜0
    foodT_1 = (d.cell("test006-私人空间", 3, 2))  # 舌尖上的中国1
    liveT_1 = (d.cell("test006-私人空间", 3, 3))  # 我爱我家2
    walkT_1 = (d.cell("test006-私人空间", 3, 4))  # 旅游照片3
    studyT_1 = (d.cell("test006-私人空间", 3, 5))  # 互联网十4
    healthT_1 = (d.cell("test006-私人空间", 3, 6))  # 强身健体5
    socialT_1 = (d.cell("test006-私人空间", 3, 7))  # 同学们6
    workT_1 = (d.cell("test006-私人空间", 3, 8))  # 办公场所7
    literatureT_1 = (d.cell("test006-私人空间", 3, 9))  # 文娱空间8
    entertainmentT_1 = (d.cell("test006-私人空间", 3, 10))  # 电影放映室9
    beautyT_1 = (d.cell("test006-私人空间", 3, 11))  # Onlyyou10
    otherT_1 = (d.cell("test006-私人空间", 3, 12))  # 摄影11

    # 2.初始化
    def setUp(self):
        # 1.建立连接信息
        cnn = Connect()
        self.driver = cnn.connect()
        # 2.创建工具类
        self.tools = Tools(self.driver)  # tools工具
        # 3.创建_CreatePersonalSpaceHandle公有定位控件对象
        self.handle = SPACEHANDLE5(self.driver)
        # 4.创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')
        # 5. 获取截图路径、日志路径、日志名
        self.screen_path = cf.getParam('space', "per_path_001_1")  # 通过配置文件获取截图的路径
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名
        # 6.创建Createspace和Closespace对象
        self.cr = CreatePersonSpace()
        self.cl = ClosePersonSpace()
        sleep(2)
        # 7.创建日志记录模块
        self.log = Log(self.logfile)
        # 8.打印日志
        self.log.info('****************************************用例开始！****************************************')
        self.log.info("------------START:test1_1创建私人空间CreatePersonSpace001_1.py------------")

    # 3.释放资源
    def tearDown(self):
        # 1.打印日志
        self.log.info("------------END:test1_1创建私人空间CreatePersonSpace001_1.py------------")
        self.log.info('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~用例结束！~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        # 2.关闭driver
        self.driver.quit()

    # 4.测试用例
    @ddt.data([spacename_1, clothesT_1, foodT_1, liveT_1,
               walkT_1, studyT_1, healthT_1, socialT_1, workT_1,
               literatureT_1, entertainmentT_1, beautyT_1, otherT_1])
    @ddt.unpack
    def test_perspacecreate(self, spacename, clothesT, foodT, liveT, walkT,
                            studyT, healthT, socialT, workT, literatureT,
                            entertainmentT, beautyT, otherT):
        try:
            # 1.进入空间列表
            sleep(1)
            self.handle.Kjlb_click()
            self.log.info('进入空间列表')
            # #2.点击主菜单
            # self.handle.Kjlb_mainmenu_click()
            # #3.点击+私人空间
            # self.handle.Kjlb_mainmenu_newpersonspace_click()
            # 4.创建私人空间
            if self.driver.find_elements_by_name(spacename) != []:  # 检查当前的私人空间是否已经存在,如果存在就关闭
                self.cl.closePersonSpace(self.driver, spacename)  # 先关闭
                self.cr.createPersonSpace(self.driver, spacename, clothesT, foodT, liveT,
                                          walkT, studyT, healthT, socialT, workT, literatureT,
                                          entertainmentT, beautyT, otherT)  # 再创建
                self.cl.closePersonSpace(self.driver, spacename)  # 再关闭
            else:
                self.cr.createPersonSpace(self.driver, spacename, clothesT, foodT, liveT,
                                          walkT, studyT, healthT, socialT, workT, literatureT,
                                          entertainmentT, beautyT, otherT)  # 创建
                self.cl.closePersonSpace(self.driver, spacename)  # 关闭
        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("Outside : %s" % err)
            raise err
