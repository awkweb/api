from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from dry_rest_permissions.generics import DRYPermissions
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
        return Budget.objects.filter(user=user)
