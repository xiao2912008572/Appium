# Author:Xiaojingyuan
import re

# resp = {'token': 'token_12345678', 'session': 'session_id_123456'}
#
# # 配置关联参数
# correlation = '${session}=[session];${token}=[token]'
#
# # 配置关联字典
# correlationDict = {}
#
# # 将关联参数的';'分解
# # correlation =  ['${session}=[message]', '${token}=[token]']
# correlation = correlation.replace('\n', '').replace('\r', '').split(';')
# print('correlation = ', correlation)
#
# # 将第0个关联项目'='分解
# # param =  ['${session}', '[message]']
# param = correlation[0].split('=')
# print('param = ', param)
#
# a = param[1][1:-1].split('][')
# print('a = ',a)

# 配置关联字典
correlationDict = {}

# 关联原始数据
correlation = '${session}=[session];${token}=[token]'

# 处理关联数据(存到列表中)
correlation = correlation.replace('\n', '').replace('\r', '').split(';')

# 返回值
resp = {'token': 'token_12345678', 'session': 'session_id_123456'}
# resp1 = [{'token': 'token_12345678', 'session': 'session_id_123456'}]

for j in range(len(correlation)):
    param = correlation[j].split('=')

    # param的值
    # ['${session}', '[session]']
    # ['${token}', '[token]']

    if len(param) == 2:
        if param[1] == '' or not re.search(r'^\[', param[1]) or not re.search(r'\]$', param[1]):
            print(' 关联参数设置有误，请检查[Correlation]字段参数格式是否正确！！！')
            continue
        value = resp
        print('value = ',value)                     #-------------value(返回值)-------------

        # 打印a的值
        # a = ['session']
        # a = ['token']

        a = param[1][1:-1].split('][')
        print('a = ',a)                              #------------- a -------------

        for key in param[1][1:-1].split(']['):
            print('key = ',key)                      #-------------key-------------
            print()
            try:
                temp = value[int(key)]
            except:
                try:
                    temp = value[key]
                except:
                    break
            value = temp
        correlationDict[param[0]] = value
print()
print('correlationDict = ',correlationDict)
