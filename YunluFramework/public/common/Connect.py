__author__ = 'xiaoj'
from time import sleep
from appium import webdriver
import os
import configparser

'''
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from StoneUIFramework.public.common.log import Log
from StoneUIFramework.config.globalparam import GlobalParam
cf = GlobalParam('config','path_file.conf')
logfile = cf.getParam('space',"logfile")#日志文件名
logger = Log(logfile)
'''

# from StoneUIFramework.public.common.pyappium import PyAppium
from YunluFramework.public.handle.yunku.YUNKUHANDLE1 import YUNKUHANDLE1


class Connect:
    def __init__(self):
        pass

    def connect(self):
        cf = configparser.ConfigParser()
        # 获取当前文件夹的父目录的父目录的绝对路径
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        file_path = os.path.join(BASE_DIR, "config", "connect.conf")
        # 读取配置文件
        cf.read(file_path)
        desired_caps1 = eval(cf.get("APP","desired_caps1"))
        # desired_caps1 = eval(cf.get("APP", "desired_caps"))
        # 初始化appium连接
        try:
            driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps1)
            # driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        except:
            assert False, "初始化appium连接失败,程序已退出!!!"
        sleep(2)
        return driver


# cnn = Connect()
# driver = cnn.connect()
# sleep(2)
'''
云库删除坐标测试
h = _YUNKUHANDLE1(driver)
h.Yk_click()#点击云库
h.Yk_menu_click()#点击菜单栏
h.Yk_piclist_click(0)#点击第一张照片
h.Yk_menu_piclist_delete_click()#点击删除
'''

# driver.find_element_by_id("aaa ").send_keys()
# sleep(2)
# h = _SPACEHANDLE1(driver)
# h.Kjlb_click()
# h.Kjlb_browseorgspaceByID_click(0)

# p = PyAppium(driver)
# css = ("id->com.yunlu6.stone:id/navi_item_zone1")
# p.get_element(css,'空间列表').click()


'''
class Buyu(object):
    def __init__(self):
        self.driver = driver

    def find_element(self,locator,text = '',timeout=5):
        try:
            element = WebDriverWait(self.driver,timeout,1).until(EC.presence_of_element_located(locator))
        except Exception:
            logger.error("定位元素：%s超时"%locator[1])
            assert False,"定位元素:%s超时"%text
        return element

    def click(self,locator):
        try:
            element = self.find_element(locator)
            element.click()
        except Exception:
            logger.error('元素：%s无法点击'%locator[1])

a = Buyu()
locator = ("id","com.yunlu6.stone:id/navi_item_zone1")
# a.find_element(locator,'空间列表').click()
a.find_element(locator).click()
'''

'''
# row_x = driver.get_window_size()['width']
# row_y = driver.get_window_size()['height']
# print(row_x)
# print(row_y)
#
# sleep(3)
# tools = Tools(driver)
# tools.click_element_by_coordinate(150,400)


# standard_x = 1080
# standard_y = 1920
# #1. 算X轴和Y轴相对坐标率
# scale_x = row_x/standard_x
# scale_y = row_y/standard_y
# #2. 将真实坐标转换成相对坐标
# adjust_x = int(( 150 * scale_x ))
# adjust_y = int(( 400 * scale_y ))
# print(adjust_x)
# print(adjust_y)
# #3. 点击
# driver.tap([(adjust_x,adjust_y)],duration=500)
'''
