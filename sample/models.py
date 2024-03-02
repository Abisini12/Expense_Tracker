from django.db import models

# Create your models here.
class TableIntro(models.Model):
    Amount=models.DecimalField(max_digits=15, decimal_places=3,blank=True,null=True)
    Accountid=models.IntegerField(blank=True,null=True)
    Categoryid=models.IntegerField(blank=True,null=True)
    Trans_type=models.CharField(max_length=50,blank=True,null=True)
    Payee=models.CharField(max_length=255,blank=True,null=True)
    Payee_to=models.CharField(max_length=255,blank=True,null=True)
    Trans_to=models.CharField(max_length=255,blank=True,null=True)


