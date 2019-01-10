""" 
@Time    : 2018/10/14 16:04
@Author  : 郭家兴
@Email   : 302802003@qq.com
@File    : fail_screenshot.py
@Desc    :
"""
import os
import time


def shot_img(driver):
    # 获取当前目录
    current_dir = os.path.dirname(__file__)
    # 获取当前目录的父级目录
    parent_dir = os.path.dirname(current_dir)
    now = time.strftime('%Y-%m-%d-%H_%M_%S')
    if driver.capabilities['browserName'] == 'firefox':
        driver.save_screenshot(
            parent_dir + '/img/firefox/' + now + driver.capabilities['browserName'] + '.png')
    if driver.capabilities['browserName'] == 'chrome':
        driver.save_screenshot(
            parent_dir + '/img/chrome/' + now + driver.capabilities['browserName'] + '.png')
    if driver.capabilities['browserName'] == 'ie':
        driver.save_screenshot(parent_dir + '/img/ie/' + now + driver.capabilities['browserName'] + '.png')
    if driver.capabilities['browserName'] == 'MicrosoftEdge':
        driver.save_screenshot(parent_dir + '/img/edge/' + now + driver.capabilities['browserName'] + '.png')