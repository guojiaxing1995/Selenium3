""" 
@Time    : 2018/10/23 21:33
@Author  : 郭家兴
@Email   : 302802003@qq.com
@File    : operation_mysql.py
@Desc    : 操作mysql
"""
import os

import pymysql

from lib.read_ini import ReadIni


class OperationMysql:
    def __init__(self):
        # 获取当前目录
        current_dir = os.path.dirname(__file__)
        # 获取当前目录的父级目录
        parent_dir = os.path.dirname(current_dir)
        read_ini = ReadIni(parent_dir + r'/config/baseConfig.ini')
        host = read_ini.get_value('mysql','host')
        port = read_ini.get_value('mysql','port')
        user = read_ini.get_value('mysql','user')
        passwd = read_ini.get_value('mysql','passwd')
        db = read_ini.get_value('mysql','db')
        self.conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            passwd=passwd,
            db=db)

    def get_cursor(self):
        self.cursor = self.conn.cursor()
        return self.cursor


