""" 
@Time    : 2018/10/14 14:35
@Author  : 郭家兴
@Email   : 302802003@qq.com
@File    : registerBusiness.py
@Desc    :
"""
from handle.registerHandle import RegisterHandle


class RegisterBusiness:
    def __init__(self,driver):
        self.driver = driver
        self.register_handle = RegisterHandle(self.driver)

    def register(self,user_name):
        self.register_handle.input_userName(user_name)
        self.register_handle.get_code_num()