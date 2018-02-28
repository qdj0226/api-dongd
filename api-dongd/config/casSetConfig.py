#-*- coding:utf-8 -*-
__author__ = "dongd"
__datetime__ = r"2018\2\27 0027"
__software__ = "PyCharm"


import os

# 越秀旧改测试用例集路径
yx_jg_web = os.path.abspath(os.path.join(os.path.dirname(__file__),"..","testcases","yx_jg_web"))
lilin_app = os.path.abspath(os.path.join(os.path.dirname(__file__),"..","testcases","lilin_app"))


run = [yx_jg_web,lilin_app]
