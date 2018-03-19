#-*- coding:utf-8 -*-
__author__ = "dongd"
__datetime__ = r"2018\2\26 0026"
__software__ = "PyCharm"


import os

emailcofig = os.path.abspath(os.path.join(os.path.dirname(__file__),"emailconfig.ini"))
logconfig = os.path.abspath(os.path.join(os.path.dirname(__file__),"logconfig.ini"))
logfile = log_path = os.path.abspath(os.path.join(os.path.dirname(__file__),"..","logs"))
testportsconfig = os.path.abspath(os.path.join(os.path.dirname(__file__),"../","testreports"))
dataexcelfile = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "datas", "yxjg.xlsx"))


if __name__ == '__main__':
    print(testportsconfig)
    print(logconfig)
    print(logfile)
    print(emailcofig)
