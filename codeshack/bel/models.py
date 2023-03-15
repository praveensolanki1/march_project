from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
   name = models.CharField(max_length=100,null=True)
   email = models.EmailField(unique=True)
   bio = models.TextField(null=True,blank=True)


   USERNAME_FIELD = 'email'
   REQUIRED_FIELDS =[]


class Event(models.Model):
   name = models.CharField(max_length=200,null=True)
   description = models.TextField(null=True,blank=True)
   participants = models.ManyToManyField(User,blank=True)
   date = models.DateField()
   created = models.DateTimeField(auto_now=True)
   updated = models.DateTimeField(auto_now_add=True)