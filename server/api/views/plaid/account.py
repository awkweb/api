from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from dry_rest_permissions.generics import DRYPermissions
from server.api.models import Account
from server.api.serializers import AccountSerializer


class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows accounts to be created, destroyed, edited, or viewed.
    """

    permission_classes = (
        IsAuthenticated,
        DRYPermissions,
    )
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
