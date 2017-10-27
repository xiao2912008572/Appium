__author__ = 'xiaoj'
# -*- coding: utf-8 -*-

import unittest
from time import sleep
import logging
from StoneAPP.Connect import Connect
from StoneAPP.AllTools.Tools import Tools
from StoneAPP.AllTools.Config import Config




#使用已登录的账号进行浏览产品
class yunku_GongSi(unittest.TestCase):
    def test_gongsi(self):
        cnn = Connect()
        driver = cnn.connect()
        tools = Tools(driver)#tools工具

        cf = Config()
        screen_path = cf.get_PATH('yunku',"path_003")#通过配置文件获取截图的路径
        log_path = cf.get_PATH('yunku','log_003')#通过配置文件获取日志的路径

        try:
            tools.coverUpdate(screen_path)#覆盖更新日志,覆盖更新截图
            tools.getLog(log_path)#打印日志
            sleep(1)
            #点击进入云库界面
            driver.find_element_by_id("com.yunlu6.stone:id/navi_item_work_cloundlibrary").click()
            sleep(1)
            tools.getScreenShot(screen_path,'main')#截main图

            #右上角下拉框
            driver.find_element_by_id("com.yunlu6.stone:id/iv_right_search_cloundlibrary").click()
            sleep(1)
            #点击"+文件"
            driver.find_element_by_id("com.yunlu6.stone:id/btn_pop_cloundlibrary_fragement_upload").click()

            #选择相册方式添加1张照片
            driver.find_element_by_id("com.yunlu6.stone:id/pop_cloundlibrary_tv_album").click()#点击相册
            sleep(1)
            driver.find_elements_by_id("com.yunlu6.stone:id/item_cloudlibrary_ll_checked")[2].click()#点击第四章照片
            driver.find_element_by_id("com.yunlu6.stone:id/title_tv_edit_menu_tv").click()#点击完成

            #当上传图片加载中提示框消失后，再进行截图操作
            # if not driver.find_element_by_id("com.yunlu6.stone:id/ll_loading").is_displayed():
            if driver.find_element_by_id("com.yunlu6.stone:id/gridview").is_displayed():
                sleep(10)

            tools.getScreenShot(screen_path,'上传后云库检查')#截图
            #点击批量操作，选择第一张照片
            driver.find_elements_by_id("com.yunlu6.stone:id/cloudlibrary_image_item")[0].click()#选择第一张照片
            driver.find_element_by_id("com.yunlu6.stone:id/title_main_tv_more_menu").click()#点击下拉框
            driver.find_element_by_id("com.yunlu6.stone:id/btn_new_space").click()#点击分类

            #点击分类到
            sleep(1)
            driver.save_screenshot("C地址拼接:\\Users\\xiaoj\Desktop\screenshot\云库分类公司档\分类到页面检查.png")
            driver.find_element_by_name("xjy机构").click()#选择分类到xjy机构
            driver.find_element_by_name("公司档").click()#选择分类到文件库
            driver.find_element_by_id("com.yunlu6.stone:id/title_tv_menu").click()#点击"√"按钮
            sleep(1)
            tools.getScreenShot(screen_path,'分类后云库检查')#截图

            #检查xjy机构的文件库是否有刚才传过来的图片
             #1.选择空间列表
            driver.find_element_by_id("com.yunlu6.stone:id/navi_item_zone").click()
             #2.选择"xjy机构"
            driver.find_element_by_name("xjy机构").click()
             #3.点击公司档
            driver.find_element_by_id("com.yunlu6.stone:id/title_main_tv_more_menu").click()
            driver.find_element_by_id("com.yunlu6.stone:id/btn_pop_company_archivies").click()
             #4.点击添加公司档
            driver.find_element_by_id("com.yunlu6.stone:id/title_tv_menu").click()
            #5.点击添加照片，选择文件库
            driver.find_element_by_id("com.yunlu6.stone:id/iv_add").click()
            driver.find_element_by_id("com.yunlu6.stone:id/pop_cloundlibrary_tv_wifi_sync").click()
            sleep(1)
            tools.getScreenShot(screen_path,'文件库检查')#截图
             #6.删除
            logging.info("susscess@@!!!!!!")#宣布成功
            driver.quit()#退出

        except Exception as e:
            tools.getScreenShot(screen_path,'exception')#截图
            logging.info("error@@@@!!!!!!")#打印错误的日志
            driver.quit()



