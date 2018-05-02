# Author:Xiaojingyuan
import re


class Check:
    def __init__(self):
        self.correlationDict = {}

        # 用于解析返回值(response)

    def analysis_check(self, api_check, response):
        '''
        用于解析返回值中的数据，将这些数据存入关联字典中以供使用
        :param response : 接口返回值
        :return:
        '''
        # 如果关联数据不为空
        if api_check != '':
            # 1.处理关联数据(存到列表中)
            api_check = api_check.replace('\n', '').replace('\r', '').split(';')

            # 2.分解关联数据
            for j in range(len(api_check)):
                api_check = api_check[j].split('=')

                # 3.判断处理后的关联列表长度为2时
                if len(api_check) == 2:
                    if api_check[1] == '' or not re.search(r'^\[', api_check[1]) or not re.search(r'\]$', api_check[1]):
                        # self.log.error(api_no + ' ' + api_name + ' 关联参数设置有误，请检查[Correlation]字段参数格式是否正确！！！')
                        print('error!!!')
                        continue

                    # 4.返回结果赋值
                    value = response

                    # 5.继续处理api_check
                    a = api_check[1][1:-1].split('][')
                    print(a)
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


                    if 'true' == api_check[0] or 'True' == api_check[0]:
                        api_check[0] = bool(api_check[0])
                        # print(api_check[0])
                        assert api_check[0] == value, '不等于'
                        return
                    else:
                        # print(api_check[0])
                        assert api_check[0] == value, '不等于'

                    # self.api_checkDict[api_check[0]] = value
        # return self.api_checkDict


# response = {"id": 19831, "success": 'true'}
# api_check = 'true=[success]'

response1 = [{"success": 'true'}]
api_check1 = 'true=[0][success]'

response2 = {'id': 8429, 'success': True}
api_check2 = 'True=[success];8429=[id]'

c = Check()
# a = c.analysis_response(correlation=correlation, response=response)
a = c.analysis_check(api_check=api_check2, response=response2)
