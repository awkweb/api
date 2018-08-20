from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from dry_rest_permissions.generics import DRYPermissions
from server.api.models import Transaction
from server.api.serializers import TransactionSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows transactions to be created, destroyed, edited, or viewed.
    """

    permission_classes = (
        IsAuthenticated,
        DRYPermissions,
    )
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
