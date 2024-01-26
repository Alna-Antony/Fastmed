from django.db import models

# Create your models here.
class catdb(models.Model):
    categoryname=models.CharField(max_length=100,null=True,blank=True)
    description=models.CharField(max_length=100,null=True,blank=True)
    categoryimage=models.ImageField(upload_to="catimage",null=True,blank=True)

class prodb(models.Model):
    categoryname=models.CharField(max_length=100,null=True,blank=True)
    productname=models.CharField(max_length=100,null=True,blank=True)
    productdescription=models.CharField(max_length=100,null=True,blank=True)
    productprice=models.IntegerField(null=True,blank=True)
    productimage=models.ImageField(upload_to="profile",null=True,blank=True)

class prescriptiondb(models.Model):
    prescription=models.ImageField(upload_to="prescriptionimages",null=True,blank=True)


