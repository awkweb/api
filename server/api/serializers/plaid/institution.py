from rest_framework.serializers import ModelSerializer
from ...models import Institution


class InstitutionSerializer(ModelSerializer):
    class Meta:
        model = Institution
        fields = ("color", "institution_id", "name")
        read_only_fields = ("color",)
