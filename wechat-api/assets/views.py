from django.shortcuts import render
from django.http import HttpResponse 
from common.lib.core import login_required 
from common.lib.parser import Parser 
# Create your views here.


@login_required
def index(request):
    par = Parser(request)
    par.parser()

    return HttpResponse('hello World')