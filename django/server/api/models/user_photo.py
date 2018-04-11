from django.contrib.gis.db import models
from django.contrib.auth import get_user_model


class UserPhoto(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    hidden = models.BooleanField(
        default=False,
    )
    order = models.IntegerField()
    url = models.URLField()
    user = models.ForeignKey(
        to=get_user_model(),
        related_name='photos',
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = 'api_user_photo'
        verbose_name = 'photo'
        verbose_name_plural = 'photos'
        ordering = ['order']

    def __str__(self):
        return f'{self.id}'

    @staticmethod
    def has_read_permission(request):
        return True

    def has_object_read_permission(self, request):
        return True

    @staticmethod
    def has_write_permission(self):
        return True

    def has_object_write_permission(self, request):
        return request.user == self.user

