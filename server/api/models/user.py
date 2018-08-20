from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(
        blank=True,
        max_length=30,
    )

    @staticmethod
    def has_read_permission(request):
        return True

    def has_object_read_permission(self, request):
        return True

    @staticmethod
    def has_write_permission(self):
        return True

    def has_object_write_permission(self, request):
        return request.user == self
