from django_filters.rest_framework import DateFilter, FilterSet
from ..models import Transaction


class TransactionFilter(FilterSet):
    min_price = DateFilter(field_name="date", lookup_expr="gte")
    max_price = DateFilter(field_name="date", lookup_expr="lte")

    class Meta:
        model = Transaction
        fields = ["start", "end"]
