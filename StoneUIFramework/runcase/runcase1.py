__author__ = 'xiaoj'
import unittest
import time
import sys

# sys.path.append("C:\\Users\\xiaoj\PycharmProjects\Appium")
sys.path.append("C:\Program Files (x86)\Jenkins\workspace\jenkins_github_test1\\")
# sys.path.append('/usr/local/StoneUIFramework')
# sys.path.append("/usr/local/Appium")

from StoneUIFramework.public.common.HTMLTestRunner import HTMLTestRunner
from StoneUIFramework.config.globalparam import GlobalParam
from StoneUIFramework.public.common.sendmail import SendMail
from StoneUIFramework.runcase.choosecase import SuiteController

# 控制用例跑的次数，死循环，可人工干预退出
if __name__ == '__main__':
    #1.创建控制器对象
    SC = SuiteController()
    #2.选择测试用例
    suiteA = SC.chooseSuite(1, 1, 'ALL')  # 所有用例
    # unittest.TextTestRunner(verbosity=2).run(suiteA)
    a = 1
    while a != 5:
        # a = a + 1
        # ------------------------------测试报告----------------------------------
        cf = GlobalParam("config", "report.conf")
        path = cf.getParam("report", "path")  # 报告存储路径
        timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))  # 获取时间戳
        filename = path + timestr + ".html"  # 测试报告命名
        fp = open(filename, 'wb')
        runner = HTMLTestRunner(
            stream=fp,
            title='测试结果',
            description='测试报告'
        )
        runner.run(suiteA)
        fp.close()  # 测试报告关闭
        # runner = unittest.TextTestRunner()
        # runner.run(suite)
        # 发送邮件
        time.sleep(5)
        sendMail = SendMail()
        sendMail.send()
        break
