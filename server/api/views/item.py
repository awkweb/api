from os import environ
from Crypto.Cipher import AES
from Crypto import Random
from django.db.transaction import atomic
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from dry_rest_permissions.generics import DRYPermissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT
from rest_framework.viewsets import ModelViewSet
from ..lib import PlaidClient, encrypt, decrypt
from ..models import Account, Institution, Item
from ..serializers import ItemSerializer

plaid = PlaidClient()
sensitive_post_parameters_m = method_decorator(
    sensitive_post_parameters("public_token")
)


class ItemViewSet(ModelViewSet):
    """
    API endpoint that allows Accounts to be deleted, listed, or updated.
    """

    permission_classes = (IsAuthenticated, DRYPermissions)
    serializer_class = ItemSerializer

    def get_queryset(self):
        user = self.request.user
        return Item.objects.filter(user=user)

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super(ItemViewSet, self).dispatch(*args, **kwargs)

    @atomic
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        institution_data = serializer.validated_data["institution"]
        institution, _ = Institution.objects.get_or_create(
            institution_id=institution_data.get("institution_id"),
            name=institution_data.get("name"),
        )

        user = request.auth.user
        public_token = serializer.validated_data["public_token"]
        access_token, item_id = plaid.get_access_token(public_token)

        iv = user.iv_bytes
        item = Item.objects.create(
            access_token=encrypt(access_token, iv),
            item_id=encrypt(item_id, iv),
            public_token=public_token,
            user=user,
            institution=institution,
        )

        account = serializer.validated_data["account"]
        Account.objects.create(
            account_id=account.get("account_id"),
            mask=account.get("mask"),
            name=account.get("name"),
            subtype=account.get("subtype"),
            type=account.get("type"),
            user=user,
            item=item,
        )
        return Response(ItemSerializer(item).data, status=HTTP_200_OK, headers={})

    def destroy(self, request, *args, **kwargs):
        user = request.auth.user
        item = self.get_object()
        iv = user.iv_bytes
        access_token = decrypt(item.access_token, iv)
        plaid.delete_item(access_token)
        Item.delete(item)
        return Response(status=HTTP_204_NO_CONTENT)


from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# todo : add this to item view set
@csrf_exempt
def handle_plaid_hook(request):
    print("webhook")
    print("==============")
    print(request)
    # Sometimes the payload comes in as the request body, sometimes it comes in
    # as a POST parameter. This will handle either case.
    if "payload" in request.POST:
        print("payload")
        payload = json.loads(request.POST["payload"])
    else:
        print("body")
        payload = json.loads(request.body)

    print(payload)
    return Response("Password changed", status=HTTP_200_OK, headers={})
