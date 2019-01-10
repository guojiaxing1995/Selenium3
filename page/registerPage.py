""" 
@Time    : 2018/10/14 11:22
@Author  : 郭家兴
@Email   : 302802003@qq.com
@File    : registerPage.py
@Desc    :
"""
from lib.get_by_local import GetByLocal


class RegisterPage:
    def __init__(self,driver):
        self.driver = driver
        self.getByLocal = GetByLocal(self.driver)

    def get_userName_element(self):
        """
        获取注册页面用户名输入框
        """
        return self.getByLocal.get_element('register_element','userName')

    def get_identifying_code(self):
        """
       获取验证码图片element
        """
        return self.getByLocal.get_element('register_element','identifying_code')