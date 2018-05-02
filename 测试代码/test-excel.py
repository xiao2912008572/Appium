from YunluFramework_API.public.common.datainfo import DataInfo
import ddt


class Excel:
    def __init__(self, xls, sheet_name):
        # .创建excel操作对象
        self.d = DataInfo(path=xls)

        # 获取表单行数
        self.len = self.d.get_rows(sheet_name=sheet_name)

        # 初始化表单名
        self.sheet_name = sheet_name

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
            api_description = str(self.d.cell(sheet_name=self.sheet_name, rowno=i, colno=2))

            # 2.记录接口描述次数
            if api_description == description:
                api_description_flag += 1

                # 当描述第一次被找到的时候，记录当前行数
                if api_description_flag == 1:
                    row_no = i
                else:
                    pass

        return [api_description_flag,row_no]

    def get_data(self, description):
        '''
        获取测试数据
        :param description ：描述信息
        :return:
        '''
        # 1.申明列表
        list = []

        # 2.存描述次数
        description_row_no = self.excel_data(description)
        flag = description_row_no[0]
        row_no = description_row_no[1]

        if flag == 1:
            return eval(self.d.cell(sheet_name=self.sheet_name, rowno=row_no, colno=7))

        elif flag > 1:
            for i in range(row_no, row_no + flag):
                a = self.d.cell(sheet_name=self.sheet_name, rowno=i, colno=7)
                list.append(eval(a))
            return list

        else:
            return None


# ex = Excel(xls='data_api.xls', sheet_name='test')
# # a = ex.excel_data(description='Space - 空间列表')
# a = ex.get_data(description='Space - 空间列表')
# print(a)
# b = ex.get_data(description='Space - 空间列表1')
# print(b)
