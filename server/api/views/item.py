from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from dry_rest_permissions.generics import DRYPermissions
from ..lib import DestroyListUpdateViewSet, PlaidClient
from ..models import Item
from ..serializers import ItemSerializer

plaid = PlaidClient()


class ItemViewSet(DestroyListUpdateViewSet):
    """
    API endpoint that allows Items to be deleted, listed, or updated.
    """

    permission_classes = (IsAuthenticated, DRYPermissions)
    serializer_class = ItemSerializer

    def get_queryset(self):
        user = self.request.user
        return Item.objects.filter(user=user)

    def destroy(self, request, *args, **kwargs):
        item = self.get_object()
        plaid.delete_item(item.access_token)
        Item.delete(item)
        return Response(status=HTTP_204_NO_CONTENT)
