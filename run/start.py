""" 
@Time    : 2018/10/21 12:53
@Author  : 郭家兴
@Email   : 302802003@qq.com
@File    : start.py
@Desc    :
"""
import os

from KeyWord.runkeyword import RunKeyWord
from lib.read_ini import ReadIni
from run.runddt import RunDDT

if __name__=='__main__':
    # 获取当前目录
    current_dir = os.path.dirname(__file__)
    # 获取当前目录的父级目录
    parent_dir = os.path.dirname(current_dir)
    read_ini = ReadIni(parent_dir + r'/config/baseConfig.ini')
    frameType = read_ini.get_value('setting', 'frameType')
    if frameType == 'keyWord':
        run = RunKeyWord()
        run.run()
    elif frameType == 'ddt':
        run = RunDDT()
        run.run()