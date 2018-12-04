from rest_framework.permissions import IsAuthenticated
from dry_rest_permissions.generics import DRYPermissions
from ..models import Account
from ..serializers import AccountSerializer


class AccountViewSet:
    """
    API endpoint that allows Accounts to be updated.
    """

    permission_classes = (IsAuthenticated, DRYPermissions)
    serializer_class = AccountSerializer

    def get_queryset(self):
        user = self.request.auth.user
        return Account.objects.filter(user=user)
