from django.db import models

# Create your models here.
class Customer(models.Model):
    Name =models.CharField(max_length=50)
    Email =models.EmailField()
    Contect=models.CharField(max_length=10)
    Password=models.CharField(max_length=10)
    Re_Password=models.CharField(max_length=10)

class MyCust(models.Model):
    Email=models.EmailField()
    Pasword=models.CharField(max_length=20)
    
