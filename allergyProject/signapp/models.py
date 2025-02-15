from django.db import models
from django.contrib.auth.models import AbstractUser
from searchapp.models import Allergy

# Create your models here.
class Customer(AbstractUser):
    cno = models.AutoField(primary_key=True)
    username = models.CharField(max_length=16, unique=True)
    email = models.EmailField(max_length=40)
    phone = models.CharField(max_length=16)
    password = models.TextField()
    birthdate = models.DateField()
    gender = models.BooleanField()
    allerinfo = models.TextField(null=True)
    
    class Meta:
        db_table = "customers" # DB에 표시되고 사용할 테이블 명