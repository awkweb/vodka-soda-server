from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now

GENDERS = (
    (-1, 'other'),
    (0, 'male'),
    (1, 'female'),
)


class User(AbstractUser):
    bio = models.CharField(
        blank=True,
        max_length=140,
    )
    birth_date = models.DateTimeField(
        default=now,
    )
    display_name = models.CharField(
        max_length=30,
    )
    gender = models.IntegerField(
        default=0,
        choices=GENDERS,
    )
    hidden = models.BooleanField(
        default=False,
        help_text="Designates whether this user should be visible to other users. Select this to hide from all users."
    )

    REQUIRED_FIELDS = [
        'email',
        'display_name',
    ]

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
