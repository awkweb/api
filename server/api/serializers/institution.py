from rest_framework import serializers
from server.api.models import Institution


class InstitutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Institution
        fields = (
            'created_at',
            'id',
            'institution_id',
            'name',
        )
