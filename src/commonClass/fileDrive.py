# -*- coding: utf-8 -*-
# @Time    : 18-1-17 下午9:58
# @Author  : dongd
# @File    : fileDrive.py
# @Software: PyCharm


import os

def file_sorting_time_latest(test_report):
    '''
    按时间排序获取最新文件
    :param test_report: 文件夹路径
    :return: 返回文件全称
    '''
    lists = os.listdir(test_report)                                    #列出目录的下所有文件和文件夹保存到lists
    if len(lists) == 0:
        return None
    else:
        lists.sort(key=lambda fn:os.path.getmtime(os.path.join(test_report,fn)))#按时间顺序排序
        return lists

def file_sorting_time_latest_old(test_report):
    '''
        按时间排序获取最旧文件
        :param test_report: 文件夹路径
        :return: 返回文件全称
        '''
    lists = os.listdir(test_report)  # 列出目录的下所有文件和文件夹保存到lists
    if len(lists) == 0:
        return None
    else:
        lists.sort(key=lambda fn: os.path.getmtime(os.path.join(test_report, fn)),reverse=True)  # 按时间倒叙排序
        return lists

def mkdir(path):
    '''创建文件夹'''
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)

    if not isExists:
        os.makedirs(path)
        print("文件夹创建成功——————{}".format(path))
        return True
    else:
        print("文件夹已存在——————{}".format(path))


def max_filenumber(filelist,max_number,filepath):
    '''
    检测文件夹内文件数量，大于指定数量将会删除，每次删除最后一个文件
    :param filelist: 传入文件列表
    :param max_number: 最大数量
    :param filepath: 文件夹路径
    '''
    try:
        if len(filelist)> max_number:
            file = os.path.join(filepath, filelist.pop(-1))
            os.remove(file)
            max_filenumber(filelist,max_number,filepath)
    except Exception as e:
        raise e

if __name__ == '__main__':
    file = r"F:\github\api-dongd\testreports"
    files = file_sorting_time_latest_old(file)
    print(files)