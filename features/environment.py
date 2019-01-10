""" 
@Time    : 2018/10/20 10:30
@Author  : 郭家兴
@Email   : 302802003@qq.com
@File    : environment.py
@Desc    :
"""

# USE: behave -D BEHAVE_DEBUG_ON_ERROR (to enable debug-on-error)
#  USE: behave -D BEHAVE_DEBUG_ON_ERROR=yes (to enable debug-on-error)
#  USE: behave -D BEHAVE_DEBUG_ON_ERROR=no (to disable debug-on-error)
import os

from lib.create_driver import create_driver
from lib.get_by_local import GetByLocal
from lib.read_ini import ReadIni

BEHAVE_DEBUG_ON_ERROR = True
def setup_debug_on_error(userdata):
    global BEHAVE_DEBUG_ON_ERROR
    BEHAVE_DEBUG_ON_ERROR = userdata.getbool("BEHAVE_DEBUG_ON_ERROR")


def before_feature(context,*args):
    pass

def after_feature(context,*args):
    pass

def before_step(context,step,*args):
    if BEHAVE_DEBUG_ON_ERROR and step.status == "failed":
        # -- ENTER DEBUGGER: Zoom in on failure location.
        # NOTE: Use IPython debugger, same for pdb (basic python debugger).
        import ipdb
        ipdb.post_mortem(step.exc_traceback)


def after_step(context,*args):
    pass

def before_scenario(context,*args):
    pass

def after_scenario(context,*args):
    pass

def before_tag(context,*args):
    pass

def after_tag(context,*args):
    pass

def before_all(context):
    # 获取当前目录
    current_dir = os.path.dirname(__file__)
    # 获取当前目录的父级目录
    parent_dir = os.path.dirname(current_dir)
    global base_config
    base_config = ReadIni(parent_dir + r'/config/baseConfig.ini')
    browser = base_config.get_value('setting', 'BDDbrowser')
    context.driver = create_driver(browser)
    context.get_local_by = GetByLocal(context.driver)


def after_all(context,*args):
    pass