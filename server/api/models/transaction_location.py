import uuid
from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _
from .transaction import Transaction


class TransactionLocation(models.Model):
    """
    A Transaction has only one TransactionLocation and a TransactionLocation has only one Transaction.
    """

    id = models.UUIDField(_("id"), primary_key=True, default=uuid.uuid4, editable=False)
    address = models.CharField(_("address"), max_length=50)
    city = models.CharField(_("city"), max_length=50)
    state = models.CharField(_("state"), max_length=50)
    zip = models.CharField(_("zip"), max_length=10)
    lat = models.FloatField(_("latitude"))
    lon = models.FloatField(_("longitude"))
    transaction = models.OneToOneField(
        Transaction,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="transaction_location",
        verbose_name=_("transaction"),
    )

    class Meta:
        db_table = "api_transaction_location"
        verbose_name = "transaction location"
        verbose_name_plural = "transaction locations"
