import datetime
from django.http import HttpResponse, HttpResponseForbidden
from django.db.transaction import atomic
from django.core.exceptions import SuspiciousOperation
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from dry_rest_permissions.generics import DRYPermissions
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT
from rest_framework.viewsets import ModelViewSet
from ..lib import PlaidClient
from ..models import Account, Institution, Item, Transaction
from ..serializers import ItemSerializer

plaid = PlaidClient()
sensitive_post_parameters_m = method_decorator(
    sensitive_post_parameters("public_token")
)


class ItemViewSet(ModelViewSet):
    """
    API endpoint that allows Accounts to be created, deleted, listed, or updated.
    """

    permission_classes = (IsAuthenticated, DRYPermissions)
    serializer_class = ItemSerializer

    def get_queryset(self):
        user = self.request.user
        return Item.objects.filter(user=user).order_by("date_created")

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super(ItemViewSet, self).dispatch(*args, **kwargs)

    def list(self, request):
        user = request.user
        items = Item.objects.filter(user=user).order_by("institution__name")
        for item in items:
            print(item.institution, item._access_token)
            if item.expired:
                public_token = plaid.get_public_token(item._access_token)
                item.public_token = public_token
                item.save()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    @atomic
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        institution_data = serializer.validated_data["institution"]
        institution, _ = Institution.objects.get_or_create(
            institution_id=institution_data.get("institution_id"),
            name=institution_data.get("name"),
        )

        user = request.auth.user
        public_token = serializer.validated_data["public_token"]
        access_token, item_id = plaid.get_access_token(public_token)
        item = Item.objects.create(
            access_token=access_token,
            item_id=item_id,
            public_token=public_token,
            user=user,
            institution=institution,
        )

        account = serializer.validated_data["account"]
        Account.objects.create(
            account_id=account.get("account_id"),
            mask=account.get("mask"),
            name=account.get("name"),
            subtype=account.get("subtype"),
            type=account.get("type"),
            user=user,
            item=item,
        )
        return Response(ItemSerializer(item).data, status=HTTP_200_OK, headers={})

    def destroy(self, request, *args, **kwargs):
        item = self.get_object()
        plaid.delete_item(item._access_token)
        Item.delete(item)
        return Response(status=HTTP_204_NO_CONTENT)

    @action(detail=False, methods=["post"], permission_classes=(AllowAny,))
    def hooks(self, request):
        try:
            data = request.data
            webhook_code = data.get("webhook_code")
            if webhook_code is None:
                return HttpResponseForbidden("Invalid signature header")

            if webhook_code == "TRANSACTIONS_REMOVED":
                transaction_ids = data.get("removed_transactions")
                Transaction.objects.filter(origin_id__in=transaction_ids).delete()
                return HttpResponse()

            item_id = data.get("item_id")
            item = Item.objects.get(item_id=item_id)
            if webhook_code == "INITIAL_UPDATE" or webhook_code == "DEFAULT_UPDATE":
                new_transactions = data.get("new_transactions")
                response = plaid.get_transactions(
                    item._access_token, count=new_transactions
                )
                transactions = []
                for transaction in response:
                    amount_cents = transaction.get("amount") * 100
                    account = Account.objects.get(item_id=item.id)
                    currency = transaction.get("iso_currency_code")
                    date = transaction.get("date")
                    name = transaction.get("name")
                    origin_id = transaction.get("transaction_id")
                    transactions.append(
                        Transaction(
                            amount_cents=amount_cents,
                            currency=currency,
                            date=date,
                            name=name,
                            origin_id=origin_id,
                            origin="PL",
                            account=account,
                            user=item.user,
                        )
                    )
                Transaction.objects.bulk_create(transactions)
                return HttpResponse()

            elif webhook_code == "HISTORICAL_UPDATE":
                start = datetime.datetime.utcnow() - datetime.timedelta(days=1095)
                new_transactions = data.get("new_transactions")
                response = plaid.get_transactions(
                    item._access_token, count=new_transactions, start=start
                )
                transactions = []
                for transaction in response:
                    try:
                        origin_id = transaction.get("transaction_id")
                        Transaction.objects.get(origin_id=origin_id)
                    except Transaction.DoesNotExist:
                        amount_cents = transaction.get("amount") * 100
                        account = Account.objects.get(item_id=item.id)
                        currency = transaction.get("iso_currency_code")
                        date = transaction.get("date")
                        name = transaction.get("name")
                        transactions.append(
                            Transaction(
                                amount_cents=amount_cents,
                                currency=currency,
                                date=date,
                                name=name,
                                origin_id=origin_id,
                                origin="PL",
                                account=account,
                                user=item.user,
                            )
                        )
                Transaction.objects.bulk_create(transactions)
                return HttpResponse()

            elif webhook_code == "ERROR":
                public_token = plaid.get_public_token(item._access_token)
                item.expired = True
                item.public_token = public_token
                item.save()
                return HttpResponse()

        except SuspiciousOperation:
            return HttpResponseForbidden("Invalid signature header")
