from django.contrib.gis.db import models
from django.contrib.auth import get_user_model


class Institution(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    institution_id = models.CharField(
        blank=True,
        max_length=4,
    )
    name = models.CharField(
        blank=True,
        max_length=100,
    )

    class Meta:
        db_table = 'api_institution'
        verbose_name = 'institution'
        verbose_name_plural = 'institutions'

    def __str__(self):
        return f'{self.id}'

    @staticmethod
    def has_read_permission(request):
        return True

    def has_object_read_permission(self, request):
        return True

    @staticmethod
    def has_write_permission(request):
        return False

    @staticmethod
    def has_create_permission(request):
        return True
