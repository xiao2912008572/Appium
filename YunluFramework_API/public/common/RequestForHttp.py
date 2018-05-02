# Author:Xiaojingyuan
import json
from YunluFramework_API.public.common.Handle import Handle
import requests
import time


# 用于处理请求的Get和Post方法
class RequestForHttp(Handle):
    def __init__(self):
        Handle.__init__(self)

    # get请求
    def get_function(self, url, r_data):
        '''
        get请求
        :param url: 接口地址
        :param r_data: 数据
        :return:
        '''
        try:
            if '/api' in url:
                # 0. url拼接
                url = self.url + url

            else:
                url = url

            # 1.发送请求
            with requests.Session() as s:
                r = s.get(url, params=r_data)

            # 2.打印请求状态码
            status = r.status_code

            # 3.打印返回结果
            response = r.text

            try:
                # 4.解码json数据,将json转为字典
                dict_r = json.loads(response)

                # 5.格式化输出json（字典转json）
                # ensure_ascii=False 中文不转码
                json_r = json.dumps(
                    dict_r,
                    sort_keys=True,
                    ensure_ascii=False,
                    indent=4,
                    separators=(',', ': '))
                return [status, json_r]
            
            except Exception:
                return status

        except Exception as err:
            self.log.error("GET请求错误 : %s" % err)
            raise err

    # post请求
    def post_function(self, url, r_data, headers=None):
        '''
        post请求
        :param url: 接口路由
        :param r_data: 数据
        :return:
        '''
        try:
            if '/api' in url:
                # 0. url拼接
                url = self.url + url

            else:
                url = url

            # 1.发送请求
            with requests.Session() as s:
                r = s.post(url, data=r_data, headers=headers)

            # 2.打印请求状态码
            status = r.status_code

            # 3.打印返回结果
            response = r.text

            try:
                # 4.解码json数据,将json转为字典
                dict_r = json.loads(response)

                # 5.格式化输出json
                # ensure_ascii=False 中文不转码
                json_r = json.dumps(
                    dict_r,
                    sort_keys=True,
                    ensure_ascii=False,
                    indent=4,
                    separators=(',', ': '))
                return [status, json_r]
            
            except Exception as e:
                return status

        except Exception as err:
            self.log.error("POST请求错误 : %s" % err)
            raise err

    # delete请求
    def delete_function(self, url, r_data):
        '''
        post请求
        :param url: 接口地址
        :param r_data: 数据
        :return:
        '''
        try:
            if '/api' in url:
                # 0. url拼接
                url = self.url + url

            else:
                url = url

            # 1.发送请求
            with requests.Session() as s:
                r = s.delete(url, data=r_data)

            # 2.打印请求状态码
            status = r.status_code

            # 3.打印返回结果
            response = r.text

            try:
                # 4.解码json数据,将json转为字典
                dict_r = json.loads(response)

                # 5.格式化输出json
                # ensure_ascii=False 中文不转码
                json_r = json.dumps(
                    dict_r,
                    sort_keys=True,
                    ensure_ascii=False,
                    indent=4,
                    separators=(',', ': '))
                return [status, json_r]

            except Exception as e:
                return status

        except Exception as err:
            self.log.error("DELETE请求错误 : %s" % err)
            raise err

    # put请求
    def put_function(self, url, r_data):
        '''
        put请求
        :param url: 接口地址
        :param r_data: 数据
        :return:
        '''
        try:
            if '/api' in url:
                # 0. url拼接
                url = self.url + url

            else:
                url = url

            # 1.发送请求
            with requests.Session() as s:
                r = s.put(url, data=r_data)

            # 2.打印请求状态码
            status = r.status_code

            # 3.打印返回结果
            response = r.text

            try:
                # 4.解码json数据,将json转为字典
                dict_r = json.loads(response)

                # 5.格式化输出json
                # ensure_ascii=False 中文不转码
                json_r = json.dumps(
                    dict_r,
                    sort_keys=True,
                    ensure_ascii=False,
                    indent=4,
                    separators=(',', ': '))
                return [status, json_r]

            except Exception as e:
                return status

        except Exception as err:
            self.log.error("PUT请求错误 : %s" % err)
            raise err


# data = {
#     'token': '3888f2c8717f50b7a7f47e2371c1cbf2',
#     'number': '121750866140321'
# }
# req = RequestForHttp()
# response = req.put_function(url='/api/v1/order_forms/121750866140321/cancel', r_data=data)
# print(response)
