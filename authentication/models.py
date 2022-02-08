from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
  username = models.CharField(max_length = 60, blank = True, null = True, unique = True)
  email = models.EmailField(unique = True)
  phone_no = models.CharField(max_length = 10)
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
  def __str__(self):
      return "{}".format(self.email)  