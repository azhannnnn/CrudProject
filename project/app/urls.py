from django.urls import path,include

from .views import *

urlpatterns = [

    path('',home,name="home"),
    path('registerpage/',registerpage,name='registerpage'),
    path('loginpage/',loginpage,name='loginpage'),


    # User Registration
    path('user_register/',user_register,name='user_register'),
    path('userLogin',userLogin,name='userLogin'),
    
]
