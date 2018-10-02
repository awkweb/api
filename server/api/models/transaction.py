import uuid
from django.conf import settings
from django.contrib.gis.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import ugettext_lazy as _
from .plaid import Account, Category
from .budget import Budget
from .transaction_location import TransactionLocation
from .transaction_payment_meta import TransactionPaymentMeta

DIGITAL = "DI"
PLACE = "PL"
SPECIAL = "SP"
UNRESOLVED = "UN"
TRANSACTION_TYPES = (
    (DIGITAL, "digital"),
    (PLACE, "place"),
    (SPECIAL, "special"),
    (UNRESOLVED, "unresolved"),
)


class Transaction(models.Model):
    """
    A User has many Transactions but a Transaction has only one User.
    An Institution has many Transactions but a Transaction has only one Institution.
    A Transaction has many Categories and a Category has many Transactions.
    """

    id = models.UUIDField(_("id"), primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.DecimalField(_("amount"), max_digits=10, decimal_places=2)
    category_hierarchy = (
        _("category hierarchy"),
        ArrayField(models.CharField(max_length=25, blank=True), size=8),
    )
    date = models.DateField(_("date"))
    name = models.CharField(_("name"), max_length=100)
    note = models.CharField(_("note"), max_length=140)
    pending = models.BooleanField(_("date"), default=True)
    transaction_id = models.CharField(_("transaction id"), max_length=50)
    transaction_type = models.CharField(
        _("transaction type"), max_length=2, choices=TRANSACTION_TYPES, default=DIGITAL
    )
    iso_currency_code = models.CharField(
        _("iso currency code"), blank=True, max_length=3
    )
    unofficial_currency_code = models.CharField(
        _("unofficial currency code"), blank=True, max_length=10
    )
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name="transactions",
        verbose_name=_("account"),
    )
    budget = models.ForeignKey(
        Budget,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="transactions",
        verbose_name=_("budget"),
    )
    category = models.ForeignKey(
        Category,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="transactions",
        verbose_name=_("category"),
    )
    transaction_location = models.OneToOneField(
        TransactionLocation,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="transactions",
        verbose_name=_("transaction location"),
    )
    transaction_payment_meta = models.OneToOneField(
        TransactionPaymentMeta,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="transactions",
        verbose_name=_("transaction payment meta"),
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("user")
    )

    class Meta:
        indexes = [models.Index(fields=["transaction_id"])]
        verbose_name_plural = "transactions"
