from django.contrib.gis.db import models
from django.contrib.auth import get_user_model


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
        related_name='locations',
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = 'api_user_location'
        verbose_name = 'user location'
        verbose_name_plural = 'user locations'

    def __str__(self):
        return self.id
