from django.utils import timezone
from dry_rest_permissions.generics import DRYPermissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from ..lib import get_month_end_date, get_month_start_date
from ..serializers import BudgetSerializer
from ..models import Budget


class BudgetViewSet(ModelViewSet):
    """
    API endpoint that allows Budgets to be fully manipulated.
    """

    permission_classes = (IsAuthenticated, DRYPermissions)
    serializer_class = BudgetSerializer

    def get_queryset(self):
        user = self.request.auth.user
        now = timezone.now()
        start = self.request.query_params.get("start", get_month_start_date(now))
        end = self.request.query_params.get("end", get_month_end_date(now))
        print(start)
        print(end)
        return Budget.objects.filter(user=user)
