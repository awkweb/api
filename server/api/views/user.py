from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from dry_rest_permissions.generics import DRYPermissions
from ..lib import CreateDestroyRetrieveUpdateViewSet
from ..serializers import UserSerializer


class UserViewSet(CreateDestroyRetrieveUpdateViewSet):
    """
    API endpoint that allows Users to be created, viewed, or edited.
    """

    permission_classes = (IsAuthenticated, DRYPermissions)
    serializer_class = UserSerializer

    def get_queryset(self):
        return get_user_model().objects.filter(pk=self.request.auth.user.id)
