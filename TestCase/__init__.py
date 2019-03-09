""" 
@Time    : 2018/10/14 8:51
@Author  : 郭家兴
@Email   : 302802003@qq.com
@File    : __init__.py.py
@Desc    :
"""
import time
import unittest
import os
from lib.create_driver import create_driver
from lib.operation_log import OperationLog
from lib.read_ini import ReadIni


class ParameTestCase(unittest.TestCase):
    """
    该类继承unittest  该类的子类可以传参数
    """
    def __init__(self,methodName='runTest',parames=None):
        super(ParameTestCase,self).__init__(methodName)
        global parame
        parame = parames

    @classmethod
    def create_driver(cls):
        """
        实例化driver
        :return:
        """
        cls.driver = create_driver(parame)
        cls.log = OperationLog(cls.driver)

    @classmethod
    def get_url(cls):
        """
        打开测试地址
        :return:
        """
        # 获取当前目录
        current_dir = os.path.dirname(__file__)
        # 获取当前目录的父级目录
        parent_dir = os.path.dirname(current_dir)
        read_ini = ReadIni(parent_dir + r'/config/baseConfig.ini')
        url = read_ini.get_value('setting', 'url')
        cls.driver.get(url)
        cls.driver.implicitly_wait(10)

    @classmethod
    def quit_driver(cls):
        time.sleep(5)
        cls.driver.quit()