from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    age = models.IntegerField(
      null=True
    )
    gender = models.CharField(
      default='male',
      max_length=20,
    )
