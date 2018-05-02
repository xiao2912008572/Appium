from YunluFramework_API.public.common.datainfo import DataInfo


class Excel:
    def __init__(self, xls, sheet_name):
        # .创建excel操作对象
        self.d = DataInfo(path=xls)

        # 获取表单行数
        self.len = self.d.get_rows(sheet_name=sheet_name)

        # 初始化表单名
        self.sheet_name = sheet_name

        # 4.创建DataInfo操作对象
        self.data_info = DataInfo(path='data_api.xls')

    """
        统计接口测试用例描述信息次数(此处为接口名称)
    """

    def excel_data(self, description):
        '''
        统计接口测试用例描述信息次数
        :param description:
        :return:
        '''
        api_description_flag = 0
        row_no = 0

        for i in range(2, self.len + 1):
            # 1.接口描述
            api_description = str(
                self.d.cell(sheet_name=self.sheet_name, rowno=i, colno=2))

            # 2.记录接口描述次数
            if api_description == description:
                api_description_flag += 1

                # 当描述第一次被找到的时候，记录当前行数
                if api_description_flag == 1:
                    row_no = i
                else:
                    pass

        return [api_description_flag, row_no]

    """
        获取：测试数据 和 预期结果
    """

    def get_data(self, description):
        '''
        获取测试数据 和 预期结果
        :param description ：描述信息
        :return:
        '''
        # 1.申明列表
        list = []

        # 2.存描述次数
        description_row_no = self.excel_data(description)
        flag = description_row_no[0]  # 循环控制次数
        row_no = description_row_no[1]  # 从第几行开始读数据

        # 如果符合条件的只有1次
        if flag == 1:
            data = self.d.cell(
                sheet_name=self.sheet_name, rowno=row_no, colno=7)
            hope_result = self.d.cell(
                sheet_name=self.sheet_name, rowno=row_no, colno=9)
            list1 = [data, hope_result]
            list.append(list1)
            return list

        # 如果符合条件的>1次
        elif flag > 1:
            for i in range(row_no, row_no + flag):
                # 测试数据
                data = self.d.cell(
                    sheet_name=self.sheet_name, rowno=i, colno=7)  # a:字符串

                # 预期结果
                hope_result = self.d.cell(
                    sheet_name=self.sheet_name, rowno=i, colno=9)  # a:字符串
                list1 = [data, hope_result]

                # 进入列表
                list.append(list1)

                # list.append(eval(a)) #将a转换成字典
                # list.append((a))  # 将a转换成字典
            return list

        # 以上情况均不符
        else:
            list.append(None)
            return list

    """
        将测试结果写入excel表中
    """

    def write_cell(self, description, sheet_no, col, str):
        '''
        将结果写入excel表中
        :param result : 测试结果
        :return:
        '''
        description_row_no = self.excel_data(description)
        flag = description_row_no[0]  # 循环写入次数
        row_no1 = description_row_no[1]  # 从第几行开始写

        for i in range(0, flag):
            self.d.write_Excel(
                sheet_no=sheet_no, row=row_no1 + i, col=col, str=str)

    """
        获取excel中某行数据
    """

    def get_row_data(self, sheet_name):
        len = self.data_info.get_rows(sheet_name=sheet_name)
        list_row = []

        # len = 10
        for i in range(2, len + 1):
            row_data = self.data_info.row(sheet_name=sheet_name, rowno=i)

            # 201804010 11:11AM改动
            api_no = (row_data[0])

            api_name = row_data[1]
            api_describe = row_data[2]
            api_url = row_data[3]
            api_function = row_data[4]
            api_headers = row_data[5]
            api_data = row_data[6]
            api_check = row_data[7]
            api_hope = row_data[8]
            api_reality = row_data[9]
            api_active = row_data[10]
            api_status = int(row_data[11])
            api_correlation = row_data[12]
            api_message = row_data[13]

            list_2 = [
                api_no, api_name, api_describe, api_url, api_function,
                api_headers, api_data, api_check, api_hope, api_reality,
                api_active, api_status, api_correlation, api_message
            ]
            list_row.append(list_2)
        return list_row
