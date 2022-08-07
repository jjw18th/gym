from django.shortcuts import render
from django.http import HttpResponse

def landing(request):
    res=render(request,'gym/landing2.html')
    return res;
def about(request):
    res=render(request,'gym/about2.html')
    return res;
def contact(request):
    res=render(request,'gym/contact.html')
    return res;
def message(request):
    res=render(request,'gym/contact.html')
    return res;
