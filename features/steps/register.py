""" 
@Time    : 2018/10/19 20:01
@Author  : 郭家兴
@Email   : 302802003@qq.com
@File    : register.py
@Desc    :
"""
import os
from time import sleep

from behave import *

from lib.get_by_local import GetByLocal
from lib.read_ini import ReadIni

use_step_matcher('parse')


@given('selenium driver')
def step_register1(context):
    print("1")

@when('I open the register website')
def step_register2(context):
    context.driver.get("http://www.5itest.cn/register")
    sleep(15)

@then('I expect that the title is "注册"')
def step_register3(context):
    pass


@when('I input username {user_name}')
def step_register4(context,user_name):
    userName = context.get_local_by.get_element('register_element','userName')
    userName.send_keys(user_name)


@when('I input password {pass_word}')
def step_register5(context,pass_word):
    pass

@then('I except that text "成功"')
def step_register6(context):
    print(context.text)