import xlrd
import os

class DataInfo():
    def __init__(self,path):
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        # base_dir = base_dir + "/data/space.xls"
        base_dir = base_dir + "/data/" + path
        self.workbook = xlrd.open_workbook(base_dir)

    def read_Data(self,sheet_name):#根据表单名来获取表单对象
        sheet_obj = self.workbook.sheet_by_name(sheet_name)
        return sheet_obj

    def row(self,sheet_name,rowno):#改写行，输入1就返回第一行
        sheet_obj = self.workbook.sheet_by_name(sheet_name)
        rowno = rowno -1
        return sheet_obj.row_values(rowno)

    def col(self,sheet_name,colno):#改写列，输入1就返回第一列
        sheet_obj = self.workbook.sheet_by_name(sheet_name)
        colno = colno -1
        return sheet_obj.row_values(colno)

    def cell(self,sheet_name,rowno,colno):#改写行列，输入(1,1)就返回(1,1)的数据
        sheet_obj = self.workbook.sheet_by_name(sheet_name)
        rowno = rowno - 1
        colno = colno - 1
        return sheet_obj.cell_value(rowno,colno)
