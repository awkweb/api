import json
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)
from rest_framework.response import Response
from dry_rest_permissions.generics import DRYPermissions
from server.api.serializers import (
    UserSerializer, UserRegisterSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be created, viewed, or edited.
    """

    permission_classes = (
        IsAuthenticated,
        DRYPermissions,
    )
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    @action(methods=['post'], detail=True, permission_classes=[AllowAny])
    def register(self, request, pk=None):
        if request.auth is None:
            data = request.data
            data = data.dict()
            serializer = UserRegisterSerializer(data=data)
            if serializer.is_valid():
                Response(json.loads(data))
        #         try:
        #             with transaction.atomic():
        #                 user = serializer.save()
        #
        #                 url, headers, body, token_status = self.create_token_response(request)
        #                 if token_status != 200:
        #                     raise Exception(json.loads(body).get("error_description", ""))
        #
        #                 return Response(json.loads(body), status=token_status)
        #         except Exception as e:
        #             return Response(data={"error": e.message}, status=status.HTTP_400_BAD_REQUEST)
        #     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # return Response(status=status.HTTP_403_FORBIDDEN)



        # user = self.get_object()
        # serializer = PasswordSerializer(data=request.data)
        # if serializer.is_valid():
        #     user.set_password(serializer.data['password'])
        #     user.save()
        #     return Response({'status': 'password set'})
        # else:
        #     return Response(serializer.errors,
        #                     status=status.HTTP_400_BAD_REQUEST)
