__author__ = "dongd"

import requests

from config.casSetConfig import server
from src.commonClass.log import logger

class MyHttp():
    '''
    请求类,封装get和post方法
    '''
    def __init__(self, protocol, servername, headers = None,session=None):
        '''
        :param protocol:协议类型
        :param servername:服务器名称，从配置文件中获取
        :param headers:请求头
        :param session:session实例
        '''
        self.protocol = protocol
        self.server = server[servername]
        self.header = headers
        self.session = session

    # 设置协议类型
    def get_protocol(self):
        return self.protocol

    # 设置请求头
    def set_header(self, headers):
        self.headers = headers

    def get(self,url,params=None,):
        url = "{}://{}{}".format(self.protocol,self.server, url)
        if self.session!=None and isinstance(self.session,requests.sessions.Session):
            logger.info("发起get请求(session):{},值:{}".format(url, params))
            logger.info("请求头为:{}".format(self.header))
            exec_count = 0
            while exec_count <= 1:
                try:
                    result = self.session.get(url=url, params=params, headers=self.header)
                    return result
                except Exception as e:
                    if exec_count == 0:
                        exec_count = 1
                        logger.error('发送请求失败，原因：{},正在进行第二次尝试'.format(e))
                        continue
                    logger.error("发送请求失败，原因：{}".format(e))
                    return [None, e]
        else:
            logger.info("发起get请求:{},值:{}".format(url,params))
            logger.info("请求头为:{}".format(self.header))
            exec_count = 0
            while exec_count<=1:
                try:
                    result = requests.get(url=url,params=params,headers=self.header)
                    return result
                except Exception as e:
                    if exec_count == 0:
                        exec_count = 1
                        logger.error('发送请求失败，原因：{},正在进行第二次尝试'.format(e))
                        continue
                    logger.error("发送请求失败，原因：{}".format(e))
                    return [None,e]


    def post(self,url,data):
        url = "{}://{}{}".format(self.protocol, self.server, url)
        if self.session != None and isinstance(self.session, requests.sessions.Session):
            logger.info("发起post请求(session):{},值:{}".format(url, data))
            logger.info("请求头为:{}".format(self.header))
            exec_count = 0
            while exec_count <= 1:
                try:
                    result = self.session.post(url=url, params=data, headers=self.header)
                    return result
                except Exception as e:
                    if exec_count == 0:
                        exec_count = 1
                        logger.error('发送请求失败，原因：{},正在进行第二次尝试'.format(e))
                        continue
                    logger.error("发送请求失败，原因：{}".format(e))
                    return [None, e]
        else:
            logger.info("发起post请求:{},值:{}".format(url, data))
            logger.info("请求头为:{}".format(self.header))
            exec_count = 0
            while exec_count<=1:
                try:
                    result = requests.post(url=url,params=data,headers=self.header)
                    return result
                except Exception as e:
                    if exec_count == 0:
                        exec_count = 1
                        logger.error('发送请求失败，原因：{},正在进行第二次尝试'.format(e))
                        continue
                    logger.error("发送请求失败，原因：{}".format(e))
                    return [None,e]

    def requestmode(self,request,url,data=None,params=None):
        if request == "post":
            result = self.post(url,data)
            return result
        elif request == "get":
            result = self.get(url, params)
            return result
        else:
            logger.error("请确认请求方法")
            return None

if __name__ == '__main__':
    session = requests.session()
    my = MyHttp("http","yx_jg_web_server",session=session)
    result = my.post("/smartcommunity/login/toLogin",data="loginName=admin&password=Adminmint")
    print(result.json())
    result = my.get(url="/smartcommunity/administratormanagement/mainlist?isSeparate=true")
    print(result.json())
