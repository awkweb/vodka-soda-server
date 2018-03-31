from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from dry_rest_permissions.generics import DRYPermissions

from server.api.serializers import MeSerializer


class MeView(generics.GenericAPIView):
    """
    API endpoint that retrieves the current user.
    """

    permission_classes = (
        IsAuthenticated,
        DRYPermissions,
    )
    serializer_class = MeSerializer

    def get(self, request, *args, **kwargs):
        serializer = MeSerializer(request.user).data
        return Response(serializer)
