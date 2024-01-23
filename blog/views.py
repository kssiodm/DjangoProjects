# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog(resquest):
    print('blog app1')
    return HttpResponse('<b>Está em blog APP 1!</b>')

def exemplo(resquest):
    print('exemplo app1')
    return HttpResponse('<b>Está em exemplo APP 1!</b>')
