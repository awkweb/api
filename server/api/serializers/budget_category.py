from rest_framework.serializers import (
    CurrentUserDefault,
    ModelSerializer,
    PrimaryKeyRelatedField,
)
from ..models import BudgetCategory


class BudgetCategorySerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(
        queryset=CurrentUserDefault(), write_only=True, default=CurrentUserDefault()
    )

    class Meta:
        model = BudgetCategory
        fields = ("id", "name", "user", "date_created")
