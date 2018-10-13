from django.utils import timezone
from dry_rest_permissions.generics import DRYPermissions
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from ..serializers import TransactionSerializer
from ..models import Transaction


class TransactionViewSet(ModelViewSet):
    """
    API endpoint that allows Transactions to be fully manipulated.
    """

    permission_classes = (IsAuthenticated, DRYPermissions)
    serializer_class = TransactionSerializer

    def get_queryset(self):
        user = self.request.auth.user
        return Transaction.objects.filter(user=user)

    def destroy(self, request, *args, **kwargs):
        transaction = self.get_object()
        if not transaction.deleted:
            transaction.date_deleted = timezone.now()
            transaction.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
