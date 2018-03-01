#-*- coding:utf-8 -*-
__author__ = "dongd"
__datetime__ = r"2018\2\26 0026"
__software__ = "PyCharm"

from subclass.httpprotocol import MyHttp
from subclass.log import logger
import unittest

class LoginCase(unittest.TestCase):
    def setUp(self):
        logger.info("login测试开始。。。")
        self.my = MyHttp("http","yx_jg_web_server")
        self.url = "/smartcommunity/login/toLogin"

    def tearDown(self):
        logger.info("login测试结束。。。")

    def test_01(self):
        data = {
            "loginName":"admin",
            "password":"Adminmint"
        }
        result = self.my.post(url=self.url,data=data)
        json = result.json()
        errorCode =json["errorCode"]
        print(errorCode)
        self.assertEqual(errorCode,0)

if __name__ == '__main__':
    unittest.main()