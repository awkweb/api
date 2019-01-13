from django.db.transaction import atomic
from dry_rest_permissions.generics import DRYPermissions
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import ModelViewSet
from ..models import Budget
from ..serializers import BudgetSerializer, BudgetDashboardSerializer


class BudgetViewSet(ModelViewSet):
    """
    API endpoint that allows Budgets to be fully manipulated.
    """

    permission_classes = (IsAuthenticated, DRYPermissions)
    serializer_class = BudgetSerializer

    def get_queryset(self):
        user = self.request.auth.user
        return Budget.objects.filter(user=user).order_by("name")

    @action(detail=False, methods=["get"])
    def dashboard(self, request):
        user = request.auth.user
        budgets = Budget.objects.filter(user=user).order_by("name")
        serializer = BudgetDashboardSerializer(
            budgets, context={"request": request}, many=True
        )
        return Response(serializer.data, status=HTTP_200_OK, headers={})
