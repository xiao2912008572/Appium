# Author:Xiaojingyuan
from YunluFramework_API.public.common.datainfo import DataMysql
from YunluFramework_API.public.common.datainfo import DataInfo
from YunluFramework_API.config.globalparam import GlobalParam
from YunluFramework_API.public.common.log import Log
from YunluFramework_API.public.common.loginfo import LogInfo
from requests.sessions import Session


class Handle:
    def __init__(self):
        # 1.创建数据库操作对象
        self.d = DataMysql()
        self.excel = DataInfo('data_api.xls')

        # 2.创建读取配置信息对象
        self.cf = GlobalParam('config', 'path_file.conf')

        # 3.url-接口地址
        self.url = self.cf.getURL('URL', "url")  # 接口地址

        # 4. 创建session对象
        self.session = Session()

        # 5. 打印日志模块
        self.plog = LogInfo()

        # 6.获取截图路径、日志路径、日志名
        self.logfile = self.cf.getParam('log', "logfile")  # 日志文件名

        # 7.创建日志记录模块
        self.log = Log(self.logfile)

        # 8. 创建session对象
        self.session = Session()
