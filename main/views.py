from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(response):
    return HttpResponse("hello world")

def about(response):
    return HttpResponse("about page")