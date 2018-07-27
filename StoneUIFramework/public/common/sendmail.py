# coding:utf-8
import os
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from StoneUIFramework.config.globalparam import GlobalParam
from StoneUIFramework.public.common.log import Log

# 1.配置日志记录模块
cf = GlobalParam('config', 'path_file.conf')
logfile = cf.getParam('log', "logfile")  # 日志文件名
logger = Log(logfile)

# 2.配置测试报告的路径
cf = GlobalParam("config", "report.conf")
reportPath = cf.getParam("report", "path")  # 报告存储路径

# 3.配置收发件人
# 3.1收件人信息
recvaddress = ['291008572@qq.com']
# 3.2发件人信息
# 163的用户名和密码
sendaddr_name = ''
sendaddr_pswd = ''


class SendMail:
    def __init__(self, recver=None):
        """接收邮件的人：list or tuple"""
        if recver is None:
            self.sendTo = recvaddress
        else:
            self.sendTo = recver

    def __get_report(self):
        """获取最新测试报告"""
        dirs = os.listdir(reportPath)
        dirs.sort()
        newreportname = dirs[-1]
        print('The new report name: {0}'.format(newreportname))
        return newreportname

    def __take_messages(self):
        """生成邮件的内容，和html报告附件"""
        newreport = self.__get_report()
        self.msg = MIMEMultipart()
        self.msg['Subject'] = '测试报告主题'
        self.msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')

        with open(os.path.join(reportPath, newreport), 'rb') as f:
            mailbody = f.read()
        html = MIMEText(mailbody, _subtype='html', _charset='utf-8')
        self.msg.attach(html)

        # html附件
        att1 = MIMEText(mailbody, 'base64', 'gb2312')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="TestReport.html"'  # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        self.msg.attach(att1)

    def send(self):
        """发送邮件"""
        self.__take_messages()
        self.msg['from'] = sendaddr_name
        try:
            smtp = smtplib.SMTP('smtp.163.com', 25)
            logger.info('与邮件服务器：{0}建立连接'.format('smtp.163.com'))
            smtp.login(sendaddr_name, sendaddr_pswd)
            logger.info('登录邮件服务器，用户名：{0}，密码：{1}'.format(sendaddr_name,sendaddr_pswd))
            smtp.sendmail(self.msg['from'], self.sendTo, self.msg.as_string())
            logger.info('发件人为：{0}'.format(self.msg['from']))
            logger.info('收件人为：{0}'.format(self.sendTo))
            smtp.close()
            logger.info("发送邮件成功")

        except Exception:
            logger.error('发送邮件失败')
            raise


if __name__ == '__main__':
    sendMail = SendMail()
    sendMail.send()
