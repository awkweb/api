from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.views.decorators.debug import sensitive_post_parameters
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers import ChangePasswordSerializer, LoginSerializer, RegisterSerializer

sensitive_post_parameters_m = method_decorator(
    sensitive_post_parameters("password", "password_confirm", "password_verify")
)


class ChangePasswordView(GenericAPIView):
    """
    API endpoint that allows an user to login
    """

    permission_classes = (AllowAny,)
    serializer_class = ChangePasswordSerializer

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super(ChangePasswordView, self).dispatch(*args, **kwargs)

    def patch(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        password_verify = serializer.validated_data["password_verify"]
        user = request.auth.user
        if not user.check_password(password_verify):
            return Response(
                {"password_verify": ["Incorrect password"]},
                status=HTTP_400_BAD_REQUEST,
                headers={},
            )
        password = serializer.validated_data["password"]
        user.set_password(password)
        user.save()
        return Response("Password changed", status=HTTP_200_OK, headers={})


class LoginView(GenericAPIView):
    """
    API endpoint that allows an user to login
    """

    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super(LoginView, self).dispatch(*args, **kwargs)

    def get_response_data(self, user):
        token, created = Token.objects.get_or_create(user=user)
        return {
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "id": user.pk,
            "token": token.key,
        }

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        return Response(self.get_response_data(user), status=HTTP_200_OK, headers={})


class LogoutView(APIView):
    """
    API endpoint that allows an user to logout
    """

    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        response = self.http_method_not_allowed(request, *args, **kwargs)
        return self.finalize_response(request, response, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return Response({"detail": _("Successfully logged out.")}, status=HTTP_200_OK)


class RegisterView(CreateAPIView):
    """
    API endpoint that allows an user to register
    """

    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super(RegisterView, self).dispatch(*args, **kwargs)

    def get_response_data(self, user):
        token, created = Token.objects.get_or_create(user=user)
        return {"id": user.pk, "email": user.email, "token": token.key}

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(
            self.get_response_data(user), status=HTTP_201_CREATED, headers=headers
        )
