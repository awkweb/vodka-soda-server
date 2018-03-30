from rest_framework import serializers

from server.api.models import UserPhoto


class UserPhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserPhoto
        fields = (
            'created_at',
            'id',
            'order',
            'url',
        )
        write_only_fields = (
            'user',
        )
