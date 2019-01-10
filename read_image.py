""" 
@Time    : 2018/10/10 21:30
@Author  : 郭家兴
@Email   : 302802003@qq.com
@File    : read_image.py
@Desc    :
"""
# import pytesseract
# from PIL import Image
#
# image = Image.open("D:/imc.png")
#
# text = pytesseract.image_to_string(image)
#
# print(text)

import unittest
from ddt import ddt,data,file_data,unpack

@ddt
class Test(unittest.TestCase):

    @file_data(r'D:\a.yaml')
    def test_001(self,value):
        a,b,c = value
        print(a+b+c)


unittest.main()