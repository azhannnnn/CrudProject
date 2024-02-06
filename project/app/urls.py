from django.urls import path,include

from .views import *

urlpatterns = [

    path('',home,name="home"),
    path('registerpage/',registerpage,name='registerpage'),
    path('loginpage/',loginpage,name='loginpage'),

    # User Registration
    path('user_register/',user_register,name='user_register'),
    path('userLogin',userLogin,name='userLogin'),
    path('bookuser/<int:pk>/',bookuser,name='bookuser'),
    path('booknow/',booknow,name='booknow'),

    path('dashboard/',dashboard,name='dashboard'),
    path('admin_dash/',admin_dash,name='admin-dash'),
    path('booking/',booking,name='booking'),
    path('search/',search,name='search'),
    path('logout/',logout,name='logout'),
    path('enquiry/',enquiry,name='enquiry'),
    path('contact/',contact,name='contact'),
    path('user_search/',user_search,name='user_search'),
    path('cancel/<int:pk>/',cancel,name='cancel'),


    # Admin dashboard Urls
    
    path('Admin_loginpage/',Admin_loginpage,name='Admin_loginpage'),
    path('Admin_Login/',Admin_Login,name='Admin_Login'),

    path('Add_Train/',Add_Train,name='Add_Train'),
    path('train_Report/',train_Report,name='train_Report'),
    path('train_detail/',train_detail,name='train_detail'),
    path('editTrain/<int:pk>/',editTrain,name='editTrain'),
    path('edit/<int:pk>/',edit,name='edit'),
    path('delete/<int:pk>/',delete,name='delete'),
    path('Search_train/',Search_train,name='Search_train'),
    path('viewbooking/',viewbooking,name='viewbooking'),
    path('suspend/<int:pk>',suspend,name='suspend'),

    
]
