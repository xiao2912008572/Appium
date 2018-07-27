__author__ = 'xiaoj'
__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import sys
import os
import unittest
from time import sleep
from appium import webdriver
import logging
from StoneAPP.AllTools.Tools import Tools


#使用已登录的账号进行浏览产品
class YUNLU(unittest.TestCase):
    def test_login(self):
        #连接信息
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['appPackage'] = 'com.yunlu6.stone'
        desired_caps['appActivity'] = '.WelcomeActivity'
        # desired_caps['deviceName'] = 'TWGDU16A20000974'
        desired_caps['deviceName'] = '127.0.0.1:62001'
        desired_caps["unicodeKeyboard"] = True
        desired_caps["resetKeyboard"] = True

        #初始化appium连接
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        sleep(2)
        createContactButton = None
        try:
            sleep(2)
            driver.save_screenshot("C地址拼接:\\Users\\xiaoj\Desktop\screenshot\云视搜索企业\main.png")

            #点击云视企业入口
            createContactButton = driver.find_element_by_id("com.yunlu6.stone:id/cloundview_rl_bottom_company")
            createContactButton.click()
            sleep(1)
            driver.save_screenshot("C地址拼接:\\Users\\xiaoj\Desktop\screenshot\云视搜索企业\企业列表.png")
            sleep(1)

            #输入关键字"环球万国"
            driver.find_element_by_id("com.yunlu6.stone:id/buildstone_search_key").click()
            driver.find_element_by_id("com.yunlu6.stone:id/et_search_key").send_keys(u"环球万国")
            driver.find_element_by_id("com.yunlu6.stone:id/iv_search").click()
            driver.save_screenshot("C地址拼接:\\Users\\xiaoj\Desktop\screenshot\云视搜索企业\环球万国.png")

            #点击搜索出来的企业
            driver.find_elements_by_id("com.yunlu6.stone:id/iv_logo")[0].click()
            sleep(1)
            driver.save_screenshot("C地址拼接:\\Users\\xiaoj\Desktop\screenshot\云视搜索企业\环球万国名片页.png")
            driver.quit()

        except Exception as e:
            driver.save_screenshot("C地址拼接:\\Users\\xiaoj\Desktop\screenshot\云视搜索企业\exception.png")
            log_file='C地址拼接:\\Users\\xiaoj\Desktop\exceptionLog\log005.txt'
            logging.basicConfig(filename=log_file,level=logging.DEBUG)
            driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(YUNLU)
    unittest.TextTestRunner(verbosity=2).run(suite)
