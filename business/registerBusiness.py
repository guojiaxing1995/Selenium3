""" 
@Time    : 2018/10/14 14:35
@Author  : 郭家兴
@Email   : 302802003@qq.com
@File    : registerBusiness.py
@Desc    :
"""
from page.registerPage import RegisterPage
from TestCase import ParameTestCase

class RegisterBusiness:
    def __init__(self,driver):
        self.driver = driver
        self.register_page = RegisterPage(self.driver)

    def register(self,user_name):
        self.register_page.input_userName(user_name)
        self.register_page.get_code_num()
        ParameTestCase.log("调用日志")