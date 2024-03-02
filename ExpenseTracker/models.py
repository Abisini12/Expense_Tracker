from django.db import models

from django.core.validators import MinLengthValidator
# Create your models here

class Userinfo(models.Model):
   username=models.CharField(
        max_length=255,blank=True,null=True,
        validators=[MinLengthValidator(limit_value=10, message='Ensure this field has at least 10 characters.')]
    )
   name=models.CharField(
        max_length=255,blank=True,null=True,
        validators=[MinLengthValidator(limit_value=5, message='Ensure this field has at least 5 characters.')]
    )
   email=models.CharField(max_length=255,blank=True,null=True)
   ROLE_CHOICES = (
    ('student','student'),
    ('employee','emplyoee'),
    ('manager','manager'),
    ('other','other'),
   )
   role=models.CharField(max_length=255,choices=ROLE_CHOICES, default='Student',blank=True,null=True)
   phone=models.PositiveIntegerField(blank=True,null=True)
   password=models.CharField(
        max_length=255,blank=True,null=True,
        validators=[MinLengthValidator(limit_value=8, message='Ensure this field has at least 8 characters.')]
    )
   cpassword=models.CharField(max_length=255,blank=True,null=True)

class reportinfo(models.Model):
   category=models.CharField(max_length=255,blank=True,null=True)
   purchase_product=models.CharField(max_length=255,default="choose")
   purchase_date=models.DateField(blank=True,null=True)
   amount_spent=models.DecimalField(max_digits=15, decimal_places=3,blank=True,null=True)
   number_of_products=models.PositiveIntegerField(blank=True,null=True)
   bill_receipt=models.ImageField(upload_to = 'D:/Abienv/FirstProject/media/',height_field=None, width_field=None)

class productinfo(models.Model):
   category=models.CharField(max_length=255,blank=True,null=True)
   purchase_product=models.CharField(max_length=255,default="choose")
   purchase_date=models.DateField(blank=True,null=True)
   amount_spent=models.DecimalField(max_digits=15, decimal_places=3,blank=True,null=True)
   number_of_products=models.PositiveIntegerField(blank=True,null=True)
   bill_receipt=models.ImageField(upload_to = 'D:/Abienv/FirstProject/media/',height_field=None, width_field=None)



   