#-*- coding:utf-8 -*-
__author__ = "dongd"
__datetime__ = r"2018\2\27 0027"
__software__ = "PyCharm"


from subclass.httpprotocol import MyHttp
from requests import Session
from subclass.log import logger
import unittest

class getWuList(unittest.TestCase):
    def setUp(self):
        logger.info("runtest...")
        self.my = MyHttp("http", "192.168.1.120", "80")
        self.smy =MyHttp ("http", "192.168.1.120", "80",session=Session())
        self.url = "/smartcommunity/propertymanagement/list?isSeparate=true"

    def tearDown(self):
        logger.info("outtest")

    def test_01(self):
        result = self.my.get(url=self.url)
        print(result.json())
        print(result.status_code)


    def test_02(self):
        data = {
            "loginName": "admin",
            "password": "Adminmint"
        }
        url = "/smartcommunity/login/toLogin"
        result = self.smy.post(url=url,data=data)
        print(result.json())
        result = self.smy.get(url=self.url)
        print("list",result.json())


if __name__ == '__main__':
    unittest.main()
