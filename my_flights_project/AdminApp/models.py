from django.db import models
from django.contrib.auth.models import AbstractUser

class UserRole(models.Model):
    role_name = models.CharField(max_length=100)


class User(AbstractUser):
     user_role = models.ForeignKey(UserRole, on_delete=models.CASCADE, null = True)


class Administrator(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user = models.OneToOneField(User,on_delete=models.CASCADE,default=1)



