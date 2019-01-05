from django.utils import timezone
from rest_framework.serializers import CurrentUserDefault, PrimaryKeyRelatedField
from django.db.models import Sum
from ..lib import DynamicFieldsModelSerializer, get_month_end_date, get_month_start_date
from ..models import Budget, Transaction


class BudgetSerializer(DynamicFieldsModelSerializer):
    user = PrimaryKeyRelatedField(
        queryset=CurrentUserDefault(), write_only=True, default=CurrentUserDefault()
    )

    class Meta:
        model = Budget
        fields = ("id", "amount_cents", "name", "order", "user", "date_created")


class BudgetDashboardSerializer(DynamicFieldsModelSerializer):
    def to_representation(self, obj):
        request = self.context.get("request")
        now = timezone.now()
        start_date = request.query_params.get("start_date", get_month_start_date(now))
        end_date = request.query_params.get("end_date", get_month_end_date(now))
        transactions = Transaction.objects.filter(
            budget=obj, date__range=[start_date, end_date], date_deleted=None
        )
        spent = (
            transactions.aggregate(Sum("amount_cents")).get("amount_cents__sum") or 0
        )
        transaction_count = transactions.count()
        return {
            "id": obj.id,
            "budgeted": obj.amount_cents,
            "date_created": obj.date_created,
            "name": obj.name,
            "remaining": obj.amount_cents - spent,
            "spent": spent,
            "transaction_count": transaction_count,
        }

    class Meta:
        model = Budget
