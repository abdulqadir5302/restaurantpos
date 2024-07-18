from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser,BaseUserManager

# Create your models here.
class CustomUserManager(BaseUserManager):
    def get_by_natural_key(self, email):
        return self.get(email=email)

class CustomUser(AbstractBaseUser):

    user_id = models.IntegerField(primary_key = True)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length= 100, unique=True)
    password = models.CharField(max_length=100)

    #Email for login
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    def __str__(self):
        return self.email