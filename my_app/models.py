from django.db import models

# Create your models here.
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    names=models.CharField(max_length=50)
    email=models.EmailField(max_length=50, unique=True)
    phone=models.CharField(max_length=15)
    weight=models.IntegerField(default=0)
    height=models.IntegerField(default=0)
    gender=models.CharField(max_length=10,default='male''female')
    password=models.CharField(max_length=150)

    class Meta:
        db_table = 'customer'