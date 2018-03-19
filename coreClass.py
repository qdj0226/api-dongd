#-*- coding:utf-8 -*-
#__author__ = "dongd"
#__datetime__ = r"2018\3\13 0013"
#__software__ = "PyCharm"


import unittest,time,os
import BSTestRunner
from config.configFile import testportsconfig,emailcofig
from src.commonClass.emailing import MyEmail


def all_case(path):
    '''
    获取所有测试用例
    :param path: 用例集文件夹
    :return: 返回TestSuite实例
    '''
    # 定义一个单元测试容器
    testcase = unittest.TestSuite()
    # 匹配test开头的所有py文件
    discover = unittest.defaultTestLoader.discover(path,
                                                   pattern="test*.py",
                                                   top_level_dir=None)

    # discover匹配出来的脚本循环到测试容器中
    for test_suite in discover:
        for test_case in test_suite:
            testcase.addTest(test_case)
    print("测试用例集",testcase)
    print("用例路径:",path)
    return testcase


def runner(suite,threadname=""):

    # 设置报告名称及保存路径
    now = time.strftime('%Y-%m-%d %H%M%S', time.localtime(time.time()))
    file = os.path.join(testportsconfig, (threadname + now +'.html'))
    print(file)
    re_open = open(file, 'wb')
    # 实例化BSTestRunner,执行脚本
    runner = BSTestRunner.BSTestRunner(stream=re_open, title='接口测试报告', description='测试结果')
    runner.run(all_case(suite))
    re_open.close()


def send_email(report_list,send_list):
    '''
    获取最新的测试报告并发送至指定邮箱
    :param report_list: 测试报告列表
    :param send_list:
    :return:
    '''
    try:
        if report_list is not None:
            for i in send_list:
                # 获取最新的html文件
                htmlfile = report_list.pop(-1)
                print(htmlfile)
                htmlfile = os.path.join(testportsconfig, htmlfile)
                # 发送报告到指定邮箱
                email = MyEmail(emailcofig)
                email.send_email(htmlfile)
        elif report_list is None:
            print("没有报告可以发送")
    except Exception as e:
        raise e