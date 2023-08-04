from django.db import models
from django.contrib.auth.models import AbstractUser


class UserRole(models.Model):
    role_name = models.CharField(max_length=100)

"""
Custom User model that inherits from AbstractUser, extending the default user model
"""
class User(AbstractUser):
    user_role = models.ForeignKey(UserRole, on_delete=models.CASCADE,
                                  null=True)
    

"""
Change the related_name of 'groups' and 'user_permissions' fields in the User model
"""
User._meta.get_field('groups').remote_field.related_name = 'custom_user_groups'
User._meta.get_field('user_permissions').remote_field.related_name = 'custom_user_permissions'

class Administrator(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    
