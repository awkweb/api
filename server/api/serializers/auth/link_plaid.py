from rest_framework import serializers


class LinkPlaidSerializer(serializers.Serializer):
    public_token = serializers.CharField()
