from django.contrib.gis.db import models
from django.contrib.auth import get_user_model
from .balance import Balance
from .institution import Institution

SUBTYPE_CHOICES = (
    ('SA', 'Savings'),
    ('CH', 'Checking'),
    ('CD', 'CD'),
    ('CC', 'Credit Card'),
    ('MM', 'Money Market'),
)

TYPE_CHOICES = (
    ('C', 'Credit'),
    ('D', 'Depository'),
)


class Account(models.Model):
    a_subtype = models.CharField(
        blank=True,
        choices=SUBTYPE_CHOICES,
        max_length=2,
    )
    a_type = models.CharField(
        blank=True,
        choices=TYPE_CHOICES,
        max_length=2,
    )
    account_id = models.CharField(
        blank=True,
        max_length=50,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    mask = models.CharField(
        blank=True,
        max_length=4,
    )
    name = models.CharField(
        blank=True,
        max_length=50,
    )
    official_name = models.CharField(
        blank=True,
        max_length=100,
    )
    balance = models.OneToOneField(
        Balance,
        on_delete=models.CASCADE,
    )
    institution = models.OneToOneField(
        Institution,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        to=get_user_model(),
        related_name='accounts',
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = 'api_account'
        verbose_name = 'account'
        verbose_name_plural = 'accounts'

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
