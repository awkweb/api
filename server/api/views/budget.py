from django.db.transaction import atomic
from dry_rest_permissions.generics import DRYPermissions
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
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

    @atomic
    @action(detail=False, methods=["post"])
    def reorder(self, request):
        serializer = BudgetSerializer(
            data=request.data, fields=("pk", "order"), many=True
        )
        serializer.is_valid(raise_exception=True)
        for data in request.data:
            budget_id = data["id"]
            order = data["order"]
            budget = Budget.objects.get(id=budget_id)
            budget.order = order
            budget.save()
        return Response({}, status=HTTP_200_OK, headers={})
