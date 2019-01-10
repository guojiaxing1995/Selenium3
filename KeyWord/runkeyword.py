""" 
@Time    : 2018/10/21 9:49
@Author  : 郭家兴
@Email   : 302802003@qq.com
@File    : start.py
@Desc    :
"""
import os
from time import sleep

from KeyWord.get_case_data import getCaseData
from lib.create_driver import create_driver
from lib.get_by_local import GetByLocal
from lib.read_ini import ReadIni


class RunKeyWord():
    def __init__(self):
        self.case_data = getCaseData()

    def run(self):
        lines = self.case_data.get_case_lines()
        if self.case_data.keyWordDataSources == 'excel':
            for line in range(1, lines):
                self.execute_one_case(line)

    def execute_one_case(self,line):
        self.action_method(line)
        result = self.fail_or_pass(line)
        self.case_data.write_actual_result(line,result)

    def action_method(self,line):
        method = self.case_data.get_action_method(line)
        input_data = self.case_data.get_input_data(line)
        element = self.case_data.get_action_element(line)
        if method:
            if method == 'open_browser':
                # 获取当前目录
                current_dir = os.path.dirname(__file__)
                # 获取当前目录的父级目录
                parent_dir = os.path.dirname(current_dir)
                base_config = ReadIni(parent_dir + r'/config/baseConfig.ini')
                browser = base_config.get_value('setting', 'keyWordBrowser')
                self.driver = create_driver(browser)
                self.get_local_by = GetByLocal(self.driver)
            if method == 'get_url':
                self.driver.get(input_data)
            if method == 'input':
                e = self.get_local_by.get_element(element.split(',')[0],element.split(',')[1])
                e.send_keys(input_data)
            if method == 'click':
                e = self.get_local_by.get_element(element.split(',')[0], element.split(',')[1])
                e.click()
            if method == 'sleep':
                sleep(input_data)
            if method == 'close_browser':
                self.driver.close()

    def fail_or_pass(self,line):
        except_element = self.case_data.get_except_element(line)
        except_result = self.case_data.get_except_result(line)
        if except_element:
            e = self.get_local_by.get_element(except_element.split(',')[0], except_element.split(',')[1])
            type = except_result.split('=')[0]
            result = except_result.split('=')[1]
            if type == 'text':
                if e.text == result:
                    return True
                else:
                    return False
            else:
                return False

        else:
            return True


