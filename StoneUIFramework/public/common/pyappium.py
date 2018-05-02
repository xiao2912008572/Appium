# coding=utf-8
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import logging

from StoneUIFramework.public.common.log import Log
from StoneUIFramework.config.globalparam import GlobalParam

# 配置日志模块
cf = GlobalParam('config', 'path_file.conf')
logfile = cf.getParam('log', "logfile")  # 日志文件名
logger = Log(logfile)

success = "SUCCESS   "
fail = "FAIL   "


class PyAppium():  # 继承page类
    """
        pyappium framework for the main class, the original
    selenium provided by the method of the two packaging,
    making it easier to use.
    """

    def __init__(self, driver):
        self.driver = driver

    def my_print(self, msg, text=None):
        logging.info(msg)

    def element_isvisible(self, css, secs=10):
        """
        Waiting for an element to display.
        Usage:
        driver.element_wait("id->kw",10)
        visibility_of_element_located: 判断某个元素是否可见.可见代表元素非隐藏，并且元素的宽和高都不等于0
        """
        if "->" not in css:
            raise NameError("Positioning syntax errors, lack of '->'.")

        by = css.split("->")[0].strip()
        value = css.split("->")[1].strip()
        messages = '元素: {0} 在{1}秒内未可见'.format(value, secs)

        try:
            if by == "id":
                WebDriverWait(self.driver, secs).until(EC.visibility_of_element_located((By.ID, value)), messages)
            elif by == "name":
                WebDriverWait(self.driver, secs).until(EC.visibility_of_element_located((By.NAME, value)), messages)
            elif by == "class":
                WebDriverWait(self.driver, secs).until(EC.visibility_of_element_located((By.CLASS_NAME, value)), messages)
            elif by == "link_text":
                WebDriverWait(self.driver, secs).until(EC.visibility_of_element_located((By.LINK_TEXT, value)), messages)
            elif by == "xpath":
                WebDriverWait(self.driver, secs).until(EC.visibility_of_element_located((By.XPATH, value)), messages)
            elif by == "css":
                WebDriverWait(self.driver, secs).until(EC.visibility_of_element_located((By.CSS_SELECTOR, value)), messages)
            else:
                raise NameError("Please enter the correct targeting elements,'id','name','class','link_text','xpaht','css'.")
        except Exception:
            logger.error(messages)

    def element_wait(self, css, secs=5):
        """
        Waiting for an element to display.
        Usage:
        driver.element_wait("id->kw",10)
        presence_of_element_located: 判断某个元素是否被加到了dom树里，并不代表该元素一定可见
        """
        if "->" not in css:
            raise NameError("Positioning syntax errors, lack of '->'.")

        by = css.split("->")[0].strip()
        value = css.split("->")[1].strip()
        messages = '元素: {0} 在{1}秒内未定位到'.format(value, secs)

        try:
            if by == "id":
                WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.ID, value)), messages)
            elif by == "name":
                WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.NAME, value)), messages)
            elif by == "class":
                WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.CLASS_NAME, value)), messages)
            elif by == "link_text":
                WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.LINK_TEXT, value)), messages)
            elif by == "xpath":
                WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.XPATH, value)), messages)
            elif by == "css":
                WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)), messages)
            else:
                raise NameError("Please enter the correct targeting elements,'id','name','class','link_text','xpaht','css'.")
        except Exception:
            logger.error(messages)

    def get_element(self, css, text=''):  # 改写
        """
        Judge element positioning way, and returns the element.

        Usage:
        driver.get_element('id->kw')
        """
        try:
            if "->" not in css:
                raise NameError("Positioning syntax errors, lack of '->'.")

            by = css.split("->")[0].strip()
            self.value_element = css.split("->")[1].strip()

            if by == "id":
                self.element_wait(css)
                element = self.driver.find_element_by_id(self.value_element)
            elif by == "name":
                self.element_wait(css)
                element = self.driver.find_element_by_name(self.value_element)
            elif by == "class":
                self.element_wait(css)
                element = self.driver.find_element_by_class_name(self.value_element)
            elif by == "link_text":
                self.element_wait(css)
                element = self.driver.find_element_by_link_text(self.value_element)
            elif by == "xpath":
                self.element_wait(css)
                element = self.driver.find_element_by_xpath(self.value_element)
            elif by == "css":
                self.element_wait(css)
                element = self.driver.find_element_by_css_selector(self.value_element)
            else:
                raise NameError("Please enter the correct targeting elements,'id','name','class','link_text','xpaht','css'.")
        except Exception:
            logger.error('元素：%s 请求超时,定位失败' % self.value_element)
            assert False, "{0} 定位元素：{1}-失败".format(time.asctime(), text)
        return element

    def get_elements(self, css, text=''):  # 改写
        """
        Judge element positioning way, and returns the element.

        Usage:
        driver.get_element('id->kw')
        """
        try:
            if "->" not in css:
                raise NameError("Positioning syntax errors, lack of '->'.")

            by = css.split("->")[0].strip()
            self.value_elements = css.split("->")[1].strip()

            if by == "id":
                self.element_wait(css)
                element = self.driver.find_elements_by_id(self.value_elements)
            elif by == "name":
                self.element_wait(css)
                element = self.driver.find_elements_by_name(self.value_elements)
            elif by == "class":
                self.element_wait(css)
                element = self.driver.find_elements_by_class_name(self.value_elements)
            elif by == "link_text":
                self.element_wait(css)
                element = self.driver.find_elements_by_link_text(self.value_elements)
            elif by == "xpath":
                self.element_wait(css)
                element = self.driver.find_elements_by_xpath(self.value_elements)
            elif by == "css":
                self.element_wait(css)
                element = self.driver.find_elements_by_css_selector(self.value_elements)
            else:
                raise NameError("Please enter the correct targeting elements,'id','name','class','link_text','xpaht','css'.")
        except Exception:
            logger.error('元素：%s 请求超时,定位失败' % self.value_elements)
            assert False, "{0} 定位元素：{1}-失败".format(time.asctime(), text)
        return element

    def open(self, url):
        """
        open url.

        Usage:
        driver.open("https://www.baidu.com")
        """
        t1 = time.time()
        try:
            self.driver.get(url)
            self.my_print("{0} Navigated to {1}, Spend {2} seconds".format(success, url, time.time() - t1))
        except Exception:
            self.my_print("{0} Unable to load {1}, Spend {2} seconds".format(fail, url, time.time() - t1))
            raise

    def max_window(self):
        """
        Set browser window maximized.

        Usage:
        driver.max_window()
        """
        t1 = time.time()
        self.driver.maximize_window()
        self.my_print("{0} Set browser window maximized, Spend {1} seconds".format(success, time.time() - t1))

    def set_window(self, wide, high):
        """
        Set browser window wide and high.

        Usage:
        driver.set_window(wide,high)
        """
        t1 = time.time()
        self.driver.set_window_size(wide, high)
        self.my_print("{0} Set browser window wide: {1},high: {2}, Spend {3} seconds".format(success,
                                                                                             wide, high, time.time() - t1))

    def type(self, css, text):
        """
        Operation input box.

        Usage:
        driver.type("id->kw","selenium")
        """
        t1 = time.time()
        try:
            self.element_wait(css)
            el = self.get_element(css)
            el.send_keys(text)
            self.my_print("{0} Typed element: <{1}> content: {2}, Spend {3} seconds".format(success,
                                                                                            css, text, time.time() - t1))
        except Exception:
            self.my_print("{0} Unable to type element: <{1}> content: {2}, Spend {3} seconds".format(fail,
                                                                                                     css, text, time.time() - t1))
            raise

    def clear_type(self, css, text):
        """
        Clear and input element.

        Usage:
        driver.clear_type("id->kw","selenium")
        """
        t1 = time.time()
        try:
            self.element_wait(css)
            el = self.get_element(css)
            el.clear()
            el.send_keys(text)
            self.my_print("{0} Clear and type element: <{1}> content: {2}, Spend {3} seconds".format(success,
                                                                                                     css, text, time.time() - t1))
        except Exception:
            self.my_print("{0} Unable to clear and type element: <{1}> content: {2}, Spend {3} seconds".format(fail,
                                                                                                               css, text, time.time() - t1))
            raise

    # def click(self, css):
    #     """
    #     It can click any text / image can be clicked
    #     Connection, check box, radio buttons, and even drop-down box etc..
    #
    #     Usage:
    #     driver.click("id->kw")
    #     """
    #     t1 = time.time()
    #     try:
    #         self.element_wait(css)
    #         el = self.get_element(css)
    #         el.click()
    #         self.my_print("{0} Clicked element: <{1}>, Spend {2} seconds".format(success,css,time.time() - t1))
    #     except Exception:
    #         self.my_print("{0} Unable to click element: <{1}>, Spend {2} seconds".format(fail, css, time.time() - t1))
    #         raise

    def click(self, css):
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.click("id->kw")
        """
        try:
            self.value_click = css[0].split("->")[1].strip()  # 元素id
            self.text_click = css[1]  # 元素text描述
            element = self.get_element(css[0], css[1])  # 元素获取
            element.click()
            self.driver.implicitly_wait(1)  # 智能等待1秒
            # time.sleep(1)#点击事件自动等待1秒
        except Exception as err:
            logger.error('元素：%s 无法点击,点击失败' % self.value_click)
            assert False, "{0} 点击元素：{1}-失败".format(time.asctime(), self.text_click)

    def clicks(self, css, n):
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.click("id->kw")
        """
        try:
            self.value_clicks = css[0].split("->")[1].strip()  # 元素id
            self.text_clicks = css[1]  # 元素text描述
            elements = self.get_elements(css[0], css[1])  # 元素获取
            elements[n].click()
            self.driver.implicitly_wait(1)  # 智能等待1秒
            # time.sleep(1)#点击事件自动等待1秒
        except Exception as err:
            logger.error('元素：%s 无法点击,点击失败' % self.value_clicks)
            assert False, "{0} 点击元素：{1}-失败".format(time.asctime(), self.text_clicks)

    # def clear(self,element):
    #     """
    #     It can click any text / image can be clicked
    #     Connection, check box, radio buttons, and even drop-down box etc..
    #
    #     Usage:
    #     driver.click("id->kw")
    #     """
    #     try :
    #         element.clear()
    #     except Exception as err:
    #         logging.info(u"%s : Clear_Element_Error@@!!!!!!!"%element)
    #         assert False,"CLEAR : %s ELEMENT - FAILED"%element
    def clear(self, css):
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.click("id->kw")
        """
        try:
            self.value_clear = css[0].split("->")[1].strip()  # 元素id
            self.text_clear = css[1]  # 元素text描述
            element = self.get_element(css[0], css[1])  # 元素获取
            element.clear()
            self.driver.implicitly_wait(1)  # 智能等待1秒
            # time.sleep(1)#点击事件自动等待1秒
        except Exception as err:
            logger.error('元素：%s 无法清空,清空失败' % self.value_clear)
            assert False, "{0} 清空元素：{1}-失败".format(time.asctime(), self.value_clear)

    def clears(self, css, n):
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.click("id->kw")
        """
        try:
            self.value_clears = css[0].split("->")[1].strip()  # 元素id
            self.text_clears = css[1]  # 元素text描述
            elements = self.get_elements(css[0], css[1])  # 元素获取
            elements[n].clear()
            self.driver.implicitly_wait(1)  # 智能等待1秒
            # time.sleep(1)#点击事件自动等待1秒
        except Exception as err:
            logger.error('元素：%s 无法清空,清空失败' % self.value_clears)
            assert False, "{0} 清空元素：{1}-失败".format(time.asctime(), self.text_clears)

    def send_keys(self, css, text):
        # try :
        #
        #     element.send_keys(text)
        # except Exception as err:
        #     logging.info(u"%s : SendKeys_Element_Error@@!!!!!!!"%element)
        #     assert False,"SENDKEYS : ELEMENT %s SENDKEYS %s - FAILED"%(element,text)
        try:
            self.value_send = css[0].split("->")[1].strip()  # 元素id
            self.text_send = css[1]  # 元素text描述
            element = self.get_element(css[0], css[1])  # 元素获取
            element.send_keys(text)
            self.driver.implicitly_wait(1)  # 智能等待1秒
            # time.sleep(1)#点击ok
            # 事件自动等待1秒
        except Exception as err:
            logger.error('元素：%s 无法聚焦,发送文本失败' % self.value_send)
            assert False, "{0} 元素：{1}-发送文本失败".format(time.asctime(), self.text_send)

    def sends_keys(self, css, n, text):
        # try :
        #
        #     element.send_keys(text)
        # except Exception as err:
        #     logging.info(u"%s : SendKeys_Element_Error@@!!!!!!!"%element)
        #     assert False,"SENDKEYS : ELEMENT %s SENDKEYS %s - FAILED"%(element,text)
        try:
            self.value_sends = css[0].split("->")[1].strip()  # 元素"id->com.yunlu6.xxxxx"中的com.yunlu6.xxxx
            self.text_sends = css[1]  # 元素text描述
            element = self.get_elements(css[0], css[1])  # 元素获取
            element[n].send_keys(text)
            self.driver.implicitly_wait(1)  # 智能等待1秒
            # time.sleep(1)#点击事件自动等待1秒
        except Exception as err:
            logger.error('元素：%s 无法聚焦,发送文本失败' % self.value_sends)
            assert False, "{0} 元素：{1}-发送文本失败".format(time.asctime(), self.text_sends)

    def right_click(self, css):
        """
        Right click element.

        Usage:
        driver.right_click("id->kw")
        """
        t1 = time.time()
        try:
            self.element_wait(css)
            el = self.get_element(css)
            ActionChains(self.driver).context_click(el).perform()
            self.my_print("{0} Right click element: <{1}>, Spend {2} seconds".format(success, css, time.time() - t1))
        except Exception:
            self.my_print("{0} Unable to right click element: <{1}>, Spend {2} seconds".format(fail, css, time.time() - t1))
            raise

    def move_to_element(self, css):
        """
        Mouse over the element.

        Usage:
        driver.move_to_element("id->kw")
        """
        t1 = time.time()
        try:
            self.element_wait(css)
            el = self.get_element(css)
            ActionChains(self.driver).move_to_element(el).perform()
            self.my_print("{0} Move to element: <{1}>, Spend {2} seconds".format(success, css, time.time() - t1))
        except Exception:
            self.my_print("{0} unable move to element: <{1}>, Spend {2} seconds".format(fail, css, time.time() - t1))
            raise

    def double_click(self, css):
        """
        Double click element.

        Usage:
        driver.double_click("id->kw")
        """
        t1 = time.time()
        try:
            self.element_wait(css)
            el = self.get_element(css)
            ActionChains(self.driver).double_click(el).perform()
            self.my_print("{0} Double click element: <{1}>, Spend {2} seconds".format(success, css, time.time() - t1))
        except Exception:
            self.my_print("{0} Unable to double click element: <{1}>, Spend {2} seconds".format(fail, css, time.time() - t1))
            raise

    def drag_and_drop(self, el_css, ta_css):
        """
        Drags an element a certain distance and then drops it.

        Usage:
        driver.drag_and_drop("id->kw","id->su")
        """
        t1 = time.time()
        try:
            self.element_wait(el_css)
            element = self.get_element(el_css)
            self.element_wait(ta_css)
            target = self.get_element(ta_css)
            ActionChains(self.driver).drag_and_drop(element, target).perform()
            self.my_print("{0} Drag and drop element: <{1}> to element: <{2}>, Spend {3} seconds".format(success,
                                                                                                         el_css, ta_css, time.time() - t1))
        except Exception:
            self.my_print("{0} Unable to drag and drop element: <{1}> to element: <{2}>, Spend {3} seconds".format(fail,
                                                                                                                   el_css, ta_css, time.time() - t1))
            raise

    def click_text(self, text):
        """
        Click the element by the link text

        Usage:
        driver.click_text("新闻")
        """
        t1 = time.time()
        try:
            self.driver.find_element_by_partial_link_text(text).click()
            self.my_print("{0} Click by text content: {1}, Spend {2} seconds".format(success, text, time.time() - t1))
        except Exception:
            self.my_print("{0} Unable to Click by text content: {1}, Spend {2} seconds".format(fail, text, time.time() - t1))
            raise

    def close(self):
        """
        Simulates the user clicking the "close" button in the titlebar of a popup
        window or tab.

        Usage:
        driver.close()
        """
        t1 = time.time()
        self.driver.close()
        self.my_print("{0} Closed current window, Spend {1} seconds".format(success, time.time() - t1))

    def quit(self):
        """
        Quit the driver and close all the windows.

        Usage:
        driver.quit()
        """
        t1 = time.time()
        self.driver.quit()
        self.my_print("{0} Closed all window and quit the driver, Spend {1} seconds".format(success, time.time() - t1))

    def submit(self, css):
        """
        Submit the specified form.

        Usage:
        driver.submit("id->kw")
        """
        t1 = time.time()
        try:
            self.element_wait(css)
            el = self.get_element(css)
            el.submit()
            self.my_print("{0} Submit form args element: <{1}>, Spend {2} seconds".format(success, css, time.time() - t1))
        except Exception:
            self.my_print("{0} Unable to submit form args element: <{1}>, Spend {2} seconds".format(fail, css, time.time() - t1))
            raise

    def F5(self):
        """
        Refresh the current page.

        Usage:
        driver.F5()
        """
        t1 = time
        self.driver.refresh()
        self.my_print("{0} Refresh the current page, Spend {1} seconds".format(success, time.time() - t1))

    def js(self, script):
        """
        Execute JavaScript scripts.

        Usage:
        driver.js("window.scrollTo(200,1000);")
        """
        t1 = time.time()
        try:
            self.driver.execute_script(script)
            self.my_print("{0} Execute javascript scripts: {1}, Spend {2} seconds".format(success, script, time.time() - t1))
        except Exception:
            self.my_print("{0} Unable to execute javascript scripts: {1}, Spend {2} seconds".format(fail,
                                                                                                    script, time.time() - t1))
            raise

    def get_attribute(self, css, attribute):
        """
        Gets the value of an element attribute.

        Usage:
        driver.get_attribute("id->su","href")
        """
        t1 = time.time()
        try:
            el = self.get_element(css)
            attr = el.get_attribute(attribute)
            self.my_print("{0} Get attribute element: <{1}>,attribute: {2}, Spend {3} seconds".format(success,
                                                                                                      css, attribute, time.time() - t1))
            return attr
        except Exception:
            self.my_print("{0} Unable to get attribute element: <{1}>,attribute: {2}, Spend {3} seconds".format(fail,
                                                                                                                css, attribute, time.time() - t1))
            raise

    # def get_text(self, css):
    #     """
    #     Get element text information.
    #
    #     Usage:
    #     driver.get_text("id->kw")
    #     """
    #     t1 = time.time()
    #     try:
    #         self.element_wait(css)
    #         text = self.get_element(css).text
    #         self.my_print("{0} Get element text element: <{1}>, Spend {2} seconds".format(success,css,time.time()-t1))
    #         return text
    #     except Exception:
    #         self.my_print("{0} Unable to get element text element: <{1}>, Spend {2} seconds".format(fail, css, time.time() - t1))
    #         raise

    def get_text(self, css):
        """
        It can click any text / image can be text
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.click("id->kw")
        """
        try:
            self.value_get = css[0].split("->")[1].strip()  # 元素id
            self.text_get = css[1]  # 元素text描述
            element = self.get_element(css[0], css[1])  # 元素获取
            # element.click()
            self.driver.implicitly_wait(1)  # 智能等待1秒
            return element.text
        except Exception as err:
            logger.error('元素：%s 无法获取,获取失败' % self.value_get)
            assert False, "{0} 获取文本：{1}-失败".format(time.asctime(), self.text_get)

    def get_texts(self, css, n):
        """
        It can click any text / image can be text
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.click("id->kw")
        """
        try:
            self.value_gets = css[0].split("->")[1].strip()  # 元素id
            self.text_gets = css[1]  # 元素text描述
            elements = self.get_elements(css[0], css[1])  # 元素获取
            # element.click()
            self.driver.implicitly_wait(1)  # 智能等待1秒
            return elements[n].text
        except Exception as err:
            logger.error('元素：%s 无法获取,获取失败' % self.value_gets)
            assert False, "{0} 获取文本：{1}-失败".format(time.asctime(), self.text_gets)

    def get_title(self):
        """
        Get window title.

        Usage:
        driver.get_title()
        """

        t1 = time.time()
        title = self.driver.title
        self.my_print("{0} Get current window title, Spend {1} seconds".format(success, time.time() - t1))
        return title

    def get_url(self):
        """
        Get the URL address of the current page.

        Usage:
        driver.get_url()
        """
        t1 = time.time()
        url = self.driver.current_url
        self.my_print("{0} Get current window url, Spend {1} seconds".format(success, time.time() - t1))
        return url

    def wait(self, secs):
        """
        Implicitly wait.All elements on the page.

        Usage:
        driver.wait(10)
        """
        t1 = time.time()
        self.driver.implicitly_wait(secs)
        self.my_print("{0} Set wait all element display in {1} seconds, Spend {2} seconds".format(success,
                                                                                                  secs, time.time() - t1))

    def accept_alert(self):
        """
        Accept warning box.

        Usage:
        driver.accept_alert()
        """
        t1 = time.time()
        self.driver.switch_to.alert.accept()
        self.my_print("{0} Accept warning box, Spend {1} seconds".format(success, time.time() - t1))

    def dismiss_alert(self):
        """
        Dismisses the alert available.

        Usage:
        driver.dismiss_alert()
        """
        t1 = time.time()
        self.driver.switch_to.alert.dismiss()
        self.my_print("{0} Dismisses the alert available, Spend {1} seconds".format(success, time.time() - t1))

    def switch_to_frame(self, css):
        """
        Switch to the specified frame.

        Usage:
        driver.switch_to_frame("id->kw")
        """
        t1 = time.time()
        try:
            self.element_wait(css)
            iframe_el = self.get_element(css)
            self.driver.switch_to.frame(iframe_el)
            self.my_print("{0} Switch to frame element: <{1}>, Spend {2} seconds".format(success, css, time.time() - t1))
        except Exception:
            self.my_print("{0} Unable switch to frame element: <{1}>, Spend {2} seconds".format(fail, css, time.time() - t1))
            raise

    def switch_to_frame_out(self):
        """
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.

        Usage:
        driver.switch_to_frame_out()
        """
        t1 = time.time()
        self.driver.switch_to.default_content()
        self.my_print("{0} Switch to frame out, Spend {1} seconds".format(success, time.time() - t1))

    def open_new_window(self, css):
        """
        Open the new window and switch the handle to the newly opened window.

        Usage:
        driver.open_new_window("id->kw")
        """
        t1 = time.time()
        try:
            original_windows = self.driver.current_window_handle
            el = self.get_element(css)
            el.click()
            all_handles = self.driver.window_handles
            for handle in all_handles:
                if handle != original_windows:
                    self.driver.switch_to.window(handle)
            self.my_print("{0} Click element: <{1}> open a new window and swich into, Spend {2} seconds".format(success,
                                                                                                                css, time.time() - t1))
        except Exception:
            self.my_print("{0} Click element: <{1}> open a new window and swich into, Spend {2} seconds".format(fail,
                                                                                                                css, time.time() - t1))
            raise

    def element_exist(self, css):
        """
        judge element is exist,The return result is true or false.

        Usage:
        driver.element_exist("id->kw")
        """
        t1 = time.time()
        try:
            self.element_wait(css)
            self.my_print("{0} Element: <{1}> is exist, Spend {2} seconds".format(success, css, time.time() - t1))
            return True
        except TimeoutException:
            self.my_print("{0} Element: <{1}> is not exist, Spend {2} seconds".format(fail, css, time.time() - t1))
            return False

    def take_screenshot(self, file_path):
        """
        Get the current window screenshot.

        Usage:
        driver.take_screenshot('c:/test.png')
        """
        t1 = time.time()
        try:
            self.driver.get_screenshot_as_file(file_path)
            self.my_print("{0} Get the current window screenshot,path: {1}, Spend {2} seconds".format(success,
                                                                                                      file_path, time.time() - t1))
        except Exception:
            self.my_print("{0} Unable to get the current window screenshot,path: {1}, Spend {2} seconds".format(fail,
                                                                                                                file_path, time.time() - t1))
            raise

    def into_new_window(self):
        """
        Into the new window.

        Usage:
        dirver.into_new_window()
        """
        t1 = time.time()
        try:
            all_handle = self.driver.window_handles
            flag = 0
            while len(all_handle) < 2:
                time.sleep(1)
                all_handle = self.driver.window_handles
                flag += 1
                if flag == 5:
                    break
            self.driver.switch_to.window(all_handle[-1])
            self.my_print("{0} Switch to the new window,new window's url: {1}, Spend {2} seconds".format(success,
                                                                                                         self.driver.current_url, time.time() - t1))
        except Exception:
            self.my_print("{0} Unable switch to the new window, Spend {1} seconds".format(fail, time.time() - t1))
            raise

    def type_and_enter(self, css, text, secs=0.5):
        """
        Operation input box. 1、input message,sleep 0.5s;2、input ENTER.

        Usage:
        driver.type_css_keys('id->kw','beck')
        """
        t1 = time.time()
        try:
            self.element_wait(css)
            ele = self.get_element(css)
            ele.send_keys(text)
            time.sleep(secs)
            ele.send_keys(Keys.ENTER)
            self.my_print("{0} Element <{1}> type content: {2},and sleep {3} seconds,input ENTER key, Spend {4} seconds".format(
                success, css, text, secs, time.time() - t1))
        except Exception:
            self.my_print("{0} Unable element <{1}> type content: {2},and sleep {3} seconds,input ENTER key, Spend {4} seconds".
                          format(fail, css, text, secs, time.time() - t1))
            raise

    def js_click(self, css):
        """
        Input a css selecter,use javascript click element.

        Usage:
        driver.js_click('#buttonid')
        """
        t1 = time.time()
        js_str = "$('{0}').click()".format(css)
        try:
            self.driver.execute_script(js_str)
            self.my_print("{0} Use javascript click element: {1}, Spend {2} seconds".format(success, js_str, time.time() - t1))
        except Exception:
            self.my_print("{0} Unable to use javascript click element: {1}, Spend {2} seconds".format(fail,
                                                                                                      js_str, time.time() - t1))
            raise

#
#     @property
#     def origin_driver(self):
#         """
#         Return the original driver,Can use webdriver API.
#
#         Usage:
#         driver.origin_driver
#         """
#         return self.driver
#
#
# if __name__ == '__main__':
#     driver = PySelenium("chrome")
