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

        #unicodeKeyboard是使用unicode编码方式发送字符串
        # desired_caps['unicodeKeyboard'] = True
        #resetKeyboard是将键盘隐藏起来
        # desired_caps['resetKeyboard'] = True

        #初始化appium连接
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        sleep(2)
        createContactButton = None
        try:
            sleep(2)
            driver.save_screenshot("C地址拼接:\\Users\\xiaoj\Desktop\screenshot\云视产品搜索\main.png")
            #点击云视产品入口
            createContactButton = driver.find_element_by_id("com.yunlu6.stone:id/cloundview_rl_bottom_product")
            createContactButton.click()
            sleep(2)
            driver.save_screenshot("C地址拼接:\\Users\\xiaoj\Desktop\screenshot\云视产品搜索\product.png")
            sleep(1)

            #点击搜索框，输入西班牙米黄
            createContactButton = driver.find_element_by_id("com.yunlu6.stone:id/buildstone_search_key")
            createContactButton.click()#点击搜索框
            sleep(1)

            #获取搜索框，并且输入"西班牙米黄"
            sendkey_01 = driver.find_element_by_id("com.yunlu6.stone:id/et_search_key")
            sendkey_01.send_keys(u"西班牙米黄")
            sleep(2)
            driver.save_screenshot("C地址拼接:\\Users\\xiaoj\Desktop\screenshot\云视产品搜索\搜索西班牙米黄.png")
            sleep(2)
            search_button = driver.find_element_by_id("com.yunlu6.stone:id/iv_search")
            search_button.click()
            sleep(2)
            driver.save_screenshot("C地址拼接:\\Users\\xiaoj\Desktop\screenshot\云视产品搜索\搜索结果.png")
            sleep(1)

            #点击搜索结果中的第一个
            img_button = driver.find_elements_by_id("com.yunlu6.stone:id/buildstone_img")[0]
            img_button.click()#点击第一个产品的西班牙米黄
            sleep(1)
            driver.save_screenshot("C地址拼接:\\Users\\xiaoj\Desktop\screenshot\云视产品搜索\第一个西班牙米黄.png")
            sleep(1)

            #点击第一个产品
            # product_detail = driver.find_elements_by_class_name("android.widget.ImageView")[0]
            # product_detail.click()#点击
            driver.tap([(620,1081)],500)
            sleep(1)
            driver.save_screenshot("C地址拼接:\\Users\\xiaoj\Desktop\screenshot\云视产品搜索\产品详情信息.png")
            sleep(1)

            #点击关联信息查看相应关联信息
            createContactButton = driver.find_element_by_id("com.yunlu6.stone:id/tv_right")
            createContactButton.click()
            sleep(1)
            driver.save_screenshot("C地址拼接:\\Users\\xiaoj\Desktop\screenshot\云视产品搜索\关联信息.png")
            sleep(1)

        except Exception as e:
            driver.save_screenshot("C地址拼接:\\Users\\xiaoj\Desktop\screenshot\云视产品搜索\exception.png")
            log_file='C地址拼接:\\Users\\xiaoj\Desktop\exceptionLog\log003.txt'
            logging.basicConfig(filename=log_file,level=logging.DEBUG)
            driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(YUNLU)
    unittest.TextTestRunner(verbosity=2).run(suite)
