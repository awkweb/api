from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..lib import PlaidClient

plaid = PlaidClient()


class FetchTransactionsView(GenericAPIView):
    permission_classes = IsAuthenticated

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_user(request)
        public_token = serializer.validated_data["public_token"]
        access_token = plaid.get_access_token(public_token)
        transactions = plaid.get_transactions(access_token)
        return Response(
            {"transactions": transactions}, status=status.HTTP_200_OK, headers={}
        )
