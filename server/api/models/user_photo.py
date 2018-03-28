from django.contrib.gis.db import models
from django.contrib.auth import get_user_model


class UserPhoto(models.Model):
    created_at = models.DateField(
        auto_now_add=True
    )
    url = models.URLField()
    user = models.ForeignKey(
        to=get_user_model(),
        related_name='photos',
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = 'api_user_photo'
        verbose_name = 'user photo'
        verbose_name_plural = 'user photos'

    def __str__(self):
        return self.id
