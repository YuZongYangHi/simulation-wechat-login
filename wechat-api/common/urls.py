# -*- coding:utf-8 -*- 


from django.urls import path
from .views import *

urlpatterns = [
    path('login/',login),
    path('check_login/<str:tip>/',check_login),
    path('logout/',logout)
]
