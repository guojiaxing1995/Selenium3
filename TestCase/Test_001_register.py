""" 
@Time    : 2018/10/14 14:42
@Author  : 郭家兴
@Email   : 302802003@qq.com
@File    : Test_001_register.py
@Desc    :
"""

from TestCase import ParameTestCase
from business.registerBusiness import RegisterBusiness
from lib.fail_screenshot import shot_img
from lib.operation_log import OperationLog



class Register(ParameTestCase):
    @classmethod
    def setUpClass(cls):
        cls.register_business = RegisterBusiness(cls.driver)



    def setUp(self):
        self.imgs = []

    def test_001_register(self):
        self.log.debug("eeeee")
        self.register_business.register('user_name')
        self.log.debug("jjjjj")
        self.assertEqual(True,False)
        self.log.debug("ooooo")




    def tearDown(self):
        for method_name,error in self._outcome.errors:
            if error:
                #截图保存到img文件夹
                shot_img(self.driver)
                #将截图加入报告
                self.imgs.append(self.driver.get_screenshot_as_base64())