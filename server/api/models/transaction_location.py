from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _


class TransactionLocation(models.Model):
    """
    A Transaction has only one TransactionLocation and a TransactionLocation has only one Transaction.
    """

    address = models.CharField(_("address"), max_length=50)
    city = models.CharField(_("city"), max_length=50)
    state = models.CharField(_("state"), max_length=50)
    zip = models.CharField(_("zip"), max_length=10)
    lat = models.FloatField(verbose_name="latitude")
    lon = models.FloatField(verbose_name="longitude")

    class Meta:
        verbose_name_plural = "transaction locations"
