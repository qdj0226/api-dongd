__author__ = "dongd"

import unittest,time
import BSTestRunner
from subclass.emailing import MyEmail
from subclass.fileDrive import file_sorting_time
from config.configFile import emailcofig
from config.configFile import testportsconfig

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
    print(testcase)
    return testcase

def main(path):
    runner = unittest.TextTestRunner().run(all_case(path))
    casecount = runner.testsRun
    failcount = len(runner.failures)
    failinfos = runner.failures
    return casecount,failcount,failinfos

def runner(suite,threadname=""):
    import os

    # 设置报告名称及保存路径
    now = time.strftime('%Y-%m%d %H%M%S', time.localtime(time.time()))
    file = os.path.join(testportsconfig, (threadname + now +'.html'))
    re_open = open(file, 'wb')
    # 实例化BSTestRunner,执行脚本
    runner = BSTestRunner.BSTestRunner(stream=re_open, title='接口测试报告', description='测试结果')
    runner.run(all_case(suite))
    re_open.close()


if __name__ == '__main__':
    from config.casSetConfig import *
    if isinstance(run,list):
        import multiprocessing
        conunt = 0
        for i in run:
            projectname = i.split("\\")[-1]
            thread = multiprocessing.Process(target=runner, args=(i,projectname))
            thread.start()
        list = file_sorting_time(testportsconfig)
        if list is not None :
            for i in run:
                # 获取最新的html文件
                htmlfile = list.pop(-1)
                htmlfile = os.path.join(testportsconfig, htmlfile)
                # 发送报告到指定邮箱
                email = MyEmail(emailcofig)
                email.send_email(htmlfile)
        elif list is None:
            print("没有报告可以发送")
        else:
            print("发送失败")
    else:
        runner(run)
        # 获取最新的html文件
        list = file_sorting_time(testportsconfig)
        if list is not None :
            for i in run:
                # 获取最新的html文件
                htmlfile = list.pop(-1)
                htmlfile = os.path.join(testportsconfig, htmlfile)
                # 发送报告到指定邮箱
                email = MyEmail(emailcofig)
                email.send_email(htmlfile)
        elif list is None:
            print("没有报告可以发送")
        else:
            print("发送失败")
