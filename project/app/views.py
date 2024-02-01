from django.shortcuts import render
from django .http import HttpResponse



def home(request):
    
    return HttpResponse("First time commit")


# Create your views here.
def index(request):
    # ugu
    return HttpResponse('hello')
