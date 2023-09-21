from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    id_code = models.CharField(max_length=10,null = True,blank=True)
    mobile = models.CharField(max_length=20,null=True,blank=True)
    image = models.ImageField(upload_to='users',default='user.jpg')











# Create your models here.
