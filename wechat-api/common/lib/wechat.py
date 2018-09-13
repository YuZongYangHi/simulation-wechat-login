#!/usr/bin/env python
# -*- coding:utf-8 -*- 

from django.http import HttpResponse 
from common.lib.db import redis_connect
from common.lib.api import Response_api
from common.lib.hash import hash_token
from bs4 import BeautifulSoup 
import time
import requests 
import re 
import json 

qr_url = "https://login.wx2.qq.com/jslogin?appid=wx782c26e4c19acffb&redirect_uri=https%3A%2F%2Fwx2.qq.com%2Fcgi-bin%2Fmmwebwx-bin%2Fwebwxnewloginpage&fun=new&lang=zh_CN&_={}"

qr_img = "https://login.weixin.qq.com/qrcode/{0}"

code_url = "https://login.wx2.qq.com/cgi-bin/mmwebwx-bin/login?loginicon=true&uuid={0}&tip={1}&r=874375335&_={2}"

post_url = "https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxinit?r=851572218&lang=zh_CN&pass_ticket=ISA4oelvTFvQHLtYIFKB8vFwKc6aJigI7%252BhtZstvkWKqhWgxtFBBUz%252BqDeFt0Pm1"

http_api = Response_api()
redis = redis_connect()

class Wechat(object):


    def random_time(self):
        return int(time.time() * 1000) 

    def find_qr(self):
        uri = requests.get(qr_url.format(self.random_time()))

        uid = re.findall('window.QRLogin.uuid = "(.*?)";',uri.text)[0]
        url = qr_img.format(uid)

        res = {
            "img": url,
            "uid": uid
            }
        return http_api.success(data=res)

    def search_primary_crt(self,html):
        ret = {}
        soup = BeautifulSoup(html,'html.parser')
        for tag in soup.find(name='error').find_all():
            ret[tag.name] = tag.text 
        return ret 

    def check_is_login(self,tip,uid):
        if int(tip) == 1:
            return self.wait_login(uid=uid,tip=tip)

        elif int(tip) == 0:
            return self.close_login(uid=uid,tip=tip)

    def wait_login(self,uid,tip):
        
        now_time = self.random_time()
        is_login= code_url.format(uid,tip,now_time)
        instance = requests.get(is_login)
        if 'window.code=408;' in instance.text: 
            return http_api.Custom(code=408)
        
        elif 'window.code=201' in instance.text:  
            avatar = re.findall("userAvatar = '(.*?)';",instance.text)[0]
            return http_api.Custom(code=201,data={'img':avatar})
        
        elif 'window.code=400' in s.text:
            return http_api.Custom(code=400)

    def close_login(self,uid,tip):
        now_time = self.random_time()
        s = requests.get(code_url.format(uid,tip,now_time))
        regex = re.findall('window.redirect_uri="(.*?)";',s.text)[0]
        
        crt = regex + "&fun=new&version=v2&lang=zh_CN"

        crt_response = requests.get(crt)
        response = self.search_primary_crt(crt_response.text)
       
        data = {
            "BaseRequest":{
                "DeviceID":"e658583463992794",
                "Sid":response['wxsid'],
                "Skey":response['skey'],
                "Uin":response['wxuin']
                }
        }
        
        result = requests.post(post_url,data=json.dumps(data,ensure_ascii=False))
        
        result.encoding = 'utf-8'
        value = hash_token(uid,result.text)
        redis = redis_connect()
       
        redis.set(value,result.text)
        username = json.loads(result.text)['User']['NickName']

       # print(result.text)
        return http_api.Custom(code=200,data={'uid':value,'user':username})




