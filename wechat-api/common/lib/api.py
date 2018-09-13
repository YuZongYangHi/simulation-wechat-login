#!/usr/bin/env python
# -*- coding:utf-8 -*- 

from django.http import JsonResponse 

class Response_api(object):
    
    def __new__(cls,*args,**kwargs):
        if not hasattr(cls,"_instance"):
            cls._instance = super(Response_api,cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.response = {
            "code":200,
            "message": "success",
            "data": []
        }

    def success(self,data=None):
        if data:
            self.response['data'] = data 

        return JsonResponse(self.response)

    def Notfound(self,):
        self.response['code'] = 404
        self.response['message'] = 'not found'
        return JsonResponse(self.response)
    
    def Servererror(self):
        self.response['code'] = 500
        self.response['message'] = 'server error'
        return JsonResponse(self.response)

    def Forbidden(self):
        self.response['code'] = 403
        self.response['message'] = 'server error'
        return JsonResponse(self.response)

    def Authorized(self):
        self.response['code'] = 401
        self.response['message'] = 'Authorized error'
        return JsonResponse(self.response)

    def Custom(self,code=200,message=None,data=None):

        self.response['code'] = code
        self.response['message'] = message
        self.response['data'] = data
        return JsonResponse(self.response)



