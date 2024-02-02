from django.shortcuts import render
from django .http import HttpResponse
from .models import *




# Create your views here.

def home(request):
    return render(request, 'home.html')

def registerpage(request):
    return render(request,'register.html')

def loginpage(request):
    return render(request,'login.html')




def user_register(request):
    if request.method == "POST":
        Name = request.POST.get("name")
        Email = request.POST.get("email")
        Password = request.POST.get("password")
        Cpassword = request.POST.get("cpassword")
        user = Userregister.objects.filter(Email=Email)

        if user:
            message = "User already exist"
            return render(request, "register.html", {"msg": message})
        else:
            if Password == Cpassword:
                user = Userregister(
                    Name=Name,
                    Email=Email,
                    Password=Password,
                    Cpassword=Cpassword,
                )
                user.save()
                message = "User register Successfully"
                return render(request, "login.html", {"msg": message})
            else:
                message = "Password not match"
                return render(request, "register.html", {"msg": message})




# User Login
def userLogin(request):
    if request.method == "POST":
        Email = request.POST.get("email")
        Password = request.POST.get("password")
        user = Userregister.objects.filter(Email=Email)
        if user:
            data = Userregister.objects.get(Email=Email)
            if data.Password == Password:
                Name = data.Name
                Email = data.Email
                user={
                    'Name':Name,
                    'Email':Email,
                }
                return render(request,"dashboard.html",user)
            else:
                message = "Password not match"
                return render(request, "login.html", {"msg": message})
        else:
            message = "User not exist"
            return render(request, "register.html", {"msg": message})



def dashboard(request):
    return render(request,'dashboard.html')
