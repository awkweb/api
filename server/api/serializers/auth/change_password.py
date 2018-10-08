from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _


class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)
    password_verify = serializers.CharField(write_only=True)

    def validate_password(self, password):
        validate_password(password)
        return password

    def validate(self, data):
        if data["password"] != data["password_confirm"]:
            raise serializers.ValidationError(
                _("The two password fields didn't match.")
            )
        return data
