from django.contrib.auth import authenticate
from rest_framework import serializers, exceptions
from django.utils.translation import gettext_lazy as _


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(style={"input_type": "password"})

    def authenticate(self, **kwargs):
        return authenticate(self.context["request"], **kwargs)

    def _validate_email(self, email, password):
        user = None

        if email and password:
            user = self.authenticate(email=email, password=password)
        else:
            raise exceptions.ValidationError(_('Must include "email" and "password".'))

        return user

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        user = self._validate_email(email, password)

        if user:
            if not user.is_active:
                raise exceptions.ValidationError(_("User account is disabled."))
        else:
            raise exceptions.ValidationError(
                _("Unable to log in with provided credentials.")
            )

        attrs["user"] = user
        return attrs
