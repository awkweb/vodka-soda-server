from django.contrib import admin
from django.contrib.humanize.templatetags.humanize import naturaltime
from server.api.models import UserPhoto


@admin.register(UserPhoto)
class UserPhotoAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'profile_photo',
        'hidden',
        'created',
    )
    ordering = ['-created_at']

    def created(self, obj):
        return naturaltime(obj.created_at)

    def profile_photo(self, obj):
        return obj.order == 0
