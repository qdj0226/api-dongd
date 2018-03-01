#-*- coding:utf-8 -*-
__author__ = "dongd"
__datetime__ = r"2018\3\1 0001"
__software__ = "PyCharm"

import subprocess

if __name__ == '__main__':
    subprocess.check_call('locust -f test_.py --host=https://www.baidu.com', shell=True)
