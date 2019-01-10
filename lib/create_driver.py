""" 
@Time    : 2018/10/14 16:26
@Author  : 郭家兴
@Email   : 302802003@qq.com
@File    : create_driver.py
@Desc    :
"""
from selenium import webdriver

def create_driver(parame):
    if parame == 'FireFox':
        return webdriver.Firefox()
    if parame == 'Chrome':
        return webdriver.Chrome()
    if parame == 'Edge':
        return webdriver.Edge()
    if parame == 'Ie':
        return webdriver.Ie()