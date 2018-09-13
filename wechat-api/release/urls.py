# -*- coding:utf-8 -*- 


from django.urls import path
from .views import index 

urlpatterns = [
    path('',index),
]
