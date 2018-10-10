from rest_framework.serializers import ModelSerializer
from ...models import TransactionLocation


class TransactionLocationSerializer(ModelSerializer):
    class Meta:
        model = TransactionLocation
        fields = ("id", "address", "city", "state", "zip", "lat", "lon")
