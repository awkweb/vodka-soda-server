from datetime import datetime
from math import floor
from django.contrib.auth import get_user_model
from rest_framework import serializers

from .user_location import UserLocationSerializer
from .user_photo import UserPhotoSerializer


class UserSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()
    last_active = serializers.SerializerMethodField()
    photos = UserPhotoSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = get_user_model()
        fields = (
            'age',
            'bio',
            'display_name',
            'id',
            'last_active',
            'photos',
        )
        read_only_fields = (
            'photos',
        )

    def get_age(self, obj):
        delta = datetime.now().date() - obj.birth_date.date()
        years = floor(delta.days / 365)
        return years

    def get_last_active(self, obj):
        last_location = obj.locations.order_by('-created_at').first()
        serializer = UserLocationSerializer(last_location)
        return serializer.data
