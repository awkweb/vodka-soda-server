from django.contrib import admin
from django.contrib.humanize.templatetags.humanize import naturaltime

from server.api.models import UserLocation


@admin.register(UserLocation)
class UserLocationAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'lon',
        'lat',
        'created',
    )
    ordering = ['-created_at']

    def created(self, obj):
        return naturaltime(obj.created_at)
