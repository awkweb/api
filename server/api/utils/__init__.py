from django.contrib.auth import get_user_model
from .viewsets import CreateOnlyModelViewSet


def email_address_exists(email):
    return get_user_model().objects.filter(email__iexact=email).exists()
