from django.db import models
from customer.models import *
from staff.models import *
# Create your models here.
class Cart(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    plants=models.ForeignKey(Plants_Products,on_delete=models.CASCADE,null=True)
    plants_quantity=models.IntegerField(default=1)
    pots=models.ForeignKey(Pots_Products,on_delete=models.CASCADE,null=True)
    pots_quantity=models.IntegerField(default=1)
    pebbles=models.ForeignKey(Pebbles_Products,on_delete=models.CASCADE,null=True)
    pebbles_quantity=models.IntegerField(default=1)
    fertilisers=models.ForeignKey(Fertilisers_Products,on_delete=models.CASCADE,null=True)
    fertilisers_quantity=models.IntegerField(default=1)
    seeds=models.ForeignKey(Seeds_Products,on_delete=models.CASCADE,null=True)
    seeds_quantity=models.IntegerField(default=1)