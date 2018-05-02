#!/usr/bin/env python
# coding=utf-8

# Todo：接口自动化测试
# Author：归根落叶
# Blog：http://this.ispenn.com

import json
import http.client, mimetypes
from urllib.parse import urlencode
import random
import time
import re
import logging
import os, sys

try:
    import xlrd
except:
    os.system('pip install -U xlrd')
    import xlrd
try:
    from pyDes import *
except ImportError as e:
    os.system('pip install -U pyDes --allow-external pyDes --allow-unverified pyDes')
    from pyDes import *

import hashlib
import base64
import smtplib
from email.mime.text import MIMEText

log_file = os.path.join(os.getcwd(), 'log/liveappapi.log')
log_format = '[%(asctime)s] [%(levelname)s] %(message)s'
logging.basicConfig(format=log_format, filename=log_file, filemode='w', level=logging.DEBUG)
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter(log_format)
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


# 获取并执行测试用例
def runTest(testCaseFile):
    '''
    执行测试用例方法
    :param testCaseFile : 测试用例文件
    :return:
    '''

    # 测试用例文件 = 系统打开传入的测试用例文件路径
    testCaseFile = os.path.join(os.getcwd(), testCaseFile)

    # 如果系统目录中不存在测试用例文件，则打印错误日志：测试用例文件不存在！
    if not os.path.exists(testCaseFile):
        logging.error('测试用例文件不存在！！！')
        sys.exit()

    # 测试用例对象 = xlrd模块打开测试用例文件路径
    testCase = xlrd.open_workbook(testCaseFile)

    # 声明表格对象
    table = testCase.sheet_by_index(0)

    # 错误测试用例集
    errorCase = []

    # 关联字典
    correlationDict = {}

    # 其中内置了四个参数，分别是：
    # ${randomEmail}（随机邮箱地址）
    # ${randomTel}（随机手机号码）
    # ${timestamp}（当前时间戳）
    # ${session}（session#id，默认为None）
    # ${hashPassword}（hash加密密码，明文123456）
    correlationDict['${hashPassword}'] = hash1Encode('123456')
    correlationDict['${session}'] = None

    # 循环遍历:table表格的n行数据
    for i in range(1, table.nrows):

        # ${randomEmail}（随机邮箱地址）
        correlationDict['${randomEmail}'] = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz', 6)) + '@automation.test'

        # ${randomTel}（随机手机号码）
        correlationDict['${randomTel}'] = '186' + str(random.randint(10000000, 99999999))

        # ${timestamp}（当前时间戳）
        correlationDict['${timestamp}'] = int(time.time())

        # 如果第10列的值中的回车和换行替换成空('')之后，不等于YES，那么就跳过继续
        if table.cell(i, 10).value.replace('\n', '').replace('\r', '') != 'Yes':
            continue

        '''
            此处将所有数据的换行和回车都替换成空('')
        '''
        # 编号
        num = str(int(table.cell(i, 0).value)).replace('\n', '').replace('\r', '')
        # 目的
        api_purpose = table.cell(i, 1).value.replace('\n', '').replace('\r', '')
        # 主机地址
        api_host = table.cell(i, 2).value.replace('\n', '').replace('\r', '')
        # 路由
        request_url = table.cell(i, 3).value.replace('\n', '').replace('\r', '')
        # 请求方式
        request_method = table.cell(i, 4).value.replace('\n', '').replace('\r', '')
        # 数据类型
        request_data_type = table.cell(i, 5).value.replace('\n', '').replace('\r', '')
        # 请求数据
        request_data = table.cell(i, 6).value.replace('\n', '').replace('\r', '')
        # 是否加密
        encryption = table.cell(i, 7).value.replace('\n', '').replace('\r', '')
        # 检查点
        check_point = table.cell(i, 8).value
        # 关联(用;分隔数据)
        correlation = table.cell(i, 9).value.replace('\n', '').replace('\r', '').split(';')

        # 循环读取correlationDict中的key值
        '''
            当前
            correlationDict = {
                '${hashPassword}' : hash1Encode('123456'),
                '${session}' : None,
                '${randomEmail}' : ''.join(random.sample('abcdefghijklmnopqrstuvwxyz', 6)) + '@automation.test',
                '${randomTel}' : '186' + str(random.randint(10000000, 99999999)),
                '${timestamp}' : int(time.time())
            }
        '''
        for key in correlationDict:
            # 如果发现路由中存在key，那么就将当前这个key替换成对应的value值
            if request_url.find(key) > 0:
                request_url = request_url.replace(key, str(correlationDict[key]))

        # 如果请求数据类型为表单类型：
        if request_data_type == 'Form':

            # 将请求数据存入dataFile
            dataFile = request_data

            # 如过路径中存在dataFile
            if os.path.exists(dataFile):
                # 打开文件，读取文件数据，按行读取，存入到request_data中
                fopen = open(dataFile, encoding='utf-8')
                request_data = fopen.readline()
                fopen.close()

            for keyword in correlationDict:
                if request_data.find(keyword) > 0:
                    request_data = request_data.replace(keyword, str(correlationDict[keyword]))
            try:
                if encryption == 'MD5':
                    request_data = json.loads(request_data)
                    status, md5 = getMD5(api_host, urlencode(request_data).replace("%27", "%22"))
                    if status != 200:
                        logging.error(num + ' ' + api_purpose + "[ " + str(status) + " ], 获取md5验证码失败！！！")
                        continue
                    request_data = dict(request_data, **{"sign": md5.decode("utf-8")})
                    request_data = urlencode(request_data).replace("%27", "%22")
                elif encryption == 'DES':
                    request_data = json.loads(request_data)
                    request_data = urlencode({'param': encodePostStr(request_data)})
                else:
                    request_data = urlencode(json.loads(request_data))
            except Exception as e:
                logging.error(num + ' ' + api_purpose + ' 请求的数据有误，请检查[Request Data]字段是否是标准的json格式字符串！')
                continue
        elif request_data_type == 'Data':
            dataFile = request_data
            if os.path.exists(dataFile):
                fopen = open(dataFile, encoding='utf-8')
                request_data = fopen.readline()
                fopen.close()
            for keyword in correlationDict:
                if request_data.find(keyword) > 0:
                    request_data = request_data.replace(keyword, str(correlationDict[keyword]))
            request_data = request_data.encode('utf-8')
        elif request_data_type == 'File':
            dataFile = request_data
            if not os.path.exists(dataFile):
                logging.error(num + ' ' + api_purpose + ' 文件路径配置无效，请检查[Request Data]字段配置的文件路径是否存在！！！')
                continue
            fopen = open(dataFile, 'rb')
            data = fopen.read()
            fopen.close()
            request_data = '''
------WebKitFormBoundaryDf9uRfwb8uzv1eNe
Content-Disposition:form-data;name="file";filename="%s"
Content-Type:
Content-Transfer-Encoding:binary

%s
------WebKitFormBoundaryDf9uRfwb8uzv1eNe--
    ''' % (os.path.basename(dataFile), data)
        status, resp = interfaceTest(num, api_purpose, api_host, request_url, request_data, check_point, request_method, request_data_type, correlationDict['${session}'])
        if status != 200:
            errorCase.append((num + ' ' + api_purpose, str(status), 'http://' + api_host + request_url, resp))
            continue

        # 遍历循环关联值
        for j in range(len(correlation)):
            param = correlation[j].split('=')
            if len(param) == 2:
                if param[1] == '' or not re.search(r'^\[', param[1]) or not re.search(r'\]$', param[1]):
                    logging.error(num + ' ' + api_purpose + ' 关联参数设置有误，请检查[Correlation]字段参数格式是否正确！！！')
                    continue
                value = resp
                for key in param[1][1:-1].split(']['):
                    try:
                        temp = value[int(key)]
                    except:
                        try:
                            temp = value[key]
                        except:
                            break
                    value = temp
                correlationDict[param[0]] = value
    return errorCase


# 接口测试
def interfaceTest(num, api_purpose, api_host, request_url, request_data, check_point, request_method, request_data_type, session):
    '''
    接口测试
    :param num                  :   编号
    :param api_purpose          :   目的
    :param api_host             :   主机地址
    :param request_url          :   请求路由
    :param request_data         :   请求数据
    :param check_point          :   检查点
    :param request_method       :   请求方法
    :param request_data_type    :   请求数据类型
    :param session              :   session_id
    :return:
    '''
    # 请求头
    headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'X-Requested-With': 'XMLHttpRequest',
               'Connection': 'keep-alive',
               'Referer': 'http://' + api_host,
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36'}
    # 如果session不为空
    if session is not None:
        # 将Cookie 赋值
        headers['Cookie'] = 'session=' + session

        # 如果请求类型为File，修改头文件内容格式
        if request_data_type == 'File':
            headers['Content-Type'] = 'multipart/form-data;boundary=----WebKitFormBoundaryDf9uRfwb8uzv1eNe;charset=UTF-8'

        # 如果请求类型为Data，修改头文件内容格式
        elif request_data_type == 'Data':
            headers['Content-Type'] = 'text/plain; charset=UTF-8'

    # 创建http客户端链接对象conn
    conn = http.client.HTTPConnection(api_host)
    # 调用POST方法
    if request_method == 'POST':
        conn.request('POST', request_url, request_data, headers=headers)

    # 调用GET方法
    elif request_method == 'GET':
        conn.request('GET', request_url + '?' + request_data, headers=headers)

    # 无方法可调用，报错
    else:
        logging.error(num + ' ' + api_purpose + ' HTTP请求方法错误，请确认[Request Method]字段是否正确！！！')
        return 400, request_method

    # 存返回结果
    response = conn.getresponse()

    # 解析状态码
    status = response.status

    # 读取返回结果数据
    resp = response.read()

    # 如果状态码为200：
    if status == 200:

        # 将读取到的返回结果转码成utf-8
        resp = resp.decode('utf-8')

        # 利用正则表达式，查找检查点是否在str(resp)返回值中
        if re.search(check_point, str(resp)):

            # 如果存在，则打印成功日志信息
            logging.info(num + ' ' + api_purpose + ' 成功, ' + str(status) + ', ' + str(resp))

            # 返回状态码 和 字典类型返回值
            return status, json.loads(resp)

        # 如果不存在，打印错误失败日志信息
        else:
            logging.error(num + ' ' + api_purpose + ' 失败！！！, [ ' + str(status) + ' ], ' + str(resp))
            return 2001, resp

    # 如果状态码部位200：则直接打印错误日志
    else:
        logging.error(num + ' ' + api_purpose + ' 失败！！！, [ ' + str(status) + ' ], ' + str(resp))
        return status, resp.decode('utf-8')


# 获取md5验证码
def getMD5(url, postData):
    headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'X-Requested-With': 'XMLHttpRequest'}
    conn = http.client.HTTPConnection('this.ismyhost.com')
    conn.request('POST', '/get_isignature', postData, headers=headers)
    response = conn.getresponse()
    return response.status, response.read()


# hash1加密
def hash1Encode(codeStr):
    hashobj = hashlib.sha1()
    hashobj.update(codeStr.encode('utf-8'))
    return hashobj.hexdigest()


# DES加密
def desEncode(desStr):
    k = des('secretKEY', padmode=PAD_PKCS5)
    encodeStr = base64.b64encode(k.encrypt(json.dumps(desStr)))
    return encodeStr


# 字典排序
def encodePostStr(postData):
    keyDict = {'key': 'secretKEY'}
    mergeDict = dict(postData, **keyDict)
    mergeDict = sorted(mergeDict.items())
    postStr = ''
    for i in mergeDict:
        postStr = postStr + i[0] + '=' + i[1] + '&'
    postStr = postStr[:-1]
    hashobj = hashlib.sha1()
    hashobj.update(postStr.encode('utf-8'))
    token = hashobj.hexdigest()
    postData['token'] = token
    return desEncode(postData)


# 发送通知邮件
def sendMail(text):
    sender = 'no-reply@myhost.cn'
    receiver = ['penn@myhost.cn']
    mailToCc = ['penn@myhost.cn']
    subject = '[AutomantionTest]接口自动化测试报告通知'
    smtpserver = 'smtp.exmail.qq.com'
    username = 'no-reply@myhost.cn'
    password = 'password'

    msg = MIMEText(text, 'html', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ';'.join(receiver)
    msg['Cc'] = ';'.join(mailToCc)
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver + mailToCc, msg.as_string())
    smtp.quit()


def main():
    errorTest = runTest('TestCase/TestCasePre.xlsx')
    if len(errorTest) > 0:
        html = '<html><body>接口自动化定期扫描，共有 ' + str(
            len(errorTest)) + ' 个异常接口，列表如下：' + '</p><table><tr><th style="width:100px;">接口</th><th style="width:50px;">状态</th><th style="width:200px;">接口地址</th><th>接口返回值</th></tr>'
        for test in errorTest:
            html = html + '<tr><td>' + test[0] + '</td><td>' + test[1] + '</td><td>' + test[2] + '</td><td>' + test[3] + '</td></tr>'
        html = html + '</table></body></html>'
        # sendMail(html)


if __name__ == '__main__':
    main()
