#!/usr/bin/env python
# -*- coding:utf-8 -*- 
from common.lib.db import redis_connect

from common.lib.api import Response_api

this = Response_api()

handelr_redis = redis_connect()
'''
    判断token过期时间，从redis里面获取，如果过期，返回401，前端强制push到login页面

'''
def login_required(func):

    def wrapper(request,*args,**kwargs):

        try:
            token = request.META.get('HTTP_AUTHORIZATION')
            print(token)

        except AttributeError:

            return this.Authorized()

        auth = handelr_redis.get(token)

        if not auth :

            return this.Authorized()

        return func(request,*args,**kwargs)

    return wrapper