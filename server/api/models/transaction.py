import uuid
from datetime import date
from django.conf import settings
from django.contrib.gis.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from .plaid import Account
from .budget import Budget

PLAID = "PL"
WILBUR = "WI"
VENMO = "VE"
ORIGINS = ((PLAID, "plaid"), (WILBUR, "wilbur"), (VENMO, "venmo"))


class Transaction(models.Model):
    """
    A User has many Transactions but a Transaction has only one User.
    An Account has many Transactions but a Transaction has only one Account.
    A Budget has many Transactions but a Transaction has only one Budget.
    A Transaction has only one TransactionLocation and a TransactionLocation has only one Transaction.
    """

    id = models.UUIDField(_("id"), primary_key=True, default=uuid.uuid4, editable=False)
    amount_cents = models.IntegerField(_("amount cents"))
    currency = models.CharField(_("currency"), blank=True, max_length=3)
    date = models.DateField(_("date"), default=date.today)
    description = models.CharField(_("description"), blank=True, max_length=140)
    name = models.CharField(_("name"), max_length=100)
    origin_id = models.CharField(_("origin id"), blank=True, max_length=50)
    origin = models.CharField(
        _("origin"), max_length=2, choices=ORIGINS, default=WILBUR
    )
    account = models.ForeignKey(
        Account,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="transactions",
        verbose_name=_("account"),
    )
    budget = models.ForeignKey(
        Budget,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="transactions",
        verbose_name=_("budget"),
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("user")
    )
    date_created = models.DateTimeField(_("date created"), default=timezone.now)
    date_deleted = models.DateTimeField(_("date deleted"), blank=True, null=True)

    @property
    def deleted(self):
        return self.date_deleted is not None

    class Meta:
        indexes = [models.Index(fields=["origin_id"])]
        verbose_name_plural = "transactions"

    @staticmethod
    def has_read_permission(request):
        return True

    def has_object_read_permission(self, request):
        return request.user == self.user

    @staticmethod
    def has_write_permission(self):
        return True

    def has_object_write_permission(self, request):
        return request.user == self.user
