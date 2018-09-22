from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from dry_rest_permissions.generics import DRYPermissions
from ..serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be created, viewed, or edited.
    """

    permission_classes = (
        IsAuthenticated,
        DRYPermissions,
    )
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
