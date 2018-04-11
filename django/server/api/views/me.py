from rest_framework import generics
from rest_framework.response import Response

from server.api.serializers import MeSerializer


class MeView(generics.GenericAPIView):
    """
    API endpoint that retrieves the current user.
    """

    serializer_class = MeSerializer

    def get(self, request, *args, **kwargs):
        serializer = MeSerializer(request.user).data
        return Response(serializer)
