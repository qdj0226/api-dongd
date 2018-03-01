#-*- coding:utf-8 -*-
__author__ = "dongd"
__datetime__ = r"2018\3\1 0001"
__software__ = "PyCharm"

from locust import HttpLocust, TaskSet, task
import subprocess
import json

from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    @task(1)
    def baidu(self):
        self.client.post("/post")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000



