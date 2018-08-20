from rest_framework import serializers
from server.api.models import Balance


class BalanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Balance
        fields = (
            'created_at',
            'id',
            'available',
            'current',
            'limit',
        )
