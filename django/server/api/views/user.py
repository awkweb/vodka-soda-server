from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from dry_rest_permissions.generics import DRYPermissions

from server.api.serializers import (
    UserPhotoSerializer, UserSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    permission_classes = (
        IsAuthenticated,
        DRYPermissions,
    )
    queryset = get_user_model().objects.all()\
        .filter(hidden=False)\
        .order_by('-date_joined')
    serializer_class = UserSerializer

    @detail_route(
        methods=['get'],
        permission_classes=[DRYPermissions],
        url_path='photos'
    )
    def photos(self, request, pk=None):
        """
        Returns a list of all photos the user has.
        """

        user = self.get_object()
        photos = user.photos.all().order_by('order')
        return Response([UserPhotoSerializer(photo).data for photo in photos])

