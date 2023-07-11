from django.db import models
from django.contrib.auth.models import User 
#from django.contrib.auth.models import User 


# Create your models here.
class Profile(models.Model):
   user=models.OneToOneField(User,on_delete=models.CASCADE)
   username=models.CharField(max_length=30)
   email=models.CharField(max_length=50)
   phone=models.CharField(max_length=12)
   address=models.TextField()
   image=models.ImageField(default='IMG_0624.JPG',upload_to='profile_pics',null=True,blank=True)
   
   def __str__(self):
      return f'{self.username} Profile'
      
class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    sub = models.CharField(max_length=50)
    mes = models.TextField()

    def __str__(self):
        return self.name
    
class Menu_price(models.Model):
    menu_id=models.AutoField(primary_key=True)
    car_name=models.CharField(max_length=30)
    brand_name=models.CharField(max_length=30)
    oil_changing_price=models.CharField(max_length=30)
    batteries=models.CharField(max_length=30)
    engine_service=models.CharField(max_length=30)
    tire_wheel=models.CharField(max_length=30,null=True,blank=True)
    steering_suspension=models.CharField(max_length=30)
      

    def __str__(self):
        return self.car_name

class Manufacture(models.Model):
   m_id=models.AutoField(primary_key=True)
   m_name=models.CharField(max_length=30)

   def __str__(self):
      return self.m_name


class Car(models.Model):
   c_id=models.AutoField(primary_key=True)
   c_name=models.CharField(max_length=30)
   m_id=models.ForeignKey(Manufacture,on_delete=models.CASCADE)


   def __str__(self):
      return self.c_name

      
class Booking(models.Model):
   book_id=models.AutoField(primary_key=True)
   user_id = models.ForeignKey(User,on_delete=models.CASCADE)
   car_Brand=models.CharField(max_length=30)
   car_name=models.CharField(max_length=30)
   cust_fname=models.CharField(max_length=25)
   cust_lname=models.CharField(max_length=25)
   cust_email=models.CharField(max_length=30)
   cust_mobile=models.CharField(max_length=12)
   dateTime=models.CharField(max_length=10)
   Address=models.TextField()
   Services=models.TextField()
   stat=(('Pending','Pending'),('Approved','Approved'),('Repairing','Repairing'),('Repairing Done','Repairing Done'),('Released','Released'))
   cost=models.PositiveIntegerField(default=0,null=True)
   status=models.CharField(max_length=50,choices=stat,default='Pending',null=True)
   
   def __str__(self):
      return self.cust_fname

class parking_area(models.Model):
    parking_name = models.CharField(max_length=100)
    address = models.TextField()
    zipcode = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.parking_name

