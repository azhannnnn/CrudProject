from django.db import models

# Create your models here.
class Userregister(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Password = models.CharField(max_length=100)
    Cpassword = models.CharField(max_length=100)


# Admin Model
class Adminregister(models.Model):
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
    def __str__(self):
        return self.TrainName   
    

    # Contact Detail
class Contacts(models.Model):
         Name = models.CharField(max_length=100)
         Email = models.EmailField()
         Msg = models.TextField(max_length=200)

#User bookings
         
class Booking(models.Model):
     Name = models.CharField(max_length=100)
     Email = models.EmailField()
     TrainName = models.CharField(max_length=100)
     TrainNo = models.IntegerField()
     From = models.CharField(max_length=100)
     To = models.CharField(max_length=100)
     DepartureTime = models.CharField(max_length=100)
     Distance = models.CharField(max_length=100)
