#!/usr/bin/env python
# -*- coding:utf-8 -*- 

from common.lib.db import redis_connect 
from common.lib.api import Response_api
import json 

redis = redis_connect()


class Parser(object):
    def __init__(self,request):
        self.request = request

    def parser(self):
        with open('result.txt','w') as f:
            text = self.get_text()
            f.write(text)

    def wait(self):
        pass 

    def get_text(self):
        token = self.request.META.get('HTTP_AUTHORIZATION')
        text = redis.get(token)
        return text.decode()