from rest_framework.serializers import (
    CurrentUserDefault,
    ModelSerializer,
    PrimaryKeyRelatedField,
)
from django.db.models import Sum
from ..models import Budget, Transaction


class BudgetSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(
        queryset=CurrentUserDefault(), write_only=True, default=CurrentUserDefault()
    )

    def to_representation(self, obj):
        transactions = Transaction.objects.filter(budget=obj)
        activity = transactions.aggregate(Sum("amount")).get("amount__sum") or 0
        transaction_count = transactions.count()
        return {
            "id": obj.id,
            "activity": activity,
            "budgeted": obj.amount,
            "date_created": obj.date_created,
            "name": obj.name,
            "order": obj.order,
            "remaining": obj.amount - activity,
            "transaction_count": transaction_count,
        }

    class Meta:
        model = Budget
        fields = ("id", "amount", "name", "order", "user", "date_created")
