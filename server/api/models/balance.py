from django.contrib.gis.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from .account import Account


class Balance(models.Model):
    """
    An Account has many Balance but a Balance can have only one Account.
    """

    available = models.DecimalField(_("available"), max_digits=10, decimal_places=2)
    current = models.DecimalField(_("current"), max_digits=10, decimal_places=2)
    limit = models.DecimalField(_("limit"), max_digits=10, decimal_places=2)
    iso_currency_code = models.CharField(
        _("iso_currency_code"), blank=True, max_length=3
    )
    unofficial_currency_code = models.CharField(
        _("unofficial_currency_code"), blank=True, max_length=10
    )
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="balances"
    )
    date_created = models.DateTimeField(_("date_created"), default=timezone.now)

    class Meta:
        verbose_name_plural = "balances"
