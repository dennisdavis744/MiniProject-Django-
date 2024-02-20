from django.db import models

# Create your models here.

class customer_registeration(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    age = models.IntegerField()
    phone = models.IntegerField()
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    confirm_password = models.CharField(max_length=30)

class productsinfo(models.Model):
    product_name = models.CharField(max_length=50)
    price = models.IntegerField()
    material = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/',blank=True)

class staff_regsinfo(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    confirm_password = models.CharField(max_length=30)
    verfiystatus=models.BooleanField(default=False)

class addproduct(models.Model):
    itemname=models.CharField(max_length=100)
    itemimage = models.ImageField(upload_to='images/',blank=True)
    price = models.IntegerField()
    material = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

class cartetl(models.Model):
    userid=models.IntegerField(null=False,primary_key=False)
    coverimage=models.CharField(max_length=10,null=False)
    itemname=models.CharField(max_length=100)
    price=models.IntegerField(null=False)