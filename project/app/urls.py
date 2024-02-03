from django.urls import path,include

from .views import *

urlpatterns = [

    path('',home,name="home"),
    path('registerpage/',registerpage,name='registerpage'),
    path('loginpage/',loginpage,name='loginpage'),

    # User Registration
    path('user_register/',user_register,name='user_register'),
    path('userLogin',userLogin,name='userLogin'),

    path('dashboard/',dashboard,name='dashboard'),
    path('admin_dash/',admin_dash,name='admin-dash'),


# Admin dashboard Urls
path('Add_Train/',Add_Train,name='Add_Train'),
path('Add_Route/',Add_Route,name='Add_Route'),
path('View_Route/',View_Route,name='View_Route'),
path('train_Report/',train_Report,name='train_Report'),
path('train_detail/',train_detail,name='train_detail'),
path('root_detail/',root_detail,name='root_detail'),
    
]
