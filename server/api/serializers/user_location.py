from rest_framework import serializers
from server.api.models import UserLocation
from rest_framework import mixins


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
        write_only_fields = (
            'user',
        )
