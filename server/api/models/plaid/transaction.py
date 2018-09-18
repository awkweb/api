from django.contrib.postgres.fields import ArrayField, JSONField
from django.contrib.gis.db import models
from django.contrib.auth import get_user_model
from .account import Account
from .transaction_location import TransactionLocation


TRANSACTION_TYPE_CHOICES = (
    ('SP', 'Special'),
    ('PL', 'Place'),
)


class Transaction(models.Model):
    amount = models.DecimalField(
        decimal_places=2,
        max_digits=10,
    )
    category = ArrayField(
        models.CharField(
            max_length=50,
            blank=True,
        ),
    )
    category_id = models.CharField(
        blank=True,
        max_length=20,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    date = models.DateField()
    name = models.CharField(
        blank=True,
        max_length=100,
    )
    payment_meta = JSONField()
    pending = models.BooleanField()
    pending_transaction_id = models.CharField(
        blank=True,
        max_length=50,
    )
    transaction_id = models.CharField(
        blank=True,
        max_length=50,
    )
    transaction_type = models.CharField(
        blank=True,
        choices=TRANSACTION_TYPE_CHOICES,
        max_length=2,
    )
    transaction_location = models.OneToOneField(
        TransactionLocation,
        on_delete=models.CASCADE,
    )
    account = models.ForeignKey(
        to=Account,
        related_name='transactions',
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = 'api_transaction'
        verbose_name = 'transaction'
        verbose_name_plural = 'transactions'

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
