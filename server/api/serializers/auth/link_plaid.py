from rest_framework import serializers
from ..plaid import AccountSerializer, InstitutionSerializer


class LinkPlaidSerializer(serializers.Serializer):
    accounts = AccountSerializer(
        many=True, fields=("account_id", "mask", "name", "subtype", "type")
    )
    institution = InstitutionSerializer()
    token = serializers.CharField()
