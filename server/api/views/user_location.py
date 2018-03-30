from rest_framework.permissions import IsAuthenticated
from dry_rest_permissions.generics import DRYPermissions

from server.api.models import UserLocation
from server.api.serializers import UserLocationSerializer
from server.api.utils import CreateOnlyModelViewSet


class UserLocationViewSet(CreateOnlyModelViewSet):
    """
    API endpoint that allows user locations to be created.
    """

    permission_classes = (
        IsAuthenticated,
        DRYPermissions,
    )
    queryset = UserLocation.objects.all()
    serializer_class = UserLocationSerializer
