""" 
@Time    : 2018/10/14 9:56
@Author  : 郭家兴
@Email   : 302802003@qq.com
@File    : get_by_local.py
@Desc    : 通过定位方式和配置文件来获取element
"""
import os


from lib.read_ini import ReadIni


class GetByLocal:
    def __init__(self,driver):
        self.driver = driver

    def get_element(self,section,key):
        #获取当前目录
        current_dir = os.path.dirname(__file__)
        #获取当前目录的父级目录
        parent_dir = os.path.dirname(current_dir)
        read_ini = ReadIni(parent_dir+r'/config/LocalElement.ini')
        local = read_ini.get_value(section,key)
        local_by = local.split('>')[0]
        local_value = local.split('>')[1]
        if local_by == 'id':
            return self.driver.find_element_by_id(local_value)
        elif local_by == 'name':
            return self.driver.find_element_by_name(local_value)
        elif local_by == 'className':
            return self.driver.find_element_by_class_name(local_value)
        elif local_by == 'cssSelector':
            return self.driver.find_element_by_css_selector(local_value)
        elif local_by == 'tagName':
            return self.driver.find_element_by_tag_name(local_value)
        elif local_by == 'xpath':
            return self.driver.find_element_by_xpath(local_value)
        elif local_by == 'linkText':
            return self.driver.find_element_by_link_text(local_value)
        elif local_by == 'partialLinkText':
            return self.driver.find_element_by_partial_link_text(local_value)
        else:
            None