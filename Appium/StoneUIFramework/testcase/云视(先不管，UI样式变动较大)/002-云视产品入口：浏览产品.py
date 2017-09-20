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
        desired_caps['deviceName'] = 'TWGDU16A20000974'
        desired_caps["unicodeKeyboard"] = True
        desired_caps["resetKeyboard"] = True

        #初始化appium连接
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        sleep(3)
        createContactButton = None
        try:
            sleep(3)
            driver.save_screenshot("C地址拼接:\\Users\\xiaoj\Desktop\screenshot\云视产品详情\main.png")
            #点击云视产品入口
            createContactButton = driver.find_element_by_id("com.yunlu6.stone:id/cloundview_rl_bottom_product")
            createContactButton.click()
            sleep(2)
            driver.save_screenshot("C地址拼接:\\Users\\xiaoj\Desktop\screenshot\云视产品详情\product.png")
            driver.swipe(530,1580,530,463)#滑动屏幕从A点到B点
            sleep(2)#等待两秒后保存A-B的截图
            driver.save_screenshot("C地址拼接:\\Users\\xiaoj\Desktop\screenshot\云视产品详情\上下滑动浏览产品截图.png")

            #分别浏览产品界面的各个标签，并且捕获截图
            #把标签列表存在list_tag中，获取它的长度，然后用循环遍历它点击每一个标签
            list_tag = driver.find_elements_by_id("com.yunlu6.stone:id/tag_id")
            createContactButton1 = list_tag[0]
            createContactButton2 = list_tag[1]
            createContactButton1.click()
            sleep(1)
            driver.save_screenshot("C地址拼接:\\Users\\xiaoj\Desktop\screenshot\云视产品详情\第一个标签.png")
            sleep(1)
            createContactButton2.click()
            sleep(1)
            driver.save_screenshot("C地址拼接:\\Users\\xiaoj\Desktop\screenshot\云视产品详情\第二个标签.png")
            sleep(1)
            # for i in range(len(list_tag)):
            #     createContactButton = list_tag[i]
            #     # if i < len(list_tag) -1 :
            #     createContactButton.click()
            #     sleep(1)
            #     driver.save_screenshot("C地址拼接:\\Users\\xiaoj\Desktop\screenshot\云视产品详情\各个标签的截图%d.png"%(i+1))
            #     sleep(1)
                # else:#最后一个标签等待时间要久一点，这样截图才完整
                #     createContactButton.click()
                #     sleep(2)
                #     driver.save_screenshot("C地址拼接:\\Users\\xiaoj\Desktop\screenshot\云视产品详情\各个标签的截图%d.png"%(i+1))
                #     sleep(1)

            #浏览第1个标签下的产品详情，并且捕获截图
            list_tag0 = driver.find_elements_by_id("com.yunlu6.stone:id/tag_id")[0]
            createContactButton = list_tag0
            createContactButton.click()#选中第一个标签

            #获取产品图片列表的第一个产品图片
            product_01 = driver.find_elements_by_id("com.yunlu6.stone:id/buildstone_img")[0]
            createContactButton = product_01
            createContactButton.click()
            sleep(1)
            driver.save_screenshot("C地址拼接:\\Users\\xiaoj\Desktop\screenshot\云视产品详情\第一个标签下的第一个产品图片.png")
            sleep(1)

            #点击第一个产品，查看产品详情页
            driver.tap([(718,1375)],500)
            # elments_product = driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.ImageView[1]")
            # elments_product = driver.find_elements_by_id("com.yunlu6.stone:id/iv_productr")
            # elments_product[0].click()
            sleep(2)
            driver.save_screenshot("C地址拼接:\\Users\\xiaoj\Desktop\screenshot\云视产品详情\产品详情页.png")
            sleep(2)

            createContactButton = driver.find_element_by_id("com.yunlu6.stone:id/tv_middle")
            createContactButton.click()
            sleep(1)
            driver.save_screenshot("C地址拼接:\\Users\\xiaoj\Desktop\screenshot\云视产品详情\产品参数.png")
            sleep(1)

            createContactButton = driver.find_element_by_id("com.yunlu6.stone:id/tv_right")
            createContactButton.click()
            sleep(1)
            driver.save_screenshot("C地址拼接:\\Users\\xiaoj\Desktop\screenshot\云视产品详情\关联信息.png")
            sleep(1)

        except Exception as e:
            driver.save_screenshot("C地址拼接:\\Users\\xiaoj\Desktop\screenshot\云视产品详情\exception.png")
            log_file='C地址拼接:\\Users\\xiaoj\Desktop\exceptionLog\log-002.txt'
            logging.basicConfig(filename=log_file,level=logging.DEBUG)
            driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(YUNLU)
    unittest.TextTestRunner(verbosity=2).run(suite)