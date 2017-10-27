__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import sys
import os
import unittest
from time import sleep
from appium import webdriver
from StoneAPP.AllTools.Tools import Tools


class YUNLU(unittest.TestCase):
    def test_login(self):
        #连接信息
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['appPackage'] = 'com.yunlu6.stone'
        desired_caps['appActivity'] = '.WelcomeActivity'
        desired_caps['deviceName'] = 'TWGDU16A20000974'
        #初始化appium连接
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        sleep(3)
        createContactButton = None
        try:
            #点击登录按钮
            login_button = driver.find_element_by_id("com.yunlu6.stone:id/main_login")
            login_button.click()

            phonenumber_input = driver.find_element_by_id("com.yunlu6.stone:id/login_et_photo")
            phonenumber_input.send_keys("13027104206")
            sleep(1)

            #获取密码对象
            password_input = driver.find_element_by_id("com.yunlu6.stone:id/login_et_password")
            password_input.send_keys("12345678")
            sleep(2)

            createContactButton = driver.find_element_by_id("com.yunlu6.stone:id/login_btn")
            createContactButton.click()

            sleep(5)
            driver.save_screenshot("login.png")

        except Exception as e:
            driver.save_screenshot("exception.png")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(YUNLU)
    unittest.TextTestRunner(verbosity=2).run(suite)

