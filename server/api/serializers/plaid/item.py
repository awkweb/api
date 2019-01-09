from rest_framework.serializers import ModelSerializer
from ...models import Item
from .account import AccountSerializer
from .institution import InstitutionSerializer


class ItemSerializer(ModelSerializer):
    account = AccountSerializer(
        fields=("account_id", "mask", "name", "subtype", "type")
    )
    institution = InstitutionSerializer()

    class Meta:
        model = Item
        fields = (
            "id",
            "expired",
            "public_token",
            "institution",
            "account",
            "date_created",
        )
