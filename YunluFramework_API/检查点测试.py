import re

# # 用于解析检查点
# def analysis_check(api_no, api_name, api_check, response):
#     '''
#     用于检查点的校验
#     :param response : 接口返回值
#     :return:
#     '''
#     correlationDict = {'${result}': '123'}
#     correlationDict = {'${token}': '5b3e277374854d141b1e894ed0d8ce2c', '${token1}': '6bc91e372785ece0f7ed8e0b1c99e37c', '${space_name}': 'api测试', '${test_team_id}': 5114, '${code_7}': '123390640100137', '${code_15}': '123390640100146', '${code_7_items_id}': 2524, '${code_15_items_id}': 2525, '${code_7_refunds_id}': 78, '${code_15_refunds_id}': 79}

#     # 标志符
#     flag = ''
#     # print("flag标志 = ", flag)

#     # 如果检查数据不为空
#     if api_check != '':
#         # 1.处理关联数据(存到列表中)
#         api_check = api_check.replace('\n', '').replace('\r', '').split(';')
#         # print('api_check = ',api_check)

#         # 2.分解关联数据
#         for j in range(len(api_check)):

#             # 判断是否为'='关系
#             if '=' in api_check[j]:
#                 # print("= 存在于api_check中")

#                 # 如果 '#len#' 存在
#                 if '#len#' in api_check[j]:
#                     # print('去除指定的 #len# 字符串 ：', api_check[j].strip('#len#'))
#                     # param = api_check[j].replace('#len#', '').split('=')
#                     flag = '#len#'
#                     # print("1.flag 等于#len# ：", flag)

#                 # 如果 '#len#'不存在
#                 elif '#len#' not in api_check[j]:
#                     param = api_check[j].split('=')
#                     # print('没进入 #len# 的param = ', param)
#                     flag = '='

#             # 判断是否为'<>'关系
#             elif '<>' in api_check[j]:
#                 param = api_check[j].split('<>')
#                 flag = '<>'
#                 # print("4. flag = <>:", flag)

#             # 3.判断处理后的关联列表长度为2时
#             if len(param) == 2:
#                 if param[1] == '' or not re.search(
#                         r'^\[', param[1]) or not re.search(r'\]$', param[1]):
#                     # .log.error(api_no + ' ' + api_name +
#                     #                 ' 关联参数设置有误，请检查[Check]字段参数格式是否正确！！！')
#                     print('关联参数设置有误，请检查[Check]字段参数格式是否正确！！！')
#                     continue

#                 # 4.返回结果赋值
#                 value = response

#                 # 5.继续处理api_check
#                 a = param[1][1:-1].split('][')
#                 print('a = ',a) # a为['1', 'name'] ['2', 'name'] ['3', 'success'] ['0', 'name']

#                 # 6.循环遍历列表的键
#                 for key in a:
#                     try:
#                         temp = value[int(key)]
#                         print('temp1 = ', temp)#temp1为temp1 =  {'name': '销售主管'} temp1 =  {'name': '销售员'}
#                     except:
#                         try:
#                             temp = value[key]
#                             print('temp = ', temp)#temp为 销售主管 销售员 导购员 true

#                         except:
#                             break
#                     value = temp
#                     print('value = ', value)

#                 print('param[0] = ',param[0])

#                 # 替换检查点中的关联数据
#                 for k in correlationDict:
#                     if param[0] == k:
#                         param[0] = correlationDict[k]
#                         print('k = ',k)
#                         print(param[0])

#             try:
#                 # print("----------进入检查点数据校验-------------")
#                 # print("flag = ", flag)
#                 # 检查点数据校验
#                 # '='关系断言
#                 if flag == '=':
#                     # print('等于')

#                     # 先将value值中的True或False的类型转换成str类型，再与param[0]断言
#                     if param[0] in 'True' or 'False':
#                         value = str(value)
#                         assert param[0] == value
#                         print('---value----:',value)

#                         # 20180410 10:36加入
#                         # return [True, value]
#                         print('true',value)

#                     # 如果返回数据为int型，比较时将excel中的数据先转换成整型数据
#                     elif type(value) == int:
#                         # print('进入elif')
#                         assert int(param[0]) == value

#                         # 20180410 10:36加入
#                         # return [True, value]
#                         print('true',value)

#                     # 无需转换时，直接比较检查点
#                     else:
#                         # print('进入else')
#                         # print('param[0] = ', param[0])
#                         # print('value = ', value)
#                         assert param[0] == value

#                         # 20180410 10:36加入
#                         # return [True, value]
#                         print('true',value)

#                 # '<>'关系断言
#                 if flag == '<>':
#                     # 先将value值中的True或False的类型转换成str类型，再与param[0]断言
#                     if param[0] in 'True' or 'False':
#                         value = str(value)
#                         assert param[0] != value

#                         # 20180410 10:36加入
#                         # return [True, value]
#                         print('true',value)

#                     # 如果返回数据为int型，比较时将excel中的数据先转换成整型数据
#                     elif type(value) == int:
#                         # print('进入elif')
#                         assert int(param[0]) != value

#                         # 20180410 10:36加入
#                         # return [True, value]
#                         print('true',value)

#                     # 无需转换时，直接比较检查点
#                     else:
#                         # print('进入else')
#                         assert param[0] != value

#                         # 20180410 10:36加入
#                         # return [True, value]
#                         print('true',value)

#                 # '#len#'关系断言
#                 if flag == '#len#':
#                     # print('进入#len#')
#                     assert len(value) == int(param[0])

#                     # 20180410 10:36加入
#                     # return [True, value]
#                     print('true',value)

#             except Exception as e:
#                 # print('进入exception')
#                 print('false',value)
#                 return [False, value]
#     return [True ,value]


# 用于解析检查点
def analysis_check(api_no, api_name, api_check, response):
    '''
    用于检查点的校验
    :param response : 接口返回值
    :return:
    '''
    correlationDict = {
        '${self.token}': '5b3e277374854d141b1e894ed0d8ce2c',
        '${self.token1}': '6bc91e372785ece0f7ed8e0b1c99e37c',
        '${space_name}': 'api测试',
        '${test_team_id}': 5114,
        '${code_7}': '123390850472111',
        '${code_15}': '123390850471231',
        '${code_7_items_id}': 2540,
        '${code_15_items_id}': 2541,
        '${code_7_refunds_shdd_id}': 92,
        '${code_15_refunds_shdd_id}': 93,
        '${refund_code_tkbh_7}': '6333908504702370001',
        '${code_item_7_tkcp_id}': 2540
    }

    # 标志符
    flag = ''
    # print("flag标志 = ", flag)

    # 如果检查数据不为空
    if api_check != '':
        # 1.处理关联数据(存到列表中)
        api_check = api_check.replace('\n', '').replace('\r', '').split(';')
        # print('api_check = ',api_check)

        # 2.分解关联数据
        for j in range(len(api_check)):
            print('j = ', j)

            # 判断是否为'='关系
            if '=' in api_check[j]:
                # print("= 存在于api_check中")

                # 如果 '#len#' 存在
                if '#len#' in api_check[j]:
                    # print('去除指定的 #len# 字符串 ：', api_check[j].strip('#len#'))
                    # param = api_check[j].replace('#len#', '').split('=')
                    flag = '#len#'
                    # print("1.flag 等于#len# ：", flag)

                # 如果 '#len#'不存在
                elif '#len#' not in api_check[j]:
                    param = api_check[j].split('=')
                    # print('没进入 #len# 的param = ', param)
                    flag = '='

            # 判断是否为'<>'关系
            elif '<>' in api_check[j]:
                param = api_check[j].split('<>')
                flag = '<>'
                # print("4. flag = <>:", flag)

            # 3.判断处理后的关联列表长度为2时
            if len(param) == 2:
                if param[1] == '' or not re.search(
                        r'^\[', param[1]) or not re.search(r'\]$', param[1]):
                    continue

                # 4.返回结果赋值
                value = response
                # 5.继续处理api_check
                a = param[1][1:-1].split('][')
                # print('a = ',a)

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
                    print('#value# = ', value)

                # 替换检查点中的关联数据
                # print('correlationDict = ', correlationDict)
                for k in correlationDict:
                    if param[0] == k:
                        print('param[0] = ', param[0])
                        param[0] = correlationDict[k]
                        print('k = ', k)
                        print(param[0])

            try:
                print('===========param=============:', param)
                print("----------进入检查点数据校验-------------")
                print("flag = ", flag)
                # 检查点数据校验
                # '='关系断言
                if flag == '=':
                    print('等于')
                    print('进入等于阶段后的---->param[0] = ', param[0])
                    print('进入等于阶段后的---->type(param[0]) 值 = ', type(param[0]))
                    print('进入等于阶段后的---->value 值 = ', value)
                    print('进入等于阶段后的---->type(value) 值 = ', type(value))

                    # 如果返回值解析结果value值是数值，先将check中解析出来的param[0]的值转为int再断言
                    if type(value) == int:
                        print('进入if')
                        assert int(param[0]) == value
                        print('true', value)

                        # 20180410 10:36加入
                        # return [True, value]

                    elif type(value) == float:
                        print('进入elif1')
                        assert float(param[0]) == value
                        print('true', value)

                    # 将value值中的True或False的类型转换成str类型，再与param[0]断言
                    # 先判断传进来的parma[0]的类型是否为str类型，如果是才能和'True'/'False'比较
                    elif param[0] == 'True' or param[0] == 'False':
                        print('进入elif2')
                        value = str(value)

                        assert param[0] == value
                        print('true', value)

                        # 20180410 10:36加入
                        # return [True, value]

                    # 无需转换时，直接比较检查点
                    else:
                        print('进入else')
                        print('param[0] = ', param[0])
                        print('value = ', value)

                        assert param[0] == value
                        print('true', value)

                        # 20180410 10:36加入
                        # return [True, value]

                # '<>'关系断言
                if flag == '<>':

                    print('不等于')
                    print('进入不等于阶段后的---->param[0] = ', param[0])
                    print('进入不等于阶段后的---->type(param[0]) 值 = ', type(param[0]))
                    print('进入不等于阶段后的---->value 值 = ', value)
                    print('进入不等于阶段后的---->type(value) 值 = ', type(value))

                    # 如果返回值解析结果value值是数值，先将check中解析出来的param[0]的值转为int再断言
                    if type(value) == int:
                        print('进入if')
                        assert int(param[0]) != value
                        print('true', value)

                        # 20180410 10:36加入
                        # return [True, value]

                    elif type(value) == float:
                        print('进入elif1')
                        assert float(param[0]) != value
                        print('true', value)

                    # 将value值中的True或False的类型转换成str类型，再与param[0]断言
                    # 先判断传进来的parma[0]的类型是否为str类型，如果是才能和'True'/'False'比较
                    elif param[0] == 'True' or param[0] == 'False':
                        print('进入elif2')
                        value = str(value)

                        assert param[0] != value
                        print('true', value)

                        # 20180410 10:36加入
                        # return [True, value]

                    # 无需转换时，直接比较检查点
                    else:
                        print('进入else')
                        print('param[0] = ', param[0])
                        print('value = ', value)

                        assert param[0] != value
                        print('true', value)

                        # 20180410 10:36加入
                        # return [True, value]
                    # # 先将value值中的True或False的类型转换成str类型，再与param[0]断言
                    # if param[0] in 'True' or 'False':
                    #     value = str(value)

                    #     print('true',value)
                    #     assert param[0] != value

                    #     # 20180410 10:36加入
                    #     # return [True, value]

                    # # 如果返回数据为int型，比较时将excel中的数据先转换成整型数据
                    # elif type(value) == int:
                    # # elif isinstance(value,int):
                    #     # print('进入elif')

                    #     print('true',value)
                    #     assert int(param[0]) != value

                    #     # 20180410 10:36加入
                    #     # return [True, value]

                    # # 无需转换时，直接比较检查点
                    # else:
                    #     # print('进入else')

                    #     print('true',value)
                    #     assert param[0] != value

                    #     # 20180410 10:36加入
                    #     # return [True, value]

                # '#len#'关系断言
                if flag == '#len#':
                    print('进入#len#')
                    print('true', value)
                    assert len(value) == int(param[0])

                    # 20180410 10:36加入
                    # return [True, value]

            except Exception as e:
                print('e = ', e)
                print('进入exception')
                print('false', value)
                return [False, value]
    return [True, value]


api_no = 1
api_name = 'test_1'
api_check = '${result}=[success]'
api_check = '销售主管=[0][name];销售员=[1][name];导购员=[2][name];${result}=[3][success]'
api_check = "1=[refund_orders][amount];神仙=[refund_orders][apply_user];goods=[refund_orders][clazz];7day=[refund_orders][fund_des];${code_7}=[refund_orders][order_form_code];balance=[refund_orders][pay_mode];1=[refund_orders][quantity];7天无理由退货申请=[refund_orders][reason];xjy测试订单卖家版=[refund_orders][seller];canceled=[refund_orders][state];0.02=[refund_orders][middel_fee][amount];0.0=[refund_orders][middel_fee][payment_commisions];0.0=[refund_orders][middel_fee][payment_rate];0.015=[refund_orders][middel_fee][technical_rate];0.015=[refund_orders][middel_fee][technical_service_fee];1.0=[refund_orders][order_item][amount];${code_item_7_tkcp_id}=[refund_orders][order_item][id];7天=[refund_orders][order_item][name];${code_7}=[refund_orders][order_item][order_form_code];1.0=[refund_orders][order_item][original_price];1.0=[refund_orders][order_item][price];55721=[refund_orders][order_item][product_id];1=[refund_orders][order_item][quantity];=[refund_orders][order_item][refund_state_desc];${test_team_id}=[refund_orders][order_item][organization][id];卖家机构=[refund_orders][order_item][organization][name];"
api_check = "1=[refund_orders][amount];神仙=[refund_orders][apply_user]"

# response = [{
#     'name': '销售主管'
# }, {
#     'name': '销售员'
# }, {
#     'name': '导购员'
# }, {
#     'success': '123'
# }]
response = {
    "refund_orders": {
        "amount":
        1.0,
        "apply_user":
        "神仙",
        "clazz":
        "goods",
        "created_at":
        "2018-04-18 14:10:50",
        "express_infos":
        'null',
        "fund_des":
        "7day",
        "fund_files": [{
            "id":
            1234,
            "thumb_url":
            "http://imgprv.yunlu6.com/Fj0dqxVUL2feDU-DbeXBMsny1ZwB-general?e=1524035206&token=3l2F6e3bmg_EkYo8scdTIMyVFZQ9XlZBLiCVIVpt:RcriFxIjmVzHUsSDIu-37F1SQ48=",
            "url":
            "http://imgprv.yunlu6.com/Fj0dqxVUL2feDU-DbeXBMsny1ZwB?e=1524035206&token=3l2F6e3bmg_EkYo8scdTIMyVFZQ9XlZBLiCVIVpt:KcY2VQ-q51lCk39CYV53VbhRufw="
        }],
        "id":
        92,
        "middel_fee": {
            "amount": "0.02",
            "payment_commisions": "0.0",
            "payment_rate": "0.0",
            "technical_rate": "0.015",
            "technical_service_fee": "0.015"
        },
        "order_form_code":
        "123390850472111",
        "order_item": {
            "amount": "1.0",
            "id": 2540,
            "logo": "http://imgpub.yunlu6.com/FufejM2-HeqJD20S6GbI3YJaKEvK",
            "name": "7天",
            "order_form_code": "123390850472111",
            "organization": {
                "id": 5114,
                "logo": "https://www.yunlu6.com/assets/blank.jpg",
                "name": "卖家机构"
            },
            "original_price": "1.0",
            "price": "1.0",
            "product_id": 55721,
            "quantity": 1.0,
            "refund_state_desc": ""
        },
        "pay_mode":
        "balance",
        "quantity":
        1,
        "reason":
        "7天无理由退货申请",
        "refund_code":
        "6333908504702370001",
        "refund_logs": [{
            "act_des": "发起退货申请",
            "created_at": "2018-04-18 14:10:50",
            "name": "神仙"
        }],
        "refuse_apply_des":
        "",
        "refuse_apply_files":
        'null',
        "seller":
        "xjy测试订单卖家版",
        "state":
        "canceled",
        "time_sec":
        1524031850
    }
}

response = {
    "refund_orders": {
        "amount": 1.0,
        "apply_user": "神仙"
    }
}
a = analysis_check(api_no, api_name, api_check, response)
print('a = ', a)
