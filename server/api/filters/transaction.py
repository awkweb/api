from django_filters.rest_framework import (
    DateFromToRangeFilter,
    FilterSet,
    RangeFilter,
    UUIDFilter,
)
from ..models import Transaction


class TransactionFilter(FilterSet):
    amount_cents = RangeFilter(field_name="amount_cents")
    account = UUIDFilter(field_name="account")
    budget = UUIDFilter(field_name="budget")
    date = DateFromToRangeFilter(field_name="date")

    class Meta:
        model = Transaction
        fields = ["account", "amount_cents", "budget", "date"]
