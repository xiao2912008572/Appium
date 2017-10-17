__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from time import sleep
from StoneUIFramework.config.globalparam import GlobalParam
from StoneUIFramework.public.handle.yunku.YUNKUHANDLE3 import _YUNKUHANDLE3
from StoneUIFramework.public.common.log import Log


# 上传图片
class UploadPic:
    # 1.初始化
    def __init__(self):
        # 1.创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')
        # 2.创建截图路径、日志路径、日志名
        self.logfile = cf.getParam('log', 'logfile')  # 日志文件名
        # 3.创建日志模块
        self.log = Log(self.logfile)

    # 2.上传图片-公用方法
    def uploadPic(self, driver, picno):
        # 创建_YUNKUHANDLE3公有定位控件对象
        handle = _YUNKUHANDLE3(driver)
        sleep(1)
        try:
            self.log.info('------START:test1_1上传图片.UploadPic.py------')
            # # 1.云库首页
            # handle.Yk_click()
            # self.log.info('点击进入云库首页')
            # 2.点击+按钮
            handle.Yk_add_click()
            self.log.info('点击：+按钮')
            # 3.选择相册
            handle.Yk_add_ByAlbum_click()
            self.log.info('选择相册方式')
            sleep(1)
            # 4.选择第1张图片
            handle.Yk_add_ByAlbum_piclist_click(picno)
            self.log.info('选择第{0}张照片'.format(picno+1))
            #5.点击完成
            handle.Yk_add_ByAlbum_confirm_click()
            self.log.info('点击完成')
        except Exception as err:
            self.log.error("UploadPic Inside : %s" % err)
            raise err
