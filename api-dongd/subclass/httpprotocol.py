__author__ = "dongd"

from subclass.log import logger
import requests

class MyHttp():
    '''
    请求类,封装get和post方法
    '''
    def __init__(self, protocol, host, port, headers = None,session=None):
        '''
        :param protocol:协议类型
        :param host:ip域名
        :param port:端口
        :param headers:请求头
        :param session:session实例
        '''
        self.protocol = protocol
        self.host = host
        self.port = port
        self.header = headers
        self.session = session

    def set_host(self, host):
        self.host = host

    def get_host(self):
        return self.host

    def get_protocol(self):
        return self.protocol

    def set_port(self, port):
        self.port = port

    def get_port(self):
        return  self.port

    # 设置http头
    def set_header(self, headers):
        self.headers = headers

    def get(self,url,params=None,):
        url = "{}://{}:{}{}".format(self.protocol, self.host, self.port, url)
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
        url = "{}://{}:{}{}".format(self.protocol, self.host, self.port, url)
        if self.session != None and isinstance(self.session, requests.sessions.Session):
            logger.info("发起post请求(session):{},值:{}".format(url, data))
            logger.info("请求头为:{}".format(self.header))
            exec_count = 0
            while exec_count <= 1:
                try:
                    result = self.session.post(url=url, data=data, headers=self.header)
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
                    result = requests.post(url=url,data=data,headers=self.header)
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