from rest_framework import serializers
from server.api.models import Transaction
from .transaction_location import TransactionLocationSerializer


class TransactionSerializer(serializers.ModelSerializer):
    transaction_locations = TransactionLocationSerializer(
        read_only=True,
    )

    class Meta:
        model = Transaction
        fields = (
            'created_at',
            'id',
            'amount',
            'category',
            'category_id',
            'date',
            'name',
            'payment_meta',
            'pending',
            'pending_transaction_id',
            'pending_transaction_id',
            'transaction_id',
            'transaction_type',
            'transaction_locations',
        )
