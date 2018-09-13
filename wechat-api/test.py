# -*- coding:utf-8 -*-
import json 

f = open('result.txt','r')

text = json.load(f)
print(type(text))

print(text['User']['NickName'])
