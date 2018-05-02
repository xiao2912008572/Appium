# Author:Xiaojingyuan
from YunluFramework_API.api_test import *
from YunluFramework_API.public.common.test_excel import Excel
import re
import json


class API_REQUEST(Login):
    def __init__(self, sheet_name):
        Handle.__init__(self)
        # 1.sheet_name
        self.sheet_name = sheet_name

        # 2.token
        self.token = self.get_token()
        self.token1 = self.get_token1()

        # 3. 创建请求对象
        self.R = RequestForHttp()

        # 4.获取excel中行数据
        self.excel = Excel(xls='data_api.xls', sheet_name=self.sheet_name)
        self.data = self.excel.get_row_data(sheet_name=self.sheet_name)

        # 5.关联字典
        # 关联字典
        self.correlationDict = {}
        self.checkDict = {}

        # 其中内置了四个参数，分别是：
        # ${token}（token令牌值）
        # ${randomTel}（随机手机号码）
        # ${timestamp}（当前时间戳）
        # ${session}（session#id，默认为None）
        # ${hashPassword}（hash加密密码，明文123456）

        self.correlationDict['${self.token}'] = self.token
        self.correlationDict['${self.token1}'] = self.token1
        self.correlationDict['${space_name}'] = 'api测试'

    def print_log(self, api_no, api_name, api_describe, api_url, api_function,
                  api_headers, api_data, api_check, api_status, api_hope,
                  response):
        '''
        打印日志模块
        :param api_no       : 接口编号
        :param api_name     : 接口名称
        :param api_describe : 接口描述
        :param api_url      : 接口地址
        :param api_function : 接口方法
        :param api_headers  : 接口头部
        :param api_data     : 接口数据
        :param api_check    : 接口检查
        :param api_hope     : 接口预期
        :param response     : 接口返回
        :return:
        '''
        self.log.info('1. 接口编号 : {0}'.format(api_no))
        self.log.info('2. 接口名称 : {0}'.format(api_name))
        self.log.info('3. 接口描述 : {0}'.format(api_describe))
        self.log.info('4. 接口路由 : {0}'.format(api_url))
        self.log.info('5. 接口方式 : {0}'.format(api_function))
        self.log.info('6. 接口头部 : {0}'.format(api_headers))
        self.log.info('7. 接口数据 : {0}'.format(api_data))
        self.log.info('8. 接口检查 : {0}'.format(api_check))
        self.log.info('9. 预期状态 ：{0}'.format(api_status))
        self.log.info('10.接口预期 : {0}'.format(api_hope))
        if api_status == 204:
            self.log.info('11.接口返回 : {0}'.format(response[1]))
        else:
            self.log.info('11.接口返回 : {0}'.format(response[1]))

    def api_method(self, method, api_url, data, api_headers):
        '''
        请求方式选择器
        :param method       : 请求方式
        :param api_url      : 接口路由
        :param data         : 请求数据
        :param api_headers  : 请求头
        :return:
        '''
        if method == 'GET':
            response = self.R.get_function(api_url, data)
            return response

        elif method == 'POST':
            response = self.R.post_function(api_url, data, api_headers)
            return response

        elif method == 'DELETE':
            response = self.R.delete_function(api_url, data)
            return response

        elif method == 'PUT':
            response = self.R.put_function(api_url, data)
            return response

        else:
            pass

    ''' 
        通用的接口请求方法,返回接口的response值
    '''

    def api_requests(self, api_no, api_name, api_describe, api_url,
                     api_function, api_headers, api_data, api_check, api_hope,
                     api_status, api_correlation, api_messages):
        '''
        公用请求方法
        :param api_no       : 接口编号
        :param api_name     : 接口名称
        :param api_describe : 接口描述
        :param api_url      : 接口地址
        :param api_function : 接口方法
        :param api_headers  : 接口头部
        :param api_data     : 接口数据
        :param api_check    : 接口检查
        :param api_hope     : 接口预期
        :return             : 接口返回 response[0] - 状态码 | response[1] - 返回值
        '''
        # 0 解析请求头，如果为json类型，将str类型的headers转换成字典类型
        if api_headers == "{'Content-Type':'application/json'}":
            # 1）将header转换成字典格式
            api_headers = eval(api_headers)

            # 2）直接将api_data转换成json格式
            self.data = self.analysis_data(api_data)
            self.data = json.dumps(self.data)

            # 3）解析url
            api_url = self.analysis_url(api_url)

        # 1 如果api_headers为空
        if api_headers == '':
            # 1.解析data 和 url ———— 将data转为字典格式
            try:
                # 1.1解析测试数据
                self.data = self.analysis_data(api_data)

                # 1.2 解析url
                api_url = self.analysis_url(api_url)

            except Exception as e:
                # 1.1 将请求数据转换成字典
                self.data = api_data
                self.data = eval(self.data)

                # 1.2 解析url
                api_url = self.analysis_url(api_url)
                self.log.error(e)

        # 2. 发送请求
        # 2.1 发送请求
        response = self.api_method(
            method=api_function,
            api_url=api_url,
            data=self.data,
            api_headers=api_headers)

        # 2.2 打印日志
        # 2.1 > 如果状态码不为204
        if api_status != 204:

            # 3. 打印日志
            self.print_log(api_no, api_name, api_describe, api_url,
                           api_function, api_headers, self.data, api_check,
                           api_hope, api_status, response)

            # 4.解析返回值
            status_code = response[0]  # 状态码
            response1 = json.loads(response[1])  # 解析返回值
            self.analysis_response(api_no, api_name, api_correlation,
                                   response1)

            # 5.解析关联消息
            self.analysis_messages(api_no, api_name, api_messages)

            return status_code, response1

        # 2.2 > 如果状态码为204
        elif api_status == 204:

            # 3.解析返回值
            status_code = response  # 状态码

            response1 = ''
            response = [status_code, response1]

            # 4. 打印日志
            self.print_log(api_no, api_name, api_describe, api_url,
                           api_function, api_headers, self.data, api_check,
                           api_hope, api_status, response)

            # 5.解析关联消息
            self.analysis_messages(api_no, api_name, api_messages)

            # return status_code, response1
            return response

        # # 2. 发送请求
        # # 2.1 > 如果状态码不为204
        # if api_status != 204:
        #
        #     # 2. 发送请求
        #     response = self.api_method(method=api_function, api_url=api_url, data=data, api_headers=api_headers)
        #
        #     # 3. 打印日志
        #     self.print_log(api_no, api_name, api_describe, api_url, api_function, api_headers,
        #                    data, api_check, api_hope, api_status, response)
        #
        #     # 4.解析返回值
        #     status_code = response[0]  # 状态码
        #     response1 = json.loads(response[1])  # 解析返回值
        #     self.analysis_response(api_no, api_name, api_correlation, response1)
        #
        #     # 5.解析关联消息
        #     self.analysis_messages(api_no, api_name, api_messages)
        #
        #     return status_code, response1
        #
        # # 2.2 > 如果状态码为204，返回结果为【no content】
        # elif api_status == 204:
        #
        #     # 2.发送请求
        #     response = self.api_method(method=api_function, api_url=api_url, data=data, api_headers=api_headers)
        #
        #     # 3.解析返回值
        #     status_code = response  # 状态码
        #     response1 = ''
        #     response = [status_code, response1]
        #
        #     # 4. 打印日志
        #     self.print_log(api_no, api_name, api_describe, api_url, api_function, api_headers,
        #                    data, api_check, api_hope, api_status, response)
        #
        #     # 5.解析关联消息
        #     self.analysis_messages(api_no, api_name, api_messages)
        #
        #     return status_code, response1

    '''
        用于解析返回值中的数据和请求数据中的关联项
    '''

    # 用于解析请求地址(api_data)
    def analysis_url(self, api_url):
        '''
        用于解析url地址
        :param api_url : 接口路由
        :return:
        '''
        # 1.替换api_data中的关联项
        for k in self.correlationDict:
            if (api_url.find(k)) > 0:
                # 此处将id team_id等参数获取到后转换成str类型
                api_url = api_url.replace(k, str(self.correlationDict[k]))
        return api_url

    # 用于解析请求数据(api_data)
    def analysis_data(self, api_data):
        '''
        用于解析关联数据，将需要关联的字段存到关联字典中
        :param api_data : 接口请求数据
        :return:
        '''
        # 1.请求数据：字符串转字典
        dic_api_data = eval(api_data)

        # 2.循环遍历测试数据
        for k in dict(dic_api_data):
            for key in self.correlationDict:
                if dic_api_data[k] == key:
                    dic_api_data[k] = self.correlationDict[key]
        return dic_api_data

    # 用于解析返回值(response)
    def analysis_response(self, api_no, api_name, correlation, response):
        '''
        用于解析返回值中的数据，将这些数据存入关联字典中以供使用
        :param response : 接口返回值
        :return:
        '''
        # 如果关联数据不为空
        if correlation != '':
            # 1.处理关联数据(存到列表中)
            correlation = correlation.replace('\n', '').replace('\r',
                                                                '').split(';')

            # 2.分解关联数据
            for j in range(len(correlation)):
                param = correlation[j].split('=')

                # 3.判断处理后的关联列表长度为2时
                if len(param) == 2:
                    if param[1] == '' or not re.search(
                            r'^\[', param[1]) or not re.search(
                                r'\]$', param[1]):
                        self.log.error(
                            api_no + ' ' + api_name +
                            ' 关联参数设置有误，请检查[Correlation]字段参数格式是否正确！！！')
                        continue

                    # 4.返回结果赋值
                    value = response

                    # 5.继续处理correlation
                    a = param[1][1:-1].split('][')

                    # 6.循环遍历列表的键
                    for key in a:
                        try:
                            temp = value[int(key)]
                        except:
                            try:
                                temp = value[key]
                            except:
                                break
                        value = temp
                    self.correlationDict[param[0]] = value
        return self.correlationDict

    # 用于解析检查点
    def analysis_check(self, api_no, api_name, api_check, response):
        '''
        用于检查点的校验
        :param response : 接口返回值
        :return:
        '''
        # 标志符
        flag = ''

        # 如果检查数据不为空
        if api_check != '':
            # 1.处理关联数据(存到列表中)
            api_check = api_check.replace('\n', '').replace('\r',
                                                            '').split(';')

            # 2.分解关联数据
            for j in range(len(api_check)):

                # 判断是否为'='关系
                if '=' in api_check[j]:

                    # 如果 '#len#' 存在
                    if '#len#' in api_check[j]:
                        flag = '#len#'

                    # 如果 '#len#'不存在
                    elif '#len#' not in api_check[j]:
                        param = api_check[j].split('=')
                        flag = '='

                # 判断是否为'<>'关系
                elif '<>' in api_check[j]:
                    param = api_check[j].split('<>')
                    flag = '<>'

                # 3.判断处理后的关联列表长度为2时
                if len(param) == 2:
                    if param[1] == '' or not re.search(
                            r'^\[', param[1]) or not re.search(
                                r'\]$', param[1]):
                        self.log.error(api_no + ' ' + api_name +
                                       ' 关联参数设置有误，请检查[Check]字段参数格式是否正确！！！')
                        continue

                    # 4.返回结果赋值
                    value = response
                    # 5.继续处理api_check
                    a = param[1][1:-1].split('][')

                    # 6.循环遍历列表的键
                    for key in a:
                        try:
                            temp = value[int(key)]
                        except:
                            try:
                                temp = value[key]
                            except:
                                break
                        value = temp

                    # 替换检查点中的关联数据
                    # self.log.debug('self.correlationDict = {0}'.format(
                    #     self.correlationDict))
                    for k in self.correlationDict:
                        if param[0] == k:
                            self.log.debug('param[0] = {0}'.format(param[0]))

                            param[0] = self.correlationDict[k]
                            self.log.debug('字典关键字为:{0}'.format(k))

                            self.log.debug('param[0] = {0}'.format(param[0]))

                try:
                    self.log.debug('----------进入检查点数据校验-------------')
                    # print("----------进入检查点数据校验-------------")
                    self.log.debug('flag = {0}'.format(flag))
                    # 检查点数据校验
                    # '='关系断言
                    if flag == '=':
                        self.log.debug('进入等于')

                        self.log.debug('进入等于阶段后的---->param[0] = {0}'.format(
                            param[0]))

                        self.log.debug(
                            '进入等于阶段后的---->type(param[0]) 值 = {0}'.format(
                                type(param[0])))

                        self.log.debug(
                            '进入等于阶段后的---->value 值 = {0}'.format(value))

                        self.log.debug(
                            '进入等于阶段后的---->type(value) 值 = {0}'.format(
                                type(value)))

                        # 如果返回值解析结果value值是数值，先将check中解析出来的param[0]的值转为int再断言
                        if type(value) == int:
                            self.log.debug('进入if')

                            assert int(param[0]) == value

                            self.log.debug('true | value = {0}'.format(value))

                            # 20180410 10:36加入
                            # return [True, value]

                        elif type(value) == float:
                            self.log.debug('进入elif1')

                            assert float(param[0]) == value

                            self.log.debug('true | value = {0}'.format(value))

                        # 将value值中的True或False的类型转换成str类型，再与param[0]断言
                        # 先判断传进来的parma[0]的类型是否为str类型，如果是才能和'True'/'False'比较
                        elif param[0] == 'True' or param[0] == 'False':
                            self.log.debug('进入elif2')

                            value = str(value)

                            assert param[0] == value

                            self.log.debug('true | value = {0}'.format(value))

                            # 20180410 10:36加入
                            # return [True, value]

                        # 无需转换时，直接比较检查点
                        else:
                            self.log.debug('进入else')

                            self.log.debug('param[0] = {0}'.format(param[0]))

                            self.log.debug('value = {0}'.format(value))

                            assert param[0] == value

                            self.log.debug('true | value = {0}'.format(value))
                            # 20180410 10:36加入
                            # return [True, value]

                    # '<>'关系断言
                    if flag == '<>':
                        self.log.debug('进入不等于')

                        self.log.debug('进入不等于阶段后的---->param[0] = {0}'.format(
                            param[0]))

                        self.log.debug(
                            '进入不等于阶段后的---->type(param[0]) 值 = {0}'.format(
                                type(param[0])))

                        self.log.debug('进入不等于阶段后的---->value 值 = {0}'.format(
                            type(value)))

                        self.log.debug(
                            '进入不等于阶段后的---->type(value) 值 = {0}'.format(
                                type(value)))

                        # 如果返回值解析结果value值是数值，先将check中解析出来的param[0]的值转为int再断言
                        if type(value) == int:
                            self.log.debug('进入if')

                            assert int(param[0]) != value

                            self.log.debug('true | value = {0}'.format(value))

                            # 20180410 10:36加入
                            # return [True, value]

                        elif type(value) == float:
                            self.log.debug('进入elif1')

                            assert float(param[0]) != value

                            self.log.debug('true | value = {0}'.format(value))

                        # 将value值中的True或False的类型转换成str类型，再与param[0]断言
                        # 先判断传进来的parma[0]的类型是否为str类型，如果是才能和'True'/'False'比较
                        elif param[0] == 'True' or param[0] == 'False':
                            self.log.debug('进入elif2')

                            value = str(value)

                            assert param[0] != value
                            self.log.debug('true | value = {0}'.format(value))

                            # 20180410 10:36加入
                            # return [True, value]

                        # 无需转换时，直接比较检查点
                        else:
                            self.log.debug('进入else')

                            self.log.debug('param[0] = {0}'.format(param[0]))

                            self.log.debug('value = {0}'.format(value))

                            assert param[0] != value
                            self.log.debug('true | value = {0}'.format(value))

                    # '#len#'关系断言
                    if flag == '#len#':
                        self.log.debug('进入#len#')
                        self.log.debug('int(parma[0]) = {0}'.format(
                            int(param[0])))
                        self.log.debug('len(value) = {0}'.format(len(value)))

                        assert len(value) == int(param[0])
                        self.log.debug('true | len(value) = {0}'.format(
                            len(value)))

                        # 20180410 10:36加入
                        # return [True, value]

                except Exception as e:
                    self.log.error('进入exception')
                    self.log.error('Exception : {0}'.format(e))
                    self.log.error('false | value = {0}'.format(value))
                    return [False, value]
        return [True, value]

    # 获取leancloud系统消息记录
    def get_Messages_from_leancloud(self):
        import requests
        url = "https://3bxid9fg.api.lncld.net/1.1/rtm/messages/history"

        headers = {
            'X-LC-Id': "3BXiD9Fga5RtswdyrJSFQ3h3-gzGzoHsz",
            'X-LC-Sign':
            "7396816f73bdbcf70281b09dc2c1b3b9,1517046641139,master",
        }
        # 1.发送请求
        with requests.Session() as s:
            response = s.get(url, headers=headers)

        # 2.解析返回内容
        res = response.text

        # 3.转为字典
        dict_r = json.loads(res)

        # 转为json,并格式化输出
        json_r = json.dumps(
            dict_r,
            sort_keys=True,
            ensure_ascii=False,
            indent=4,
            separators=(',', ': '))
        return json_r

    # 获取发送给某个用户的(忽略发送着的身份【system】|【user】)最新一条消息的【data】数据
    def get_first_message(self, to_who):
        # 1.调用消息记录模块,返回消息记录列表
        re1 = self.get_Messages_from_leancloud()
        re1 = json.loads(re1)

        # 2.循环存消息
        messages = []
        for i in re1:
            if i['to'] == to_who:
                messages.append(i)
            else:
                pass
        message_1 = messages[0]

        # 3.解析第一条数据
        dict1 = message_1['data']
        data = dict1 = json.loads(dict1)

        # 4.直接取出id
        # dict1 = dict1['_lcattrs']['id']

        # 5.格式化输出
        # message_1 = json.dumps(message_1, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': '))
        # print(message_1)
        # print(dict1)

        # 6.返回message_1,类型为字典
        return data

    # 解析发给某个用户的最新一条消息的关联数据
    def analysis_messages(self, api_no, api_name, correlation):
        '''
        用于解析返回值中的数据，将这些数据存入关联字典中以供使用
        :return:
        '''
        # 如果关联数据不为空
        if correlation != '':
            # 1.处理关联数据(存到列表中)
            correlation = correlation.replace('\n', '').replace('\r',
                                                                '').split(';')

            # 2.分解关联数据
            for j in range(len(correlation)):
                correlation = correlation[j].split('=')

                # 3.判断处理后的关联列表长度为2时
                if len(correlation) == 2:
                    if correlation[1] == '' or not re.search(
                            r'^\[', correlation[1]) or not re.search(
                                r'\]$', correlation[1]):
                        self.log.error(
                            api_no + ' ' + api_name +
                            ' 关联参数设置有误，请检查[Correlation]字段参数格式是否正确！！！')
                        continue

                    # 4.返回结果赋值
                    '''
                        临时方案，此时推送给的用户id是写死的，token1的用户
                    '''
                    value = self.get_first_message(
                        to_who='d66dcb63-107f-4d30-a632-d97882b7465f')

                    # 5.继续处理correlation
                    a = correlation[1][1:-1].split('][')

                    # 6.循环遍历列表的键
                    for key in a:
                        try:
                            temp = value[int(key)]
                        except:
                            try:
                                temp = value[key]
                            except:
                                break
                        value = temp
                    self.correlationDict[correlation[0]] = value
        return self.correlationDict


# request = API_REQUEST(sheet_name='test2')
# col = '${mes_invite_id}=[_lcattrs][id]'
# a = request.analysis_messages(api_no='1',api_name='消息id',correlation=col)
# print(a)

# re1 = request.get_first_message('d66dcb63-107f-4d30-a632-d97882b7465f')
# print(re1)

# re1 = json.loads(re1)
# to = 'd66dcb63-107f-4d30-a632-d97882b7465f'
# list1 = []
# for i in re1:
#     if i['to'] == to:
#         list1.append(i)
#     else:
#         pass
# list1 = list1[0]
# dict1 = list1['data']
# dict1 = json.loads(dict1)
# dict1 = dict1['_lcattrs']['id']
#
# list1 = json.dumps(list1, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': '))
# print(list1)
# print(dict1)

# excel = Excel(xls='data_api.xls', sheet_name='test2')
# data = excel.get_row_data(sheet_name='test2')
#
# for i in range(0, len(data)):
#     api_no = data[i][0]  # 接口编号
#     api_name = data[i][1]  # 接口名称
#     api_describe = data[i][2]  # 接口描述r
#     api_url = data[i][3]  # 接口路由
#     api_function = data[i][4]  # 接口方法
#     api_headers = data[i][5]  # 接口头部
#     api_data = data[i][6]  # 接口数据
#     api_check = data[i][7]  # 接口检查
#     api_hope = data[i][8]  # 接口预期
#     api_active = data[i][10]  # 接口执行
#     api_status = (data[i][11])  # 预期状态
#     api_correlation = data[i][12]  # 接口关联
#
#     if api_active == 'YES':
#         # 发送请求
#         a = request.api_requests(api_no, api_name, api_describe, api_url, api_function, api_headers,
#                              api_data, api_check, api_hope, api_status, api_correlation)
#     else:
#         pass
