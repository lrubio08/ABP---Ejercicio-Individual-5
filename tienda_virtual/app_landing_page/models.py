from django.contrib.auth.models import AbstractUser, Permission
from django.db import models
from django.contrib.contenttypes.models import ContentType

# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    #Campos adicionales
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return self.username
