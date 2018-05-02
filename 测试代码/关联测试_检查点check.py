# Author:Xiaojingyuan
import re
import json

correlationDict = {}


def analysis_response(correlation, response):
    '''
    用于解析返回值中的数据，将这些数据存入字典中以供使用
    :param response : 接口返回值
    :return:
    '''
    # 如果关联数据不为空
    if correlation != '':
        # 1.处理关联数据(存到列表中)
        _correlation = correlation.replace('\n', '').replace('\r', '').split(';')

        # 2.分解关联数据
        for j in range(len(_correlation)):
            _correlation = _correlation[j].split('=')

            # 3.判断处理后的关联列表长度为2时
            if len(_correlation) == 2:
                if _correlation[1] == '' or not re.search(r'^\[', _correlation[1]) or not re.search(r'\]$', _correlation[1]):
                    # log.error(api_no + ' ' + api_name + ' 关联参数设置有误，请检查[Correlation]字段参数格式是否正确！！！')
                    continue

                # 4.返回结果赋值
                res = response

                # 5.继续处理_correlation
                _correlation = _correlation[1][1:-1].split('][')

                # 6.循环遍历列表的键
                for key in _correlation:
                    try:
                        temp = res[int(key)]
                    except:
                        try:
                            temp = res[key]
                        except:
                            break
                    res = temp
                correlationDict[_correlation[0]] = res
    return correlationDict


def analysis_response1(correlation, response):
    # 标志
    flag = ''

    correlation = correlation.replace('\n', '').replace('\r', '').split(';')
    for j in range(len(correlation)):

        # 判断是否为'='关系
        if '=' in correlation[j]:
            print(correlation[j])

            # 如果 '#len#' 存在
            if '#len#' in correlation[j]:
                print('去除指定的 #len# 字符串 ：',correlation[j].strip('#len#'))
                param = correlation[j].replace('#len#','').split('=')
                print('进入 #len# 的param = ',param)
                flag = '#len#'

            # 如果 '#len#' 不存在
            elif '#len#' not in correlation[j]:
                param = correlation[j].split('=')
                print('没进入 #len# 的param = ',param)
                flag = '='

        # 判断是否为'<>'关系
        elif '<>' in correlation[j]:
            param = correlation[j].split('<>')
            flag = '<>'

        # print('param值 = ')
        # param的值
        # ['${session}', '[session]']
        # ['${token}', '[token]']

        if len(param) == 2:
            if param[1] == '' or not re.search(r'^\[', param[1]) or not re.search(r'\]$', param[1]):
                print(' 关联参数设置有误，请检查[Correlation]字段参数格式是否正确！！！')
                continue
            value = response
            # print('value = ',value)                     #-------------value(返回值)-------------

            a = param[1][1:-1].split('][')
            # print('a = ',a)                              #------------- a -------------
            # 打印a的值
            # a = ['session']
            # a = ['token']

            for key in a:
                # print('key = ',key)                      #-------------key-------------
                # print()
                try:
                    temp = value[int(key)]
                except:
                    try:
                        temp = value[key]
                        # print('temp = ',temp)
                    except:
                        break
                value = temp

            print()
            print('temp----->value = ', value)
            print(type(param[0]))  # str类型 ： excel表中读取的

            # value = str(value)
            # print(type(value))  # int类型 ： 返回值中读取的
            # print('param[0] = ', param[0])

            if flag == '=' :
                print('等于')
                value = str(value)
                print(type(value))  # int类型 ： 返回值中读取的
                print('param[0] = ', param[0])
                assert value == param[0], '值：不等于'
            if flag == '<>':
                value = str(value)
                print(type(value))  # int类型 ： 返回值中读取的
                print('param[0] = ', param[0])
                print('不等于')
                assert value != param[0], '值：等于'
            if flag == '#len#':
                print('取长')
                assert len(value) == int(param[0]),'长度：不等于'


            correlationDict[param[0]] = value
    return correlationDict


correlation = '${cluster_id}=[id];${token}=[token]'
response = {
    'id': 1234,
    'token': '1231sdj345jksnf54jadasf',
}

response2 = {'id': 8429, 'success': 'true','list':[1,2,3]}
api_check2 = '8429=[id];true=[success];false<>[success];3=[#len#list]'
# api_check2 = '3=[#len#list]'

# a = analysis_response1(correlation,response)
# print(a)

b = analysis_response1(api_check2, response2)
print()
print('b = ', b)
