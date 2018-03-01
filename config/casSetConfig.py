#-*- coding:utf-8 -*-
__author__ = "dongd"
__datetime__ = r"2018\2\27 0027"
__software__ = "PyCharm"


import os

# 越秀旧改测试用例集路径
yx_jg_web = os.path.abspath(os.path.join(os.path.dirname(__file__),"..","testcases","yx_jg_web"))
# 立林app测试用例集路径
lilin_app = os.path.abspath(os.path.join(os.path.dirname(__file__),"..","testcases","lilin_app"))


server = {
    "yx_jg_web_server" :"192.168.1.120:80",
    "lilin_app_server":"192.168.1.121:8080",
}

run = [yx_jg_web,lilin_app]
