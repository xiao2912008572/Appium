from time import sleep
from StoneUIFramework.config.globalparam import GlobalParam
from StoneUIFramework.public.handle.yunku.YUNKUHANDLE3 import _YUNKUHANDLE3
from StoneUIFramework.public.common.log import Log


# 编辑图片
class EditPic:
    # 1.初始化
    def __init__(self):
        # 1.创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')
        # 2.创建截图路径、日志路径、日志名
        self.logfile = cf.getParam('log', 'logfile')  # 日志文件名
        # 3.创建日志模块
        self.log = Log(self.logfile)

    # 2.编辑图片-公用方法
    def editPic(self, driver, picno, pictitle, remark):
        # 创建_YUNKUHANDLE3公有定位控件对象
        handle = _YUNKUHANDLE3(driver)
        sleep(1)
        try:
            self.log.info('------START:test2_1编辑图片.EditPic.py------')
            # # 1.云库首页
            # handle.Yk_click()
            # self.log.info('点击进入云库首页')
            # #2.点击第1张照片
            # handle.Yk_piclist_click(picno)
            # self.log.info('选择第{0}张照片'.format(picno))
            # 3.点击菜单栏
            handle.Yk_piclist_menu_click()
            self.log.info('点击菜单栏')
            # 4.点击编辑
            handle.Yk_piclist_menu_edit_click()
            self.log.info('点击编辑')
            # 5.修改名称
            handle.Yk_piclist_menu_edit_name_sendkeys(pictitle)
            self.log.info('修改图片名称为：{0}'.format(pictitle))
            # 6.修改备注
            handle.Yk_piclist_menu_edit_remark_sendkeys(remark)
            self.log.info('修改图片备注为：{0}'.format(remark))
            # 7.点击保存
            handle.Yk_piclist_menu_edit_save_click()
            self.log.info('点击保存')
            self.log.info('------END:test2_1编辑图片.EditPic.py------')
        except Exception as err:
            self.log.error("EditPic Inside : %s" % err)
            raise err
