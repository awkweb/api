from rest_framework import serializers
from ..account import AccountSerializer
from ..institution import InstitutionSerializer


class LinkPlaidSerializer(serializers.Serializer):
    accounts = AccountSerializer(
        many=True, fields=("account_id", "mask", "name", "subtype", "type")
    )
    institution = InstitutionSerializer()
    token = serializers.CharField()
