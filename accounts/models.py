from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Users(AbstractUser):

    email = models.EmailField(blank=False,null=False, max_length=255,verbose_name="email")
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"