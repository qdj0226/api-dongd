#-*- coding:utf-8 -*-
__author__ = "dongd"
__datetime__ = r"2018\3\8 0008"
__software__ = "PyCharm"


from src.commonClass.resolveXL import ResolveXL
from src.commonClass.log import logger
import json
import requests

session = None
headers=None

def post(protocol,server,url,params,sess=True):
    global session,headers
    url = "{}://{}{}".format(protocol,server,url)
    if sess:
        session = requests.session()
        exec_count = 0
        while exec_count <= 1:
            try:
                logger.info("发起post请求(session):{},值:{}".format(url, params))
                result = session.post(url, params=params, headers=headers)
                logger.info("请求头为:{}".format(result.headers))
                return result
            except Exception as e:
                if exec_count == 0:
                    exec_count = 1
                    logger.error('发送请求失败，原因：{},正在进行第二次尝试'.format(e))
                    continue
                logger.error("发送请求失败，原因：{}".format(e))
                return [None, e]
    else:
        exec_count = 0
        while exec_count <= 1:
            try:
                logger.info("发起post请求(session):{},值:{}".format(url, params))
                result = requests.post(url, params=params, headers=headers)
                logger.info("请求头为:{}".format(result.headers))
                return result
            except Exception as e:
                if exec_count == 0:
                    exec_count = 1
                    logger.error('发送请求失败，原因：{},正在进行第二次尝试'.format(e))
                    continue
                logger.error("发送请求失败，原因：{}".format(e))
                return [None, e]
def get(protocol,server,url,params=None,sess=True):
    global session,headers
    url = "{}://{}{}".format(protocol,server,url)
    if sess:
        session = requests.session()
        exec_count = 0
        while exec_count <= 1:
            try:
                logger.info("发起get请求(session):{},值:{}".format(url, params))
                result = session.get(url, params=params, headers=headers)
                logger.info("请求头为:{}".format(result.headers))
                return result
            except Exception as e:
                if exec_count == 0:
                    exec_count = 1
                    logger.error('发送请求失败，原因：{},正在进行第二次尝试'.format(e))
                    continue
                logger.error("发送请求失败，原因：{}".format(e))
                return [None, e]
    else:
        exec_count = 0
        while exec_count <= 1:
            try:
                logger.info("发起get请求:{},值:{}".format(url, params))
                result = requests.get(url, params=params, headers=headers)
                logger.info("请求头为:{}".format(result.headers))
                return result
            except Exception as e:
                if exec_count == 0:
                    exec_count = 1
                    logger.error('发送请求失败，原因：{},正在进行第二次尝试'.format(e))
                    continue
                logger.error("发送请求失败，原因：{}".format(e))
                return [None, e]


# r = ResolveXL()
# wb = r.getWorkBook(r"F:\github\api-dongd\datas\yxjg.xlsx")
# ws = r.getSheetByIndex(2)
# isE = r.getCol(ws,3)
# for idx ,id in enumerate(isE[1:]):
#     if id.value.lower() == "y":
#         ip = r.getRow(ws,idx+2)[3].value
#         url = r.getRow(ws,idx+2)[4].value
#         request_type = r.getRow(ws,idx+2)[5].value
#         data_type = r.getRow(ws, idx + 2)[7].value
#         data_type = data_type.strip()
#         value = r.getRow(ws,idx+2)[8].value
#         data = None
#         if data_type is not None and data_type == "application/x-www-form-urlencoded":
#             data = eval(value)
#         elif data_type == "application/json":
#             data = json.dumps(eval(value))
#         else:
#             print("暂时只支持form和json格式数据")


if __name__ == '__main__':
    result = post("http","192.168.1.120:80","/smartcommunity/login/toLogin",params="loginName=admin&password=Adminmint")
    print(result.json())
    print(type(session))
    result = get("http","192.168.1.120:80","/smartcommunity/administratormanagement/mainlist?isSeparate=true")
    print(type(session))
    print(result.json())