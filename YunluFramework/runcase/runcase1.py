__author__ = 'xiaoj'
import time
import sys

# sys.path.append("C:\Program Files (x86)\Jenkins\workspace\jenkins_github_test1\\")

from YunluFramework.public.common.HTMLTestRunner import HTMLTestRunner
from YunluFramework.config.globalparam import GlobalParam
from YunluFramework.public.common.sendmail import SendMail
from YunluFramework.public.common.choosesuite import SuiteController
from YunluFramework.public.common.log import Log

# 控制用例跑的次数，死循环，可人工干预退出
if __name__ == '__main__':
    # 1.配置日志模块
    cf = GlobalParam('config', 'path_file.conf')
    logfile = cf.getParam('log', "logfile")  # 日志文件名
    logger = Log(logfile)

    # 2.创建控制器对象
    SC = SuiteController()

    # 3.选择测试用例
    suiteA = SC.chooseSuite(3, 7, 'ALL')  # 所有用例
    a = 1

    # 4.循环控制测试用例(跑多少遍)
    while a != 5:
        # a = a + 1
        # ------------------------------测试报告模块----------------------------------
        # 4.1记录日志-开始
        logger.info('{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{START:RUNCASSE1}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}')
        cf = GlobalParam("config", "report.conf")
        path = cf.getParam("report", "path")
        logger.info('报告存储路径：{0}'.format(path))
        timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        filename = path + timestr + ".html"
        logger.info('测试报告名称：{0}'.format(filename))

        # 4.2创建测试报告文档
        fp = open(filename, 'wb')
        runner = HTMLTestRunner(
            stream=fp,
            title='测试结果',
            description='测试报告'
        )
        logger.info('运行测试用例！')
        runner.run(suiteA)
        fp.close()  # 测试报告关闭

        # 4.3发送邮件
        time.sleep(5)
        sendMail = SendMail()
        sendMail.send()

        # 4.4记录日志-结束
        logger.info('{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{END:RUNCASSE1}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}')
        break
