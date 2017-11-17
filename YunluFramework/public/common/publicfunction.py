__author__ = 'xiaoj'
import time
import shutil  # 强制删除
import os
import logging


class Tools:
    # 初始化传参,传入driver
    def __init__(self, driver):
        self.driver = driver

    # -----------------------------------上下左右滑动功能-------------------------------
    # 获取屏幕大小
    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    # 向左滑动
    def swipeLeft(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.9)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.1)
        self.driver.swipe(x1, y1, x2, y1, t)

    # 向右滑动
    def swipeRight(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.25)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.75)
        self.driver.swipe(x1, y1, x2, y1, t)

    # 向上滑动
    def swipeUp(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.8)
        y2 = int(l[1] * 0.4)
        self.driver.swipe(x1, y1, x1, y2, t)
        time.sleep(5)

    # 向下滑动
    def swipeDown(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.25)
        y2 = int(l[1] * 0.75)
        self.driver.swipe(x1, y1, x1, y2, t)

    # ------------------------------带时间戳的截图功能-------------------------------
    def getTime(self):
        tamp = time.strftime('%H%M%S', time.localtime())  # 时分秒
        return tamp

    # 截图功能
    def getScreenShot(self, screen_path, filename):
        timeA = self.getTime()
        filename = screen_path + filename
        filename = filename + '%s.png' % timeA
        # self.driver.implicitly_wait(2)
        time.sleep(1)  # 截图之前自动等待1秒
        self.driver.get_screenshot_as_file(filename)

    # -----------------------------强制删除文件夹再覆盖截图---------------------------
    def coverUpdate(self, log_path, screen_path, ):
        # 强制删除文件夹
        shutil.rmtree(log_path)
        # shutil.rmtree('C地址拼接:/Users/xiaoj/Desktop/exceptionLog/')
        shutil.rmtree(screen_path)

        # 重新创建文件夹
        os.mkdir(log_path)
        # os.mkdir('C地址拼接:/Users/xiaoj/Desktop/exceptionLog/')
        os.mkdir(screen_path)

    # -----------------------------不带时间戳日志打印功能---------------------------
    # def getLog(self,filename):
    #     timeA = self.getTime()
    #     # self.filename = filename + '%s.txt'%timeA
    #     logging.basicConfig(level=logging.INFO,filename=filename,encoding = "UTF-8",
    #                 format='%(asctime)s - ''levelname:%(levelname)s filename: %(filename)s '
    #                        'outputNumber: [%(lineno)d]  thread: %(threadName)s output msg:  %(message)s'
    #                        , datefmt='[%d/%b/%Y %H:%M:%S]',
    #                 )

    def getLog(self, filename):
        timeA = self.getTime()
        # self.filename = filename + '%s.txt'%timeA
        logging.basicConfig(level=logging.INFO, filename=filename, encoding="UTF-8",
                            format='[%(asctime)s-%(filename)s]-%(levelname)s:%(message)s',
                            )

    # -----------------------------解析读取日志中的字段---------------------------
    def find_word(self, filename, word):
        flag = False
        # filename = self.filename#套用上面的file
        with open(filename, 'r') as f:
            for l in f.readlines():
                if word in l:
                    # print(word+"is found@!!!")
                    flag = True
                    break
        return flag

    # -----------------------------坐标获取元素通用版本---------------------------
    def click_element_by_coordinate(self, x, y):
        # 通过传入绝对坐标，做成相对于屏幕分辨率的方式获取
        # 以1080/1920分辨率作为标准输出————三星A7
        # 1. 标准分辨率
        standard_x = 1080
        standard_y = 1920
        # 1. 算X轴和Y轴相对坐标率
        scale_x = self.getSize()[0] / standard_x
        scale_y = self.getSize()[1] / standard_y
        # 2. 将真实坐标转换成相对坐标
        adjust_x = (x * scale_x)
        adjust_y = (y * scale_y)
        # 3. 点击
        return self.driver.tap([(adjust_x, adjust_y)], duration=500)


'''
    #查找元素，没找到滑动
    def findLocal(self):
        x = 1
        while x ==1:
            if self.fact() ==1:
                self.swipeUp(2000)
                time.sleep(3)
                self.fact()
            else:
                print("找到了")
                x = 2

    #递归
    def fact(self):
        n = 1
        try:
            self.driver.find_element_by_id('').click()
        except Exception as e:
            return n

'''
