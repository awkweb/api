from rest_framework.serializers import ModelSerializer
from ...models import TransactionPaymentMeta


class TransactionPaymentMetaSerializer(ModelSerializer):
    class Meta:
        model = TransactionPaymentMeta
        fields = ("id", "address", "city", "state", "zip", "lat", "lon")
