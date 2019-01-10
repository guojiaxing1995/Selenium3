""" 
@Time    : 2018/10/14 14:42
@Author  : 郭家兴
@Email   : 302802003@qq.com
@File    : Test_001_register.py
@Desc    :
"""
import os
import unittest

from business.registerBusiness import RegisterBusiness
from lib.fail_screenshot import shot_img
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

class Register(ParameTestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = create_driver(parame)
        cls.register_business = RegisterBusiness(cls.driver)
        # 获取当前目录
        current_dir = os.path.dirname(__file__)
        # 获取当前目录的父级目录
        parent_dir = os.path.dirname(current_dir)
        read_ini = ReadIni(parent_dir + r'/config/baseConfig.ini')
        url = read_ini.get_value('setting', 'url')
        cls.driver.get(url)


    def setUp(self):
        self.imgs = []

    def test_001_register(self):
        log = OperationLog(self.driver)
        log.debug("eeeee")
        self.register_business.register('user_name')
        log.debug("jjjjj")
        self.assertEqual(True,False)
        log.debug("ooooo")




    def tearDown(self):
        for method_name,error in self._outcome.errors:
            if error:
                #截图保存到img文件夹
                shot_img(self.driver)
                #将截图加入报告
                self.imgs.append(self.driver.get_screenshot_as_base64())