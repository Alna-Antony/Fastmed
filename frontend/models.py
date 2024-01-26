from django.db import models

# Create your models here.


class contactdb(models.Model):
    firstname=models.CharField(max_length=100,null=True,blank=True)
    lastname=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    subject=models.CharField(max_length=100,null=True,blank=True)
    message=models.CharField(max_length=100,null=True,blank=True)

class signupdb(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    mobile=models.IntegerField(null=True,blank=True)
    password=models.CharField(max_length=50,null=True,blank=True)


class cartdb(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    productname=models.CharField(max_length=100,null=True,blank=True)
    categoryname=models.CharField(max_length=100,null=True,blank=True)
    price = models.IntegerField(null=True, blank=True)
    quantity=models.IntegerField(null=True,blank=True)
    totalprice=models.IntegerField(null=True,blank=True)
    prescrip=models.ImageField(upload_to="prescription",null=True,blank=True)

class paymentdb(models.Model):
    cardnum=models.IntegerField(null=True,blank=True)
    cardhold=models.CharField(max_length=100,null=True,blank=True)
    expmon=models.IntegerField(null=True,blank=True)
    expy=models.IntegerField(null=True,blank=True)
    ccvv=models.IntegerField(null=True,blank=True)


class checkoutdb(models.Model):
    country=models.CharField(max_length=100,null=True,blank=True)
    firstname=models.CharField(max_length=100,null=True,blank=True)
    lastname=models.CharField(max_length=100,null=True,blank=True)
    username=models.CharField(max_length=100,null=True,blank=True)
    productname=models.CharField(max_length=100,null=True,blank=True)
    total_price=models.IntegerField(null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    state=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    phone=models.IntegerField(null=True,blank=True)

class pdfdb(models.Model):
    username = models.CharField(max_length=100,null=True,blank=True)
    firstname = models.CharField(max_length=100,null=True,blank=True)
    lastname = models.CharField(max_length=100,null=True,blank=True)
    productname = models.CharField(max_length=100,null=True,blank=True)
    address = models.CharField(max_length=100,null=True,blank=True)
    total_price = models.IntegerField(null=True,blank=True)
    mobile = models.IntegerField(null=True,blank=True)
    Email = models.EmailField(null=True,blank=True)




