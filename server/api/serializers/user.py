from django.contrib.auth import get_user_model
from rest_framework import serializers
from .account import AccountSerializer


class UserSerializer(serializers.ModelSerializer):
    accounts = AccountSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'id',
            'first_name',
            'last_name',
            'accounts',
        )
        read_only_fields = (
            'accounts',
        )
