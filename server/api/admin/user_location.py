from django.contrib import admin
from server.api.models import UserLocation


@admin.register(UserLocation)
class UserLocationAdmin(admin.ModelAdmin):
    pass
