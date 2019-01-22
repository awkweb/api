import json
from django.db.transaction import atomic
from django.utils import timezone
from dry_rest_permissions.generics import DRYPermissions
from rest_framework.decorators import action
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from ..filters import TransactionFilter
from ..lib import PlaidClient
from ..models import Account, Budget, Item, Transaction
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
        return Transaction.objects.filter(user=user, date_deleted=None).order_by(
            "-date"
        )

    def destroy(self, request, *args, **kwargs):
        transaction = self.get_object()
        if not transaction.deleted:
            transaction.date_deleted = timezone.now()
            transaction.save()
        return Response(status=HTTP_204_NO_CONTENT)

    @atomic
    @action(detail=False, methods=["post"])
    def delete(self, request):
        transaction_ids = json.loads(request.body)
        for transaction_id in transaction_ids:
            transaction = Transaction.objects.get(id=transaction_id)
            if not transaction.deleted:
                transaction.date_deleted = timezone.now()
                transaction.save()
        return Response(status=HTTP_204_NO_CONTENT)

    @atomic
    @action(detail=False, methods=["post"])
    def categorize(self, request):
        data = json.loads(request.body)
        budget_id = data.get("budget_id")
        transaction_ids = data.get("transaction_ids")
        print(budget_id)
        print(transaction_ids)
        for transaction_id in transaction_ids:
            transaction = Transaction.objects.get(id=transaction_id)
            transaction.budget = Budget.objects.get(id=budget_id)
            transaction.save()
        return Response(status=HTTP_204_NO_CONTENT)
