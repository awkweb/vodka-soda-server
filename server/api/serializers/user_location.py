from rest_framework import serializers
from server.api.models import UserLocation


class UserLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLocation
        fields = (
            'created_at',
            'id',
            'lon',
            'lat',
            'point',
        )
