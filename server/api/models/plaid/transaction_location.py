from django.contrib.gis.db import models
from django.contrib.auth import get_user_model


class TransactionLocation(models.Model):
    address = models.CharField(
        blank=True,
        max_length=100,
    )
    city = models.CharField(
        blank=True,
        max_length=50,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    lon = models.FloatField(
        verbose_name='longitude',
    )
    lat = models.FloatField(
        verbose_name='latitude',
    )
    point = models.PointField(
        srid=4326,
    )
    state = models.CharField(
        blank=True,
        max_length=2,
    )
    store_number = models.CharField(
        blank=True,
        max_length=30,
    )
    zip_code = models.CharField(
        blank=True,
        max_length=10,
    )

    class Meta:
        db_table = 'api_transaction_location'
        verbose_name = 'transaction location'
        verbose_name_plural = 'transaction locations'

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
