from django.shortcuts import render,redirect
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


def admin_dash(request):
    return render(request,'admin-dash.html')



# Admin Dashboard
def Add_Train(request):
    return render(request,'Add-train.html')

def Add_Route(request):
    return render(request,'Add-Root.html')

def View_Route(request):
    return render(request,'View-Root.html')

def train_Report(request):
    data=AddTrain.objects.all()
    return render(request,'train-Report.html',{'data':data})


def train_detail(request):
    if request.method == 'POST':
        TrainName= request.POST.get("Tname")
        TrainNo= request.POST.get("Tno")
        From= request.POST.get("From")
        To= request.POST.get("To")
        DepartureTime= request.POST.get("Depar")
        ArivalTime= request.POST.get("Arival")
        Distance= request.POST.get("Distance")
        AddTrain.objects.create(
            TrainName=TrainName,
            TrainNo=TrainNo,
            From=From,
            To=To,
            DepartureTime=DepartureTime,
            ArivalTime=ArivalTime,
            Distance=Distance,
        )
        data=AddTrain.objects.all()
        return render(request,'train-Report.html',{'data':data})
    


def root_detail(request):
    if request.method == 'POST':
        Train= request.POST.get("Tname")
        Root= request.POST.get("Tno")
        Distance= request.POST.get("From")
        Fere= request.POST.get("To")
        Add_route.objects.create(
            Train=Train,
            Root=Root,
            Distance=Distance,
            Fere=Fere
        )
        data=AddTrain.objects.all()
        return render(request,'View-Root.html',data)    
