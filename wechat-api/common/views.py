#!/usr/bin/env python
# -*- coding:utf-8 -*- 

from common.lib.api import Response_api
from common.lib.wechat import Wechat


instance = Wechat()

def login(request):
    if request.method == 'GET':
        return instance.find_qr()

def check_login(request,tip):     
    uid = request.GET.get('uid')
    return instance.check_is_login(tip,uid)

def logout(request):
    pass 