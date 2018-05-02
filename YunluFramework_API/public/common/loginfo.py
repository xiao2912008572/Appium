# Author:Xiaojingyuan
from YunluFramework_API.public.common.log import Log
from YunluFramework_API.config.globalparam import GlobalParam
import ddt
from YunluFramework_API.public.common.test_excel import Excel


@ddt.ddt
class LogInfo():
    def __init__(self):
        # 1.创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')

        # 2.获取截图路径、日志路径、日志名
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名

        # 3.创建日志记录模块
        self.log = Log(self.logfile)

        # 4.创建DataInfo操作对象
        self.excel = Excel(xls='data_api.xls', sheet_name='test2')

    def print_log(self, reponse, sheet_name):
        '''
        打印日志模块
        :param data: 请求数据
        :param response: 返回值
        :param describle: 接口描述
        :param url: 接口地址
        :param method: 请求方法
        :param header: 头文件
        :return:
        '''
        data = self.excel.get_row_data(sheet_name=sheet_name)

        for i in range(0, len(data)):
            api_no = data[i][0]
            api_name = data[i][1]
            api_describle = data[i][2]
            api_url = data[i][3]
            api_function = data[i][4]
            api_headers = data[i][5]
            api_data = data[i][6]
            api_check = data[i][7]
            api_hope = data[i][8]

            self.log.info('1.接口编号 : {0}'.format(api_no))
            self.log.info('2.接口名称 : {0}'.format(api_name))
            self.log.info('3.接口描述 : {0}'.format(api_describle))
            self.log.info('4.接口路由 : {0}'.format(api_url))
            self.log.info('5.接口方式 : {0}'.format(api_function))
            self.log.info('6.接口头部 : {0}'.format(api_headers))
            self.log.info('7.接口数据 : {0}'.format(api_data))
            self.log.info('8.接口检查 : {0}'.format(api_check))
            self.log.info('9.接口预期 : {0}'.format(api_hope))
            self.log.info('X.接口返回 : {0}\n'.format(reponse[1]))


# a = LogInfo()
# response = [1, 2, 3]
# data = a.printlog(response,sheet_name='SPACE')
