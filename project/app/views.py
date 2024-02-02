from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def registerpage(request):
    return render(request,'register.html')

def loginpage(request):
    return render(request,'login.html')