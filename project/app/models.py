from django.db import models

# Create your models here.
class Userregister(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Password = models.CharField(max_length=100)
    Cpassword = models.CharField(max_length=100)




# Add Train Model
    
class AddTrain(models.Model):
    TrainName= models.CharField(max_length=100)   
    TrainNo= models.IntegerField()   
    From= models.CharField(max_length=100)   
    To= models.CharField(max_length=100)   
    DepartureTime= models.CharField(max_length=100)   
    ArivalTime= models.CharField(max_length=100)   
    Distance= models.CharField(max_length=100)   
    
# Add Train Roots Model
class Add_route(models.Model):
    Train = models.ForeignKey(AddTrain,on_delete=models.CASCADE,null=True)
    Route = models.CharField(max_length=100)
    Distance=models.IntegerField()
    Fare=models.IntegerField()