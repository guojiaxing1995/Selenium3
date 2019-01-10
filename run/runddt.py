""" 
@Time    : 2018/10/14 11:02
@Author  : 郭家兴
@Email   : 302802003@qq.com
@File    : start.py
@Desc    :入口文件
"""
import HTMLTestRunner_cn
import multiprocessing
import os
import time
import unittest

from TestCase.Test_001_register import Register
from lib.read_ini import ReadIni


class RunDDT:
    def __init__(self):
        pass

    def creatsuit(self,i):
        test_suite = unittest.TestSuite()
        test_suite.addTest(Register("test_001_register",parames=i))

        return test_suite

    def run_case_creat_report(self,i,title='selenium自动化',description='用例执行情况:',tester=u'自动化测试团队'):
        # 获取当前时间
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        # 定义报告存放路径,确保此路径已存在
        filename = '../report/' + now + i + '_result.html'
        fp = open(filename, 'wb')
        # 设定测试报告相关信息
        runner = HTMLTestRunner_cn.HTMLTestRunner(
            stream=fp,
            title=title,
            description=description+'('+i+')',
            #tester=tester
        )

        runner.run(self.creatsuit(i))
        # 关闭报告文件
        fp.close()

    def run(self):
        threads = []
        # 获取当前目录
        current_dir = os.path.dirname(__file__)
        # 获取当前目录的父级目录
        parent_dir = os.path.dirname(current_dir)
        read_ini = ReadIni(parent_dir + r'/config/baseConfig.ini')
        browser = read_ini.get_value('setting', 'browser')
        for i in browser.split(','):
            t = multiprocessing.Process(target=self.run_case_creat_report, args=(i,))
            threads.append(t)
        for j in threads:
            j.start()

if __name__=='__main__':
    run = RunDDT()
    run.run()