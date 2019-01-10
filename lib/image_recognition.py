""" 
@Time    : 2018/10/14 17:40
@Author  : 郭家兴
@Email   : 302802003@qq.com
@File    : image_recognition.py
@Desc    :
"""
import os
from PIL import Image

from lib.ShowapiRequest import ShowapiRequest
from lib.read_ini import ReadIni


def shot_image(driver,code_element):
    # 获取当前目录
    current_dir = os.path.dirname(__file__)
    # 获取当前目录的父级目录
    parent_dir = os.path.dirname(current_dir)
    driver.save_screenshot((parent_dir + '/img/recognition/'+ driver.capabilities['browserName'] + '.png'))
    left = code_element.location['x']
    top = code_element.location['y']
    right = code_element.size['width'] + left
    height = code_element.size['height'] + top
    img = Image.open(parent_dir + '/img/recognition/'+ driver.capabilities['browserName'] + '.png')
    img = img.crop((left, top, right, height))
    w,h = img.size
    if h<48:
        img = img.resize((w,48),Image.ANTIALIAS)
    img.save(parent_dir + '/img/recognition/'+ driver.capabilities['browserName'] + '.png')

def recognition_show_api(path):
    """调用showApi进行图像识别"""
    # 获取当前目录
    current_dir = os.path.dirname(__file__)
    # 获取当前目录的父级目录
    parent_dir = os.path.dirname(current_dir)
    read_ini = ReadIni(parent_dir + r'/config/baseConfig.ini')
    url = read_ini.get_value('showApi', 'url')
    my_appId = read_ini.get_value('showApi', 'my_appId')
    my_appSecret = read_ini.get_value('showApi', 'my_appSecret')
    typeId = read_ini.get_value('showApi', 'typeId')
    convert_to_jpg = read_ini.get_value('showApi', 'convert_to_jpg')
    r = ShowapiRequest(url, my_appId, my_appSecret)
    r.addBodyPara("typeId", typeId)
    r.addBodyPara("convert_to_jpg", convert_to_jpg)
    r.addFilePara("image", path) #文件上传时设置
    res = r.post()
    try:
        code_num = res.json()['showapi_res_body']['Result']
    except Exception:
        code_num = ''
    return code_num



