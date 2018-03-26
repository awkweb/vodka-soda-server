from django.contrib.auth import get_user_model
from django.contrib.gis.db import models


class UserLocation(models.Model):
    created_at = models.DateField(
        auto_now_add=True
    )
    lon = models.FloatField(
        verbose_name='longitude'
    )
    lat = models.FloatField(
        verbose_name='latitude'
    )
    point = models.PointField(
        srid=32140
    )
    user = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self
