from django.shortcuts import render,redirect
from django .http import HttpResponse
from .models import *
from django.db.models import Q





# Create your views here.

def home(request):
    return render(request, 'home.html')

def registerpage(request):
    return render(request,'register.html')

def loginpage(request):
    return render(request,'login.html')

def booking(request):
    email = request.session['email']
    user = Userregister.objects.get(Email=email)
    if user:
        data = Booking.objects.filter(Email=email)
        return render(request,'booking.html',{'data':data})
    else:
        msg="Booking not found"
        return render(request,'booking.html',{'msg':msg})
   

def search(request):
    user=AddTrain.objects.all()
    return render(request,'search.html',{'user':user})


# User registration
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
                pk = data.id
                print(pk)
                request.session['id']=pk
                request.session['name']=Name
                request.session['email']=Email
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

def logout(request):

    del request.session['name']
    del request.session['email']
    request.session.flush()

    return redirect('home')


def dashboard(request):

     Email = request.session['email']
     Name = request.session['name']
          
     user={
            'Name':Name,
            'Email':Email,
          }
     return render(request,"dashboard.html",user)




def enquiry(request):
    email = request.session['email']
    user = Userregister.objects.get(Email=email)
    
    name = user.Name
    mail = user.Email
    
    return render(request,'enquiry.html',{"Name":name,"Email":mail})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('Cname')
        email = request.POST.get('Cemail')
        msg = request.POST.get('Cmsg')

        Name = request.session['name']
        
        Contacts.objects.create(
            Name=name,
            Email=email,
            Msg=msg,
        )
        return render(request,'dashboard.html',{'Name':Name})
    
def bookuser(request,pk):
    data = AddTrain.objects.get(id=pk)
    
    TrainName=data.TrainName
    TrainNo=data.TrainNo
    From=data.From
    To=data.To
    DepartureTime=data.DepartureTime
    Distance=data.Distance
    name = request.session['name']
    email = request.session['email']
    print(TrainName)
    user = {
        'Name':name,
        'Email':email,
        'TrainName':TrainName,
        'TrainNo':TrainNo,
        'From':From,
        'To':To,
        'DepartureTime':DepartureTime,
        'Distance':Distance
    }

    return  render(request,"bookingpage.html",{'User':user})

def booknow(request):
    if request.method == 'POST':
        TrainName = request.POST.get('Tname')
        TrainNo = request.POST.get('Tno')
        From = request.POST.get('From')
        To = request.POST.get('To')
        DepartureTime = request.POST.get('Depar')
        Distance = request.POST.get('Distance')
        Name = request.POST.get('Name')
        Email = request.POST.get('Email')

        Booking.objects.create(
            Name=Name,
            Email=Email,
            TrainName=TrainName,
            TrainNo=TrainNo,
            From=From,
            To=To,
            DepartureTime=DepartureTime,
            Distance=Distance
        )
        
        user = Userregister.objects.get(Email=Email)
        if user:
            data = Booking.objects.filter(Email=Email)
            return render(request,'booking.html',{'data':data})
        else:
            msg="Booking not found"
            return render(request,'booking.html',{'msg':msg})
        
def cancel(request,pk):
    user=Booking.objects.get(id=pk)
    user.delete()
    email = request.session['email']
    data=Booking.objects.filter(Email=email)
    return render(request,'booking.html',{'data':data})


        



# Admin Dashboard
def admin_dash(request):
    return render(request,'admin-dash.html')

def Add_Train(request):
    return render(request,'Add-train.html')

def train_Report(request):
    user=AddTrain.objects.all()
    return render(request,'train-Report.html',{'user':user})



def Admin_loginpage(request):
    return render(request,'admin-login.html')

# Admin Registration Views 


def Admin_Login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

       # Checking the emailid with database
        user = Adminregister.objects.filter(Email=email)
        if user:
            data = Adminregister.objects.get(Email=email)
            if data.Password == password:
                Name = data.Name
                Email = data.Email
                password = data.Password
                request.session['name'] = Name
                request.session['email'] = Email
                user = {
                    "Name": Name,
                    "Email": Email,
                }
                return render(request, "admin-dash.html", {'user':user})
            else:
                message = "Password does not match"
                return render(request, "Admin-login.html", {"msg": message})
        else:
            message = "Information does not exist"
            return render(request, "Admin-login.html", {"msg": message})            


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
        user=AddTrain.objects.all()
        return render(request,'train-Report.html',{'user':user})
    


def editTrain(request,pk):
    data=AddTrain.objects.get(id=pk)
    return render(request,'edit-Train.html',{'user':data})

def edit(request,pk):
    user=AddTrain.objects.get(id=pk)
    user. TrainName=request.POST.get('Tname')
    user.TrainNo=request.POST.get('Tno')
    user. From=request.POST.get('From')
    user.To=request.POST.get('To')
    user.DepartureTime=request.POST.get('Depar')
    user.ArivalTime=request.POST.get('Arival')
    user. Distance=request.POST.get('Distance')
    user.save()
    data=AddTrain.objects.all()
    return render(request,'train-Report.html',{'user':data})


def delete(request,pk):
    user=AddTrain.objects.get(id=pk)
    user.delete()
    data=AddTrain.objects.all()
    return render(request,'train-Report.html',{'user':data})



def Search_train(request):
    if request.method == 'GET':
        search=request.GET.get('search')
        key = AddTrain.objects.filter( Q(TrainName=search ) |  Q(TrainNo=search))
        print(key)
        return render(request,'train-Report.html',{'key':key})

    
def user_search(request):
    if request.method == 'GET':
        search=request.GET.get('search')
        print(search)
        key = AddTrain.objects.filter( (Q(TrainName=search )) or (Q(TrainNo=search)))
        return render(request,'search.html',{'key':key})
    

def viewbooking(request):
    data=Booking.objects.all()
    return render(request,'viewbooking.html',{'data':data})

def suspend(request,pk):
    user=Booking.objects.get(id=pk)
    user.delete()
    data=Booking.objects.filter()
    return render(request,'viewbooking.html',{'data':data})