from rest_framework.serializers import ModelSerializer
from ...models import Institution


class InstitutionSerializer(ModelSerializer):
    class Meta:
        model = Institution
        fields = ("institution_id", "name")
