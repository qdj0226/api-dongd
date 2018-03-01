#-*- coding:utf-8 -*-
__author__ = "dongd"
__datetime__ = r"2018\2\27 0027"
__software__ = "PyCharm"

import unittest,json
from subclass.httpprotocol import MyHttp
from subclass.log import logger

class Login(unittest.TestCase):
    def setUp(self):
        headres = {"Content-Type": "application/json"}
        logger.info("settest...")
        self.my = MyHttp("http","lilin_app_server",headers=headres)
        self.url = r"/yy-door-web-leelen//entry/login"

    def tearDown(self):
        logger.info("outtest...")

    def test_01(self):
        data = json.dumps({"phone":"13168106986","password":"123456"})
        result = self.my.post(url=self.url,data=data)
        print(result.json())

if __name__ == '__main__':
    unittest.main()


