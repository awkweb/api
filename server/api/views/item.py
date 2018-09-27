from rest_framework.permissions import IsAuthenticated
from dry_rest_permissions.generics import DRYPermissions
from ..lib import DestroyListViewSet
from ..models import Item
from ..serializers import ItemSerializer


class ItemViewSet(DestroyListViewSet):
    """
    API endpoint that allows Items to be deleted or listed.
    """

    permission_classes = (IsAuthenticated, DRYPermissions)
    serializer_class = ItemSerializer

    def get_queryset(self):
        user = self.request.user
        return Item.objects.filter(user=user)
