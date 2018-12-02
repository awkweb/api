from rest_framework.serializers import (
    BooleanField,
    CurrentUserDefault,
    ModelSerializer,
    PrimaryKeyRelatedField,
)
from ..models import Account, Budget, Transaction
from .transaction_location import TransactionLocationSerializer


class AccountPrimaryKeyRelatedField(PrimaryKeyRelatedField):
    def get_queryset(self):
        request = self.context.get("request", None)
        queryset = super(AccountPrimaryKeyRelatedField, self).get_queryset()
        if not request or not queryset:
            return None
        account_id = request.data["account"]
        return queryset.filter(id=account_id)


class BudgetPrimaryKeyRelatedField(PrimaryKeyRelatedField):
    def get_queryset(self):
        request = self.context.get("request", None)
        queryset = super(BudgetPrimaryKeyRelatedField, self).get_queryset()
        if not request or not queryset:
            return None
        budget_id = request.data["budget"]
        return queryset.filter(id=budget_id)


class TransactionSerializer(ModelSerializer):
    new = BooleanField(default=False, read_only=True)
    account = AccountPrimaryKeyRelatedField(
        allow_null=True, queryset=Account.objects, required=False
    )
    budget = BudgetPrimaryKeyRelatedField(queryset=Budget.objects, required=False)
    transaction_location = TransactionLocationSerializer(
        allow_null=True, required=False
    )
    user = PrimaryKeyRelatedField(
        queryset=CurrentUserDefault(), write_only=True, default=CurrentUserDefault()
    )

    class Meta:
        model = Transaction
        fields = (
            "id",
            "amount_cents",
            "currency",
            "date",
            "name",
            "note",
            "origin",
            "origin_id",
            "account",
            "budget",
            "transaction_location",
            "user",
            "new",
        )
