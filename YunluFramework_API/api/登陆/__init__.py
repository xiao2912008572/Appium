# Author:Xiaojingyuan
from YunluFramework_API.public.common.datainfo import DataMysql
from YunluFramework_API.public.common.datainfo import DataInfo
import unittest
from YunluFramework_API.public.common.RequestForHttp import RequestForHttp
import ddt
from YunluFramework_API.public.common.log import Log
from YunluFramework_API.config.globalparam import GlobalParam
from requests.sessions import Session
from YunluFramework_API.public.common.loginfo import LogInfo
from YunluFramework_API.public.common.Handle import Handle
import json



'''
******************************************************
1、接口描述
登录接口
2、请求url
http:..127.0.0.1:5000.login
3、请求方法
post
4、请求headers
{
    "Accept": "*.*",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "User-Agent": "python-requests.2.7.0 CPython.2.7.10 Darwin.16.4.0"
}
5、body参数
{
    "password": "123456",
    "username": "admin"
}
6、响应结果
{
    "code": 200,
    "msg": "success"
}
'''
