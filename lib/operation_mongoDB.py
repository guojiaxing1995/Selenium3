""" 
@Time    : 2018/10/23 21:41
@Author  : 郭家兴
@Email   : 302802003@qq.com
@File    : operation_mongoDB.py
@Desc    : 操作 mongoDB数据库
"""
import os

import pymongo

from lib.read_ini import ReadIni


class OpreationMongoDB:
    def __init__(self):
        # 获取当前目录
        current_dir = os.path.dirname(__file__)
        # 获取当前目录的父级目录
        parent_dir = os.path.dirname(current_dir)
        read_ini = ReadIni(parent_dir + r'/config/baseConfig.ini')
        client = read_ini.get_value('mongoDB','client')
        self.client = pymongo.MongoClient(client)

    def get_db(self,db):
        """
        传入数据库名称，返回指定数据库对象
        """
        self.my_db= self.client[db]
        return self.my_db

    def get_collection(self,collection):
        """
        传入集合名称，返回指定集合对象
        """
        self.my_collection = self.my_db[collection]
        return self.my_collection