from rest_framework.serializers import (
    CurrentUserDefault,
    ModelSerializer,
    PrimaryKeyRelatedField,
)
from ..models import Budget
from .plaid import (
    AccountSerializer,
    CategorySerializer,
    TransactionLocationSerializer,
    TransactionPaymentMetaSerializer,
)
from .budget import BudgetSerializer


class TransactionSerializer(ModelSerializer):
    account = AccountSerializer()
    budget = BudgetSerializer()
    category = CategorySerializer(required=False)
    transaction_location = TransactionLocationSerializer(required=False)
    transaction_payment_meta = TransactionPaymentMetaSerializer(required=False)
    user = PrimaryKeyRelatedField(
        queryset=CurrentUserDefault(), write_only=True, default=CurrentUserDefault()
    )

    class Meta:
        model = Budget
        fields = (
            "id",
            "amount",
            "category_hierarchy",
            "date",
            "name",
            "note",
            "pending",
            "transaction_id",
            "transaction_type",
            "iso_currency_code",
            "unofficial_currency_code",
            "account",
            "budget",
            "category",
            "transaction_location",
            "transaction_payment_meta",
            "user",
        )
