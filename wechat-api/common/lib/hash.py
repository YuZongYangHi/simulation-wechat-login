#!/usr/bin/env python
# -*- coding:utf-8 -*-
import hashlib
import hmac
import base64
from django.conf import settings

def hash_token(uid,crt):
    key = settings.SALT.encode(encoding ='utf-8')
    integration = "%s%s" % (uid,crt)
    encryption = hmac.new(key,integration.encode(encoding='utf-8'),digestmod=hashlib.sha1).digest()
    token = base64.b64encode(encryption).decode()
    return token