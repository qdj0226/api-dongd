#-*- coding:utf-8 -*-
__author__ = "dongd"
__datetime__ = r"2018\2\27 0027"
__software__ = "PyCharm"


import os

# 越秀旧改测试用例集路径
YX_JG_WEB = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src", "testCases", "yx_jg_web"))
# 立林app测试用例集路径
LILIN_APP = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src", "testCases", "lilin_app"))

# 服务器地址
server = {
    "yx_jg_web_server" :"jg.yx.ldsd.cc",
    "lilin_app_server":"192.168.1.121:8080",
}

RUN = [LILIN_APP,YX_JG_WEB]

if __name__ == '__main__':
    print(LILIN_APP)
    print(YX_JG_WEB)
