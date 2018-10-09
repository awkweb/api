from rest_framework.serializers import ModelSerializer
from ..models import BudgetCategory


class BudgetCategorySerializer(ModelSerializer):
    class Meta:
        model = BudgetCategory
        fields = ("id", "name", "user", "date_created")
