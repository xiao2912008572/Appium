__author__ = 'xiaoj'
from time import sleep
from appium import webdriver
import os
import configparser
from StoneUIFramework.public.common.publicfunction import Tools

class Connect:
    def __init__(self):
        pass
    def connect(self):
        cf = configparser.ConfigParser()
        #获取当前文件夹的父目录的父目录的绝对路径
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        file_path = os.path.join(BASE_DIR,"config","connect.conf")
        cf.read(file_path)#读取配置文件
        desired_caps = eval(cf.get("APP","desired_caps1"))
        #初始化appium连接
        try:
            driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        except:
            assert False ,"初始化appium连接失败,程序已退出!!!"
        sleep(2)
        return driver

# cnn = Connect()
# driver = cnn.connect()
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

