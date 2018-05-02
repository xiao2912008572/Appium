from YunluFramework_API.public.common.datainfo import DataInfo

d = DataInfo('data_api.xls')
len = d.get_rows('SPACE')

list = []
for i in range(2, len + 1):
    # 编号
    api_no = int(d.cell(sheet_name='SPACE', rowno=i, colno=1))

    # 接口名称
    api_name = str(d.cell(sheet_name='SPACE', rowno=i, colno=2))

    # 接口描述
    api_description = str(d.cell(sheet_name='SPACE', rowno=i, colno=3))

    # 接口路由
    url = d.cell(sheet_name='SPACE', rowno=i, colno=4)

    # 名称+描述
    description = api_name + ':' + api_description

    # 请求方法
    api_function = d.cell(sheet_name='SPACE', rowno=i, colno=5)

    # 请求头
    api_headers = d.cell(sheet_name='SPACE', rowno=i, colno=6)

    # 请求参数
    api_data = d.cell(sheet_name='SPACE', rowno=i, colno=7)

    # 检查字段
    api_check = d.cell(sheet_name='SPACE', rowno=i, colno=8)

    # 预期结果
    api_hope = d.cell(sheet_name='SPACE', rowno=i, colno=9)

    list1 = [api_no,api_name,description,api_function,api_headers,api_data,api_check,api_hope]

    # print(list1)

    list.append(list1)


    if api_name == 'Space - 空间类型列表（私人空间）':
        print('找到了！',i)
    elif api_name == 'Space - 空间创建（私人空间）':
        print('找到了！',i)

    print(i,api_no, description,url,api_function,api_headers,api_data,api_check,api_hope)


# print(list)
# print(list[11])

