from django.core.exceptions import ObjectDoesNotExist
from rest_framework.serializers import (
    BooleanField,
    CurrentUserDefault,
    ModelSerializer,
    PrimaryKeyRelatedField,
    RelatedField,
)
from ..models import Account, Budget, Transaction
from .plaid.account import AccountSerializer
from .budget import BudgetSerializer
from .transaction_location import TransactionLocationSerializer


class AccountPrimaryKeyRelatedField(RelatedField):
    def to_representation(self, data):
        serializer = AccountSerializer(data, fields=("mask", "name"))
        return serializer.data

    def to_internal_value(self, data):
        try:
            return self.get_queryset().get(pk=data)
        except ObjectDoesNotExist:
            self.fail("does_not_exist", pk_value=data)
        except (TypeError, ValueError):
            self.fail("incorrect_type", data_type=type(data).__name__)


class BudgetPrimaryKeyRelatedField(RelatedField):
    def to_representation(self, data):
        serializer = BudgetSerializer(data, fields=("id", "name"))
        return serializer.data

    def to_internal_value(self, data):
        try:
            return self.get_queryset().get(pk=data)
        except ObjectDoesNotExist:
            self.fail("does_not_exist", pk_value=data)
        except (TypeError, ValueError):
            self.fail("incorrect_type", data_type=type(data).__name__)


class TransactionSerializer(ModelSerializer):
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
            "description",
            "name",
            "origin",
            "origin_id",
            "account",
            "budget",
            "transaction_location",
            "user",
        )
