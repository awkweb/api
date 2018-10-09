from rest_framework.serializers import (
    CurrentUserDefault,
    ModelSerializer,
    PrimaryKeyRelatedField,
)
from ..models import Budget
from .budget_category import BudgetCategorySerializer


class BudgetSerializer(ModelSerializer):
    budget_category = BudgetCategorySerializer(required=False)
    user = PrimaryKeyRelatedField(
        queryset=CurrentUserDefault(), write_only=True, default=CurrentUserDefault()
    )

    class Meta:
        model = Budget
        fields = ("id", "amount", "name", "budget_category", "user", "date_created")
