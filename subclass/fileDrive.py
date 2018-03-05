# -*- coding: utf-8 -*-
# @Time    : 18-1-17 下午9:58
# @Author  : dongd
# @File    : fileDrive.py
# @Software: PyCharm


import os

def file_sorting_time(test_report):
    '''
    按时间排序文件
    :param test_report: 文件夹路径
    :return: 返回文件全称
    '''
    lists = os.listdir(test_report)                                    #列出目录的下所有文件和文件夹保存到lists
    if len(lists) == 0:
        return None
    else:
        lists.sort(key=lambda fn:os.path.getmtime(os.path.join(test_report,fn)))#按时间排序
        # file_new = os.path.join(test_report,lists.pop(-1))                     #获取最新的文件保存到file_new`
        return lists

def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)

    if not isExists:
        os.makedirs(path)
        print("文件夹创建成功——————{}".format(path))
        return True
    else:
        print("文件夹已存在——————{}".format(path))

if __name__=="__main__":
    from config.configFile import testportsconfig
    print(file_sorting_time(testportsconfig).pop(-1))