from django.contrib.auth import get_user_model

from .user import UserSerializer


class MeSerializer(UserSerializer):

    class Meta:
        model = get_user_model()
        fields = (
            'age',
            'bio',
            'birth_date',
            'date_joined',
            'display_name',
            'email',
            'id',
            'last_active',
            'photos',
        )
