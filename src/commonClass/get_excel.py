# -*- coding: utf-8 -*-
# @Time    : 18-1-17 上午9:26
# @Author  : dongd
# @File    : get_excel.py
# @Software: PyCharm

import xlrd

from src.commonClass.log import logger


class GetExcel():
    def __init__(self,xlsxfile,listname):
        '''

        :param xlsxfile: excel文件
        :param listname: sheet名称
        '''
        self.xlrd = xlrd.open_workbook(xlsxfile)
        if isinstance(listname,str):
            try:
                logger.info("获取xlsx列表,列表名:{}".format(listname))
                self.data = self.xlrd.sheet_by_name(listname)
            except Exception as e:
                logger.info("获取xlsx列表索引,索引号:{}".format(listname))
                logger.error("获取xlsx列表失败,错误信息:{}".format(e))
        elif isinstance(listname,int):
            try:
                self.data = self.xlrd.sheets()[listname]
            except Exception as e:
                logger.error("获取xlsx列表失败,错误信息:{}".format(e))
        else:
            logger.error("只能输入表格名称和表格索引号")
            raise Exception("只能输入表格名称和表格索引号")
        try:
            self.row = self.data.nrows  #行数
            self.col = self.data.ncols  #列数
        except Exception as e:
            logger.error("获取xlsx列表失败,错误信息:{}".format(e))
            raise Exception(e)

    def get_data_dict(self):
        if self.row < 1:
            # 表格列数小于1时不做任何读取操作
            print("表格的列小于1")
        else:
            # 使用第一列作为字典的键
            key = self.data.row_values(0)
            list = []
            j = 1
            # 由于第一列为标题所以递归时-1
            for i in range(self.row - 1):
                dict = {}
                value = self.data.row_values(j)
                for x in range(self.col):
                    dict[key[x]] = value[x]
                list.append(dict)
                j += 1
            return list

if __name__ == '__main__':
    ge = GetExcel(r"F:\github\api-dongd\datas\yxjg.xlsx","testCase")
    data = ge.get_data_dict()
    print(data)