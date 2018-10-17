from rest_framework.serializers import ModelSerializer
from ...models import Balance


class BalanceSerializer(ModelSerializer):
    class Meta:
        model = Balance
        fields = (
            "id",
            "available",
            "current",
            "limit",
            "iso_currency_code",
            "unofficial_currency_code",
            "account",
            "date_created",
        )
