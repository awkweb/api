from rest_framework import serializers
from server.api.models import Account
from .balance import BalanceSerializer
from .institution import InstitutionSerializer
from .transaction import TransactionSerializer


class AccountSerializer(serializers.ModelSerializer):
    balance = BalanceSerializer(
        read_only=True,
    )
    instituion = InstitutionSerializer(
        read_only=True,
    )
    transactions = TransactionSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Account
        fields = (
            'created_at',
            'id',
            'a_subtype',
            'a_type',
            'account_id',
            'account_id',
            'mask',
            'name',
            'official_name',
            'balance',
            'institution',
            'transactions',
        )
        read_only_fields = (
            'balance',
            'institution',
            'transactions',
        )
