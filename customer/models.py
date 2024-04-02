from django.db import models
#from Staff.models import *
# Create your models here.
class Customer(models.Model):
    name=models.TextField(max_length=100,null=True)
    email=models.TextField(max_length=100,null=True)
    password=models.TextField(max_length=100,null=True)



