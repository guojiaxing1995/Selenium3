""" 
@Time    : 2018/10/14 11:33
@Author  : 郭家兴
@Email   : 302802003@qq.com
@File    : registerHandle.py
@Desc    :
"""
from lib.image_recognition import shot_image
from page.registerPage import RegisterPage


class RegisterHandle:
    def __init__(self,driver):
        self.driver = driver
        self.register_page = RegisterPage(driver)

    def input_userName(self,user_name):
        self.register_page.get_userName_element().send_keys(user_name)

    def get_code_num(self):
        code = self.register_page.get_identifying_code()
        shot_image(self.driver,code)