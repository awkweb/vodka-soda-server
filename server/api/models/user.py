from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    age = models.IntegerField(
      null=True
    )
    GENDERS = (
        (0, 'male'),
        (1, 'female'),
    )
    gender = models.IntegerField(
        default=0,
        choices=GENDERS
    )
