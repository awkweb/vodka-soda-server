from rest_framework import mixins
from rest_framework import viewsets


class CreateOnlyModelViewSet(mixins.CreateModelMixin,
                             viewsets.GenericViewSet):
    """
    A viewset that provides a default `create()` action.
    """
    pass
