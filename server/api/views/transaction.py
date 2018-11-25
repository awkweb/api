from django.utils import timezone
from dry_rest_permissions.generics import DRYPermissions
from rest_framework.decorators import action
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from ..filters import TransactionFilter
from ..lib import PlaidClient
from ..models import Item, Transaction
from ..serializers import TransactionSerializer

plaid = PlaidClient()


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
        return Response(status=HTTP_204_NO_CONTENT)

    @action(detail=False, methods=["get"])
    def fetch(self, request):
        user = request.auth.user
        items = Item.objects.filter(user=user)
        transactions = []
        for item in items:
            response = plaid.get_transactions(item.access_token)
            transactions += response
        transactions.sort(key=lambda r: r["date"], reverse=True)
        return Response(transactions, status=HTTP_200_OK, headers={})
