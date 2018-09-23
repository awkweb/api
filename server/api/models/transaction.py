from django.conf import settings
from django.contrib.gis.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import ugettext_lazy as _
from .account import Account
from .budget import Budget
from .category import Category
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

    amount = models.DecimalField(_("amount"), max_digits=10, decimal_places=2)
    category_hierarchy = (
        _("category_hierarchy"),
        ArrayField(models.CharField(max_length=25, blank=True), size=8),
    )
    date = models.DateField(_("date"))
    name = models.CharField(_("name"), max_length=100)
    note = models.CharField(_("note"), max_length=140)
    pending = models.BooleanField(_("date"), default=True)
    transaction_id = models.CharField(_("transaction_id"), max_length=50)
    transaction_type = models.CharField(
        _("transaction_type"), max_length=2, choices=TRANSACTION_TYPES, default=DIGITAL
    )
    iso_currency_code = models.CharField(
        _("iso_currency_code"), blank=True, max_length=3
    )
    unofficial_currency_code = models.CharField(
        _("unofficial_currency_code"), blank=True, max_length=10
    )
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="transactions"
    )
    budget = models.ForeignKey(
        Budget, on_delete=models.CASCADE, related_name="transactions"
    )
    category = models.ForeignKey(
        Category, models.SET_NULL, blank=True, null=True, related_name="transactions"
    )
    transaction_location = models.OneToOneField(
        TransactionLocation, on_delete=models.CASCADE, related_name="transactions"
    )
    transaction_payment_meta = models.OneToOneField(
        TransactionPaymentMeta, on_delete=models.CASCADE, related_name="transactions"
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "accounts"
