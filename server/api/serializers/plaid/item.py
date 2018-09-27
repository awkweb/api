from rest_framework import serializers
from ...models import Item
from ..user import UserSerializer
from .account import AccountSerializer
from .institution import InstitutionSerializer


class ItemSerializer(serializers.ModelSerializer):
    accounts = AccountSerializer(many=True)
    institution = InstitutionSerializer()
    user = UserSerializer()

    class Meta:
        model = Item
        fields = ("id", "item_id", "user", "institution", "date_created", "accounts")
