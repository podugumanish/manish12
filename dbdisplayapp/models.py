from django.db import models


# Create your models here.
class Product(models.Model):
    Pid=models.IntegerField(primary_key=True)
    Pname=models.CharField(max_length=20)
    Pcost=models.DecimalField(max_digits=10,decimal_places=4)
    Pmfd=models.DataField()
    Pexpdt=models.DataField()

