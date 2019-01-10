""" 
@Time    : 2018/9/16 10:19
@Author  : 郭家兴
@Email   : 302802003@qq.com
@File    : start_browsers.py
@Desc    :
"""
import time

from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# driver = webdriver.Chrome()
# driver.get("http://www.5itest.cn/register")
# time.sleep(5)
# #driver.set_window_size(1920,1080)
# #driver.maximize_window()
# print(driver.capabilities['browserName'])
# title = EC.title_contains("注册")
# print(title(driver))
# element = driver.find_element_by_class_name("controls")
# #判断元素是否可见
# locator = (By.CLASS_NAME,"controls")
# WebDriverWait(driver,10).until(EC.visibility_of_element_located(locator))
#
# driver.save_screenshot("D:/imc.png")
# code_element = driver.find_element_by_id("getcode_num")
# left = code_element.location['x']
# top = code_element.location['y']
# right = code_element.size['width']+left
# height = code_element.size['height']+top
# img = Image.open("D:/imc.png")
# #img = img.resize((1920,1080),Image.BILINEAR)
# #img.save("D:/imc.png")
# img = img.crop((left,top,right,height))
# img.save("D:/imc1.png")
