from django.utils import timezone
from dry_rest_permissions.generics import DRYPermissions
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from ..filters import TransactionFilter
from ..models import Transaction
from ..serializers import TransactionSerializer


class TransactionViewSet(ModelViewSet):
    """
    API endpoint that allows Transactions to be fully manipulated.
    """

    permission_classes = (IsAuthenticated, DRYPermissions)
    serializer_class = TransactionSerializer
    filterset_class = TransactionFilter

    def get_queryset(self):
        user = self.request.auth.user
        return Transaction.objects.filter(user=user, date_deleted=None)

    def destroy(self, request, *args, **kwargs):
        transaction = self.get_object()
        if not transaction.deleted:
            transaction.date_deleted = timezone.now()
            transaction.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
