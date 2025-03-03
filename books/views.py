from django.shortcuts import render
from django.http import HttpResponse

# view function for home page declared here
def home(request):
    return HttpResponse('<h1>Hello World!</h1>')
