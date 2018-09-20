from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField()

    def validate(self, data):
        try:
            user = get_user_model().objects.filter(email=data.get('email'))
            if len(user) > 0:
                raise serializers.ValidationError(_('Email already exists'))
        except get_user_model().DoesNotExist:
            pass

        if not data.get('password') or not data.get('confirm_password'):
            raise serializers.ValidationError(_('Empty Password'))

        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError(_('Mismatch'))

        return data

    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'password',
            'confirm_password'
        )
        extra_kwargs = {'confirm_password': {'read_only': True}}
