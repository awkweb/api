from rest_framework.serializers import (
    CharField,
    CurrentUserDefault,
    DateField,
    ModelSerializer,
    PrimaryKeyRelatedField,
)
from ..models import Budget, Transaction
from .plaid import (
    AccountSerializer,
    CategorySerializer,
    TransactionLocationSerializer,
    TransactionPaymentMetaSerializer,
)


class BudgetPrimaryKeyRelatedField(PrimaryKeyRelatedField):
    def get_queryset(self):
        request = self.context.get("request", None)
        queryset = super(BudgetPrimaryKeyRelatedField, self).get_queryset()
        if not request or not queryset:
            return None
        budget_id = request.data["budget"]
        return queryset.filter(id=budget_id)


class TransactionSerializer(ModelSerializer):
    date = DateField(required=False)
    note = CharField(required=False)
    account = AccountSerializer(required=False)
    budget = BudgetPrimaryKeyRelatedField(queryset=Budget.objects, write_only=True)
    category = CategorySerializer(required=False)
    transaction_location = TransactionLocationSerializer(required=False)
    transaction_payment_meta = TransactionPaymentMetaSerializer(required=False)
    user = PrimaryKeyRelatedField(
        queryset=CurrentUserDefault(), write_only=True, default=CurrentUserDefault()
    )

    class Meta:
        model = Transaction
        fields = (
            "id",
            "amount",
            "date",
            "name",
            "note",
            "account",
            "budget",
            "category",
            "transaction_location",
            "transaction_payment_meta",
            "user",
        )
