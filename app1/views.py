from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def prakash(request):
    return HttpResponse('<marquee><h1>prakash has some problem</h1></marquee>)