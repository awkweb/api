from dry_rest_permissions.generics import DRYPermissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from ..models import Budget
from ..serializers import BudgetSerializer


class BudgetViewSet(ModelViewSet):
    """
    API endpoint that allows Budgets to be fully manipulated.
    """

    permission_classes = (IsAuthenticated, DRYPermissions)
    serializer_class = BudgetSerializer

    def get_queryset(self):
        user = self.request.auth.user
        return Budget.objects.filter(user=user).order_by("order")
