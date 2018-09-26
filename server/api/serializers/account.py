from ..lib import DynamicFieldsModelSerializer
from ..models import Account


class AccountSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Account
        fields = (
            "account_id",
            "mask",
            "name",
            "official_name",
            "subtype",
            "type",
            "user",
            "institution",
            "date_created",
        )
