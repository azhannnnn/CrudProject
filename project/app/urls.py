from django.urls import path,include

from .views import *

urlpatterns = [

    path('',home,name="home"),
    path('registerpage/',registerpage,name='registerpage'),
    path('loginpage/',loginpage,name='loginpage'),
    
]
