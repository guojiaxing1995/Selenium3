""" 
@Time    : 2018/10/21 8:53
@Author  : 郭家兴
@Email   : 302802003@qq.com
@File    : get_case_data.py
@Desc    : 获取excel文件中的测试数据
"""
import os

from lib.operation_excel import OperationExcel
from lib.read_ini import ReadIni


class getCaseData():
    def __init__(self):
        # 获取当前目录
        current_dir = os.path.dirname(__file__)
        # 获取当前目录的父级目录
        parent_dir = os.path.dirname(current_dir)
        read_ini = ReadIni(parent_dir + r'/config/baseConfig.ini')
        self.keyWordDataSources = read_ini.get_value('setting','keyWordDataSources')
        if self.keyWordDataSources == 'excel':
            self.table,self.excel = self.open_excel()

    def open_excel(self):
        # 获取当前目录
        current_dir = os.path.dirname(__file__)
        # 获取当前目录的父级目录
        parent_dir = os.path.dirname(current_dir)
        file_name = parent_dir + r'/config/keyword.xls'
        excel = OperationExcel(file_name)
        table = excel.get_table(excel.workbook)

        return table,excel

    def get_case_lines(self):
        """
        获取用例条数
        :return: lines
        """
        lines = self.excel.get_rows(self.table)
        return lines

    def get_run_or_not(self,line):
        """
        获取是否执行
        :return:run_or_not
        """
        run_or_not = self.excel.get_cell_value(self.table,line,2)
        return run_or_not

    def get_action_method(self,line):
        """
        获取元素操作方法
        :param line:
        :return: action_method
        """
        action_method = self.excel.get_cell_value(self.table,line,3)
        return action_method

    def get_action_element(self,line):
        """
        获取操作的元素
        :param line:
        :return: element
        """
        element = self.excel.get_cell_value(self.table,line,4)
        return element

    def get_input_data(self,line):
        """
        获取输入数据
        :param line:
        :return: input_data
        """
        input_data = self.excel.get_cell_value(self.table,line,5)
        return input_data

    def get_except_element(self,line):
        """
        获取预期元素
        :param line:
        :return: except_element
        """
        except_element = self.excel.get_cell_value(self.table,line,6)
        return except_element

    def get_except_result(self,line):
        """
        获取预期结果
        :param line:
        :return: except_result
        """
        except_result = self.excel.get_cell_value(self.table,line,7)
        return except_result

    def get_case_id(self,line):
        """
        获取用例编号
        :param line:
        :return: case_id
        """
        case_id = self.excel.get_cell_value(self.table,line,0)
        return case_id

    def write_actual_result(self,line,value):
        """
        将实际结果写回数据源
        :param line:
        :param value:
        :return:
        """
        # 获取当前目录
        current_dir = os.path.dirname(__file__)
        # 获取当前目录的父级目录
        parent_dir = os.path.dirname(current_dir)
        file_name = parent_dir + r'/config/keyword.xls'
        excel = OperationExcel(file_name)
        self.excel.write_execel(excel.workbook,0,line,8,value)
