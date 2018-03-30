from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractUser

GENDERS = (
    (0, 'male'),
    (1, 'female'),
)


class User(AbstractUser):
    age = models.IntegerField(
      null=True,
    )
    bio = models.CharField(
        max_length=140,
        null=True,
    )
    display_name = models.CharField(
        max_length=30,
        null=True,
    )
    gender = models.IntegerField(
        default=0,
        choices=GENDERS,
    )
    hidden = models.BooleanField(
        default=False,
        help_text="Designates whether this user should be visible to other users. Select this to hide from all users."
    )

    @staticmethod
    def has_read_permission(request):
        return True

    def has_object_read_permission(self, request):
        return True

    @staticmethod
    def has_write_permission(self):
        return True

    def has_object_write_permission(self, request):
        return request.user == self
