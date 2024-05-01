from django.db import models

# Create your models here.


   

# categories

class Plants(models.Model):
    name=models.TextField(max_length=100,null=True)

    def __str__(self):
        return self.name

class Pots(models.Model):
    name=models.TextField(max_length=100,null=True)

    def __str__(self):
        return self.name

class Pebbles(models.Model):
    name=models.TextField(max_length=100,null=True)

    def __str__(self):
        return self.name

class Fertilisers(models.Model):
    name=models.TextField(max_length=100,null=True)

    def __str__(self):
        return self.name

class Seeds(models.Model):
    name=models.TextField(max_length=100,null=True)

    def __str__(self):
        return self.name

# products

class Plants_Products(models.Model):
    name=models.TextField(max_length=100,null=True)
    description=models.TextField(max_length=400,null=True)
    image=models.ImageField(upload_to='plants',null=True)
    price=models.FloatField(null=True)
    category=models.ForeignKey(Plants,on_delete=models.CASCADE)

class Pots_Products(models.Model):
    name=models.TextField(max_length=100,null=True)
    description=models.TextField(max_length=400,null=True)
    image=models.ImageField(upload_to='Pots',null=True)
    price=models.FloatField(null=True)
    category=models.ForeignKey(Pots,on_delete=models.CASCADE)

class Pebbles_Products(models.Model):
    name=models.TextField(max_length=100,null=True)
    description=models.TextField(max_length=400,null=True)
    image=models.ImageField(upload_to='Pebbles',null=True)
    price=models.FloatField(null=True)
    category=models.ForeignKey(Pebbles,on_delete=models.CASCADE)

class Fertilisers_Products(models.Model):
    name=models.TextField(max_length=100,null=True)
    description=models.TextField(max_length=400,null=True)
    image=models.ImageField(upload_to='Fertilisers',null=True)
    price=models.FloatField(null=True)
    category=models.ForeignKey(Fertilisers,on_delete=models.CASCADE)

class Seeds_Products(models.Model):
    name=models.TextField(max_length=100,null=True)
    description=models.TextField(max_length=400,null=True)
    image=models.ImageField(upload_to='Seeds',null=True)
    price=models.FloatField(null=True)
    category=models.ForeignKey(Seeds,on_delete=models.CASCADE)
