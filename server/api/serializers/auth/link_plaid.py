from rest_framework import serializers
from ..plaid import AccountSerializer, InstitutionSerializer


class LinkPlaidSerializer(serializers.Serializer):
    accounts = AccountSerializer(
        fields=("account_id", "mask", "name", "subtype", "type"), many=True
    )
    institution = InstitutionSerializer()
    token = serializers.CharField()
