""" 
@Time    : 2018/10/21 19:15
@Author  : 郭家兴
@Email   : 302802003@qq.com
@File    : operation_log.py
@Desc    :
"""
import datetime
import logging
import os

from selenium import webdriver

from lib.read_ini import ReadIni


class OperationLog:
    def __init__(self,driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        # 这为清空当前文件的logging 因为logging会包含所有的文件的logging
        logging.Logger.manager.loggerDict.pop(__name__)
        # 将当前文件的handlers 清空
        self.logger.handlers = []
        # 然后再次移除当前文件logging配置
        self.logger.removeHandler(self.logger.handlers)
        if not self.logger.handlers:
            # 获取当前目录
            current_dir = os.path.dirname(__file__)
            # 获取当前目录的父级目录
            parent_dir = os.path.dirname(current_dir)
            read_ini = ReadIni(parent_dir + r'/config/baseConfig.ini')
            log_lever = self.get_log_lever(read_ini)
            #设置日志等级
            self.logger.setLevel(log_lever)
            formatter = logging.Formatter(driver.capabilities['browserName'] +
                ' %(asctime)s %(filename)s--> %(funcName)s %(levelno)s: %(levelname)s ----->%(message)s')
            self.stream_handler = logging.StreamHandler()
            self.stream_handler.setFormatter(formatter)
            self.logger.addHandler(self.stream_handler)

            file_name = parent_dir + r'/log/'+driver.capabilities['browserName']+'/'+datetime.datetime.now().strftime("%Y-%m-%d")+".log"
            self.file_handler = logging.FileHandler(file_name,'a',encoding='utf-8')
            self.file_handler.setFormatter(formatter)
            self.logger.addHandler(self.file_handler)



    def get_log_lever(self,read_ini):
        logLever = read_ini.get_value('setting', 'logLever')
        if logLever == 'INFO':
            return logging.INFO
        if logLever == 'WARNING':
            return logging.WARNING
        if logLever == 'ERROR':
            return logging.ERROR
        if logLever == 'DEBUG':
            return logging.DEBUG
        else:
            return logging.WARN


    def info(self, message=None):
        self.__init__(self.driver)
        self.logger.info(message)

    def debug(self, message=None):
        self.__init__(self.driver)
        self.logger.debug(message)


    def warning(self, message=None):
        self.__init__(self.driver)
        self.logger.warning(message)

    def error(self, message=None):
        self.__init__(self.driver)
        self.logger.error(message)

    def critical(self, message=None):
        self.__init__(self.driver)
        self.logger.critical(message)

# log = OperationLog(webdriver.Chrome())
# log.debug("666")
