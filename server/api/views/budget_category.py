from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from dry_rest_permissions.generics import DRYPermissions
from ..serializers import BudgetCategorySerializer
from ..models import BudgetCategory


class BudgetCategoryViewSet(ModelViewSet):
    """
    API endpoint that allows BudgetCategories to be fully manipulated.
    """

    permission_classes = (IsAuthenticated, DRYPermissions)
    serializer_class = BudgetCategorySerializer

    def get_queryset(self):
        user = self.request.auth.user
        return BudgetCategory.objects.filter(user=user)
