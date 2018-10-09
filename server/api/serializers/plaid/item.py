from rest_framework.serializers import ModelSerializer
from ...models import Item
from ..user import UserSerializer
from .account import AccountSerializer
from .institution import InstitutionSerializer


class ItemSerializer(ModelSerializer):
    accounts = AccountSerializer(many=True)
    institution = InstitutionSerializer()
    user = UserSerializer()

    class Meta:
        model = Item
        fields = ("id", "item_id", "user", "institution", "date_created", "accounts")
