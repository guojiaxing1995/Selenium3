""" 
@Time    : 2018/10/14 9:04
@Author  : 郭家兴
@Email   : 302802003@qq.com
@File    : read_ini.py
@Desc    :读取配置文件类
"""
import configparser

class ReadIni():
    def __init__(self,path):
        self.read_ini = configparser.ConfigParser()
        self.read_ini.read(path,encoding="utf-8-sig")

    def get_value(self,section,option):
        try:
            return self.read_ini.get(section, option)
        except:
            return None





