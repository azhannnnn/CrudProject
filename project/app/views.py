from django.shortcuts import render
from django .http import HttpResponse




# Create your views here.

def home(request):
    return render(request, 'home.html')

def registerpage(request):
    return render(request,'register.html')

def loginpage(request):
    return render(request,'login.html')

<<<<<<< HEAD

def dashboard(request):
    return render(request,'dashboard.html')
=======
>>>>>>> cbe1c24799d709f90c2f7bccf73b4f3ba605bb01
