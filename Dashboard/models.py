# from django.db import models

# # Create your models here.
 
# class Event(models.Model):
#     name = models.CharField(max_length=100)
#     date = models.DateField()
#     time = models.TimeField()
#     location = models.CharField(max_length=300)
#     requirement=models.CharField(max_length=300)
#     themes = models.CharField(max_length=300)
#     def __str__(self) :
#         return(f"{self.name} ")

# class Customer(models.Model):
#     Cust_name=models.CharField(max_length=100)
#     Cust_email=models.EmailField(max_length=100)
#     Cust_phone_no=models.CharField(max_length=10)
#     Cust_address=models.CharField(max_length=500)
    
# class Venue (models.Model):
#     Venue_Event_name =models.CharField(max_length=200)
#     Event_type =models.CharField(max_length=200)
#     Event_price=models.IntegerField()
#     Event_address =models.CharField(max_length=500)
   
# class Payment (models.Model):
#     Event_name =models.CharField(max_length=200)
#     Price =models.CharField(max_length=200)
#     payment_type =models.CharField(max_length=200)
#     payment_pending=models.CharField(max_length=200)
  
from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=300)
    requirement = models.CharField(max_length=300)
    themes = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.name}"

class Customer(models.Model):
    cust_name = models.CharField(max_length=100)
    cust_email = models.EmailField(max_length=100)
    cust_phone_no = models.CharField(max_length=10)
    cust_address = models.CharField(max_length=500)

class Venue(models.Model):
    venue_event_name = models.CharField(max_length=200)
    event_type = models.CharField(max_length=200)
    event_address = models.CharField(max_length=500)

class Payment(models.Model):
    name = models.CharField(max_length=300)
    price = models.CharField(max_length=300)
    payment_type = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    
class Employee(models.Model):
    emp_name = models.CharField(max_length=100)
    emp_email = models.EmailField(max_length=100)
    contact_number = models.CharField(max_length=10)
    address = models.CharField(max_length=300)
      
class Salary(models.Model):
    employee_name = models.CharField(max_length=100)
    date = models.DateField(max_length=100)
    month = models.CharField(max_length=10)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

