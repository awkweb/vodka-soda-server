from django.contrib.auth import get_user_model
from rest_framework import serializers
from server.api.models import UserPhoto


class UserSerializer(serializers.HyperlinkedModelSerializer):
    photos = serializers.PrimaryKeyRelatedField(many=True, queryset=UserPhoto.objects.all())

    class Meta:
        model = get_user_model()
        fields = (
            'url',
            'age',
            'email',
            'id',
            'photos',
        )
        read_only_fields = ('email',)
