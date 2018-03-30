from django.contrib.auth import get_user_model
from rest_framework import serializers

from .user_location import UserLocationSerializer
from .user_photo import UserPhotoSerializer


class UserSerializer(serializers.ModelSerializer):
    photos = UserPhotoSerializer(
        many=True,
        read_only=True,
    )
    last_active = serializers.SerializerMethodField()

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

    def get_last_active(self, obj):
        last_location = obj.locations.order_by('-created_at').first()
        serializer = UserLocationSerializer(last_location)
        return serializer.data
