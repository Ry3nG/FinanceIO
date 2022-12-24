from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
class User(AbstractUser):
    email = models.EmailField(unique=True)
    groups = models.ManyToManyField(Group, related_name='user_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='user_permissions', blank=True)
    
    class Meta:
        app_label = "accounts"
