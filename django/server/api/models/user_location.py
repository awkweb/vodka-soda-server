from django.contrib.gis.db import models
from django.contrib.auth import get_user_model


class UserLocation(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    lon = models.FloatField(
        verbose_name='longitude',
    )
    lat = models.FloatField(
        verbose_name='latitude',
    )
    point = models.PointField(
        srid=4326,
    )
    user = models.ForeignKey(
        to=get_user_model(),
        related_name='locations',
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = 'api_user_location'
        verbose_name = 'location'
        verbose_name_plural = 'locations'

    def __str__(self):
        return f'{self.id}'

    @staticmethod
    def has_read_permission(request):
        return True

    def has_object_read_permission(self, request):
        return True

    @staticmethod
    def has_write_permission(request):
        return False

    @staticmethod
    def has_create_permission(request):
        return True
