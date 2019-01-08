from django.db.transaction import atomic
from django.utils import timezone
from dry_rest_permissions.generics import DRYPermissions
from rest_framework.decorators import action
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from ..filters import TransactionFilter
from ..lib import PlaidClient, decrypt
from ..models import Account, Item, Transaction
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
    @action(detail=False, methods=["get"])
    def fetch(self, request):
        user = request.auth.user
        items = Item.objects.filter(user=user)
        transactions_data = []
        for item in items:
            iv = user.iv_bytes
            access_token = decrypt(item.access_token, iv)
            if item.date_last_fetched is None:
                response = plaid.get_transactions(access_token)
            else:
                response = plaid.get_transactions(
                    access_token, start=item.date_last_fetched
                )
            transactions_data += response
            item.date_last_fetched = timezone.now()
            item.save()

        transactions_lookup = {}
        transactions = []
        for transaction in Transaction.objects.filter(
            user=user, budget=None, date_deleted=None
        ):
            transactions_lookup[transaction.origin_id] = 1
            transactions.append(transaction)

        for transaction_data in transactions_data:
            transaction_id = transaction_data.get("transaction_id")
            if transaction_id in transactions_lookup:
                continue
            else:
                account_id = transaction_data.get("account_id")
                try:
                    account = Account.objects.get(account_id=account_id)
                except Account.DoesNotExist:
                    account = None
                transaction, created = Transaction.objects.get_or_create(
                    amount_cents=transaction_data.get("amount") * 100,
                    currency=transaction_data.get("iso_currency_code"),
                    date=transaction_data.get("date"),
                    name=transaction_data.get("name"),
                    origin_id=transaction_data.get("transaction_id"),
                    origin="PL",
                    account=account,
                    user=user,
                )
                if created or transaction.budget is None:
                    transactions.append(transaction)
                    transaction.new = True

        print(transactions)
        response = TransactionSerializer(
            sorted(
                transactions, key=lambda transaction: transaction.date, reverse=True
            ),
            many=True,
        )

        return Response(response.data, status=HTTP_200_OK, headers={})
