from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from dry_rest_permissions.generics import DRYPermissions

from server.api.models import UserPhoto
from server.api.serializers import UserPhotoSerializer


class UserPhotoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows user photos to be viewed or edited.
    """

    permission_classes = (
        IsAuthenticated,
        DRYPermissions,
    )
    queryset = UserPhoto.objects.all()
    serializer_class = UserPhotoSerializer
