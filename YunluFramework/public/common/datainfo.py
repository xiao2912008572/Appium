import xlrd
import os
import mysql.connector
from YunluFramework.config.globalparam import GlobalParam
import configparser


class DataInfo():
    def __init__(self, path):
        '''
        :param path: 传入xls文档名称，例如space.xls
        '''
        # 项目目录
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        # 数据data目录文件拼接
        base_dir = base_dir + "/data/" + path
        # 创建工作薄：用于操作excel表格形式数据
        self.workbook = xlrd.open_workbook(base_dir)

    # --------------------------------------------Excel表格操作--------------------------------------------
    def read_Data(self, sheet_name):
        '''
        根据表单名来获取表单对象
        :param sheet_name:表单名称
        :return:表单对象
        '''
        sheet_obj = self.workbook.sheet_by_name(sheet_name)
        return sheet_obj

    def row(self, sheet_name, rowno):
        '''
        改写行，输入1就返回第一行
        :param sheet_name: 表单名
        :param rowno: 行数
        :return:获取第一行的值，列表形式返回['A',"B','C',...]
        '''
        sheet_obj = self.workbook.sheet_by_name(sheet_name)
        rowno = rowno - 1
        return sheet_obj.row_values(rowno)

    def col(self, sheet_name, colno):
        '''
        改写列，输入1就返回第一列
        :param sheet_name: 表单名
        :param colno:列数
        :return:获取第一列的值，列表形式返回['A',"B','C',...]
        '''
        sheet_obj = self.workbook.sheet_by_name(sheet_name)
        colno = colno - 1
        return sheet_obj.row_values(colno)

    def cell(self, sheet_name, rowno, colno):
        '''
        改写行列，输入(1,1)就返回(1,1)的数据
        :param sheet_name:表单名
        :param rowno:行数
        :param colno:列数
        :return: 返回某个坐标行列的值
        '''
        sheet_obj = self.workbook.sheet_by_name(sheet_name)
        rowno = rowno - 1
        colno = colno - 1
        return sheet_obj.cell_value(rowno, colno)


class DataMysql:
    def __init__(self):
        # 读取数据库连接信息
        # 1.项目目录
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        # 2.数据库配置文件
        self.config = base_dir + "/config/sqlserver.conf"
        # 3.读取配置信息
        cf = configparser.ConfigParser()
        cf.read(self.config)
        sections_01 = cf.sections()[0]
        self.connectinfo = eval(cf.get(sections_01, "config"))

    # --------------------------------------------数据库操作--------------------------------------------
    def connect(self):
        '''
        建立数据库连接
        :return:返回数据库连接对象
        '''
        try:
            cnn = mysql.connector.connect(**self.connectinfo)
            # print('mysql连接对象是cnn', cnn)
            return cnn
        except mysql.connector.Error as e:
            print('CONNECT MYSQL FAILS!:{0}'.format(e))

    def select(self, sql, index):
        '''
        数据库查询
        :param sql: 查询语句
        :param index:查询结果索引
        :return:查询结果
        '''
        # 1.申请连接对象
        cnn = self.connect()
        # 2.创建游标
        cursor = cnn.cursor()
        # 3.利用游标执行查询语句
        cursor.execute(sql)
        # sql_select_table = "select * from test1_1创建机构空间_002"
        # print(cursor.fetchone())
        # 4.记录结果
        result = cursor.fetchall()
        return list(result[index])
