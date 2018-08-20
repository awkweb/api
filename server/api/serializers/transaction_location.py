from rest_framework import serializers
from server.api.models import TransactionLocation


class TransactionLocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = TransactionLocation
        fields = (
            'created_at',
            'id',
            'address',
            'city',
            'lon',
            'lat',
            'point',
            'state',
            'store_number',
            'zip_code',
        )
