from rest_framework.serializers import ModelSerializer
from ...models import Item
from .institution import InstitutionSerializer


class ItemSerializer(ModelSerializer):
    institution = InstitutionSerializer()

    class Meta:
        model = Item
        fields = ("id", "item_id", "institution", "date_created")
