from common.lib.db import redis_connect

from common.lib.api import Response_api


this = Response_api()

handelr_redis = redis_connect()

class SimpleMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
     
        response = self.get_response(request)
        #print(request.META.get('HTTP_ORIGIN'))
        response["Access-Control-Allow-Origin"] = request.META.get('HTTP_ORIGIN')
        return response