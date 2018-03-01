# -*- coding: utf-8 -*-
# @Time    : 18-1-17 下午9:58
# @Author  : dongd
# @File    : fileDrive.py
# @Software: PyCharm


import os

def new_report(test_report):
    '''
    获取文件夹中最新文件
    :param test_report: 文件夹路劲
    :return: 返回文件全称
    '''
    lists = os.listdir(test_report)                                    #列出目录的下所有文件和文件夹保存到lists
    lists.sort(key=lambda fn:os.path.getmtime(os.path.join(test_report,fn)))#按时间排序
    file_new = os.path.join(test_report,lists[-1])                     #获取最新的文件保存到file_new`
    return file_new

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
    path = r"F:\project\api-dongd\subclass\test"
    mkdir(path)