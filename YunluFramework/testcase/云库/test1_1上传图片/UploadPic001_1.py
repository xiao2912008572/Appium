__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from StoneUIFramework.testcase.云库.test1_1上传图片 import *


# 云库上传图片
@ddt.ddt
class yunku_UploadPic(unittest.TestCase):
    # 1.全局测试数据
    d = DataInfo("yunku.xls")  # 创建DataInfo()对象
    picNo_1 = int(d.cell("test001", 2, 1))  # 第1张图片

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
        self.screen_path = cf.getParam('yunku', "yun_path_001_1")  # 通过配置文件获取截图的路径
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名
        # 6.创建日志记录模块
        self.log = Log(self.logfile)
        # 7.创建UploadPic和DeletePic对象
        self.up = UploadPic()
        self.dl = DeletePic()
        sleep(1)
        # 8.打印日志
        self.log.info('****************************************用例开始！****************************************')
        self.log.info("------------START:test1_1上传图片.UploadPic001_1.py------------")

    # 3.释放资源
    def tearDown(self):
        # 1.打印日志
        self.log.info("------------END:test1_1上传图片.UploadPic001_1.py------------")
        self.log.info('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~用例结束！~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        # 2.关闭driver
        self.driver.quit()

    # 4.测试用例
    @ddt.data([picNo_1])
    @ddt.unpack
    def test_uploadpic(self, picno):
        '''上传图片'''
        try:
            # -------------上传图片------------
            # 1.点击云库首页
            self.handle.Yk_click()
            self.log.info('点击云库首页')
            # 2.检查上传前云库图片数量
            pic_amount_begin = len(self.handle.Yk_piclist_getElements())
            self.log.info('获取上传前云库图片数量：{0}'.format(pic_amount_begin))
            # 3.上传图片
            self.up.uploadPic(self.driver, picno)
            # 4.判断是否上传成功
            self.handle.Yk_add_ByAlbum_confirm_pageisvisible()
            self.log.info('云库首页可见，等待上传结束')
            sleep(1)
            # 5.检查上传后云库图片数量
            pic_amount_end = len(self.handle.Yk_piclist_getElements())
            self.log.info('获取上传后云库图片数量：{0}'.format(pic_amount_end))
            assert pic_amount_end == pic_amount_begin + 1, '上传图片失败'
            self.log.info('上传图片成功')
            # 6.删除图片
            self.dl.deletePic(self.driver, picno)
            # 7.删除图片云库图片数量检查
            pic_amount_delete = len(self.handle.Yk_piclist_getElements())
            self.log.info('获取删除后云库图片数量：{0}'.format(pic_amount_delete))
            assert pic_amount_begin == pic_amount_delete, "删除图片失败"
            self.log.info('删除图片成功')
        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("UploadPic Outside : %s" % err)
            raise err
